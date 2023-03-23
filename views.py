from django.shortcuts import render, redirect
from django.template import context
from django.utils import timezone
from sa_final.models import CLIST
from sa_final.models import delivery
from sa_final.models import WMODE
from sa_final.models import LMODE
from sa_final.models import FMODE
from sa_final.models import lock
from sa_final.models import shop
from django.db.models import Sum
from sa_final.models import LOGIN
from sa_final.models import solve
from sa_final.models import order, USER
from django.http import HttpResponse, HttpResponseRedirect
import math
from datetime import datetime,timedelta
import datetime
import requests
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.contrib import messages
import uuid


def index(request):
    if 'UserID' in request.session:
        return render(request, "index.html", locals())
    else:
        return HttpResponseRedirect("/login2")


#解鎖
def unlock(request):
    goal_all = [50,500,1500,3000]
    sum_p = CLIST.objects.all().aggregate(Sum('PRICE'))['PRICE__sum']

    if sum_p <= goal_all[0]:
        goal_p = goal_all[0]

    elif sum_p <= goal_all[1]:
        goal_p = goal_all[1]

    elif sum_p <= goal_all[2]:
        goal_p = goal_all[2]

    elif sum_p <= goal_all[3]:
        goal_p = goal_all[3]

    width = sum_p/goal_p*100
    context = {'sum_p': sum_p, 'goal_p':goal_p, 'width':width}

    return render(request, "unlock.html", context)

def map(request):
    return render(request, "map.html")

#歷史紀錄
def history(request):
    ord=order.objects.all()
    return render(request, "history.html",locals())

#訂單詳情頁
def detail(request,detail_id):
    detail_time=order.objects.get(ORDID=detail_id)
    detail_id=CLIST.objects.get(ORDID=detail_id)
    return render(request, "detail.html",locals())

def question(request):
    if request.method == 'POST':
        Qtype = request.POST.get('qtype')
        Qtext = request.POST.get('qtext')
        solve.objects.create(QTYPE=Qtype, QTEXT=Qtext)
        return render(request, "index.html")
    elif request.method == 'GET':
        return render(request, "solve.html")

def bag(request):
    return render(request, "bag.html")


def orders(request):
    if request.method == 'GET':
        return render(request, "order.html", locals())
    elif request.method == 'POST':
        #取表單的值
        wash = request.POST.get('washmode')
        WASH=WMODE.objects.get(WMODE=wash)
        dry = request.POST.get('drymode')
        DRY=LMODE.objects.get(LMODE=dry)
        fold = request.POST.get('foldmode')
        FOLD=FMODE.objects.get(FMODE=fold)
        qty = request.POST.get('quantity')
        QTY = int(qty)
        small = request.POST.get('smellmode')
        #利用資料庫做計算
            #洗衣
        wmodes = WMODE.objects.get(WMODE=wash)
        w_price=wmodes.MONEY
        w_memission=wmodes.MEMISSIONS
        w_time=wmodes.TIME
        w_point=wmodes.POINTS
            #烘衣
        lmodes = LMODE.objects.get(LMODE=dry)
        l_price=lmodes.MONEY
        l_memission=lmodes.MEMISSIONS
        l_time=lmodes.TIME
        l_point=wmodes.POINTS
            #摺衣
        fmodes = FMODE.objects.get(FMODE=fold)
        f_price=fmodes.MONEY
        f_memission=fmodes.MEMISSIONS
        f_time=fmodes.TIME
        f_point=wmodes.POINTS
        #計算價錢
        total_price = w_price+l_price+f_price+(QTY*50)+(w_memission+l_memission+f_memission)*3
        #計算時間(現在時間+洗衣時間)
        total_time =math.ceil(w_time+l_time+f_time)
        start=datetime.datetime.now()
        out_date = (start + timedelta(minutes=total_time))
        out_date1= (out_date + timedelta(hours=2))
        out_date2= (out_date + timedelta(hours=5))
        out_date3= (out_date + timedelta(hours=8))
        out_date4= (out_date + timedelta(hours=11))
        out_date5= (out_date + timedelta(days=1))
        out_date6= (out_date + timedelta(days=2))

        o=save()
        #計算點數
        total_point=w_point+l_point+f_point+(QTY*20)
        CLIST.objects.create(ORDID=o,WMODE=WASH, LMODE=DRY,FMODE=FOLD,BAGNUM=QTY,PRICE=total_price,TIME=out_date,SMELL=small)
        #計算碳稅
        carbonn(o,w_memission,l_memission,f_memission,total_point,total_price,request)
        ords=CLIST.objects.latest('id')
    return render(request, "order.html", locals())

#將點數建到order資料表
def carbonn(o,w_memission,l_memission,f_memission,total_point,total_price,request):
    A=request.session['UserID']
    total_memissions=(w_memission+l_memission+f_memission)*3
    order.objects.create(ORDID=o,MEMID=A ,APPID='7',C_AMOUNT=total_memissions ,GPOINT=total_point, AMOUNT=total_price)

#API對接
    # requests.post('http://d2dc-59-124-158-45.jp.ngrok.io/api/myapp/',data={
    # "ORDID":o,
    # "MEMID" :A,
    # "APPID" :"7",
    # "C_AMOUNT":total_memissions,
    # "GPOINT" :total_point,
    # "AMOUNT" :total_price,
    # "CDATE" : timezone.now(),
    # })

    requests.post('https://5858-123-241-222-92.jp.ngrok.io/historyarticles/',data={
    "ordid":o,
    "memid" :A,
    "appname" :"7",
    "c_amount":total_memissions,
    "gpoint" :total_point,
    "amount" :total_price,
    "cdate" : timezone.now(),
    })


def save():
    # 自動產生訂單編號
    i = 1
    while True:
        ordid = f"{i:03d}"
        if not CLIST.objects.filter(ORDID=ordid).exists():
            ORDID = ordid
            break
        i += 1

    return ordid


def create_order(request):
    # 產生訂單編號: 檢查目前資料庫中最大的訂單編號，再加 1
    last_order = CLIST.objects.latest('ORDID')
    new_order_id = last_order.ORDID + 1

    # 建立新的 CLIST 資料
    new_order = CLIST.objects.create(
        ORDID=new_order_id,
        # 其他欄位
    )

    # 儲存資料
    new_order.save()

    return render(request, 'create_order.html', {'new_order_id': new_order_id})

def preference(request):
    return render(request, "preference.html")

def setpreference(request):
    return render(request, "setpreference.html")

def wash(request):
    sumPrice = CLIST.objects.all().aggregate(Sum('PRICE'))['PRICE__sum']
    context = {'sumPrice': sumPrice}
    return render(request, "wash.html", context)

def cash(request):
    return render(request, "cash.html")

def Delivery(request):
    return render(request, "Delivery.html",)

def GDPR(request):
    return render(request, "GDPR.html")

def sms(request):
    return render(request, "sms.html")

def login(request):
    return render(request, "login.html")
# Create your views here.

def lock_test(request):
    locks=lock.objects.get(LOCKID="1")
    return render(request, "lock.html", locals())

def Uber(request):
    ord=CLIST.objects.latest('id')
    ORD=ord.ORDID
    shops=shop.objects.get(id=1)
    SHOPS=shops.SHOPID
    time=order.objects.latest('id')
    if request.method == 'POST':
        phone = request.POST.get('phonenumber')
        add = request.POST.get('address')
        #small = request.POST.get('smallmode')
        delivery.objects.create(ORDID=ORD,SHOPID=SHOPS,PHONE=phone, ADDRESS=add)
        #clists = CLIST.objects.all()

        return render(request, "order_uber.html", locals())
    elif request.method == 'GET':
        return render(request, 'Uber.html', locals())


#from myapp.models import Invite

SACCngrok="https://10eb-1-34-54-152.jp.ngrok.io"
serverngrok="https://3f37-114-32-188-99.jp.ngrok.io"
from sa_final.models import LOGIN
import requests

#import json
def login2_view(request):
    sum=""
    rand=LOGIN.objects.create()
    url = SACCngrok+'/RESTapiApp/Line_1/?Rbackurl='+serverngrok+'/api2/?fk='+rand.FKcheck
    req=requests.get(url,headers = {'Authorization': 'Token 1b38ff1d38ef9e4c480cc4d39b9f818b83ebf854','ngrok-skip-browser-warning': '7414'})
    req_read = req.json()
    LOGIN.objects.filter(FKcheck = rand.FKcheck).update(Rstate=req_read["Rstate"])
    firstLogin="https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri="+SACCngrok+"/LineLoginApp/callback&state="+req_read["Rstate"]+"&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW?http://example.com/?ngrok-skip-browser-warning=7414"
    return render(request, 'login.html', locals())

def api2(request):
    if request.method == 'GET':
        fknum = request.GET.get('fk')
        nomatter=LOGIN.objects.filter(FKcheck = fknum)
        sum=''
        for i in nomatter:
            sum=i.Rstate
    print(sum)
    url = SACCngrok+'/RESTapiApp/Line_2/?Rstate='+sum
    req=requests.get(url,headers = {'Authorization': 'Token 1b38ff1d38ef9e4c480cc4d39b9f818b83ebf854','ngrok-skip-browser-warning': '7414'})
    print(req)
    req_read = req.json()
    print(req_read)
    userUID=req_read["RuserID"]
    access_code=req_read["Raccess_code"]
    print(req_read["Raccess_code"])

    return login_session(request,userUID, access_code)

def login_session(request,userUID, access_code):
    if USER.objects.filter(USERID=userUID):
        USER.objects.filter(USERID=userUID).update(ACCESSCODE=access_code)
    else:
        USER.objects.create(USERID=userUID, ACCESSCODE=access_code)
    UID = userUID
    if 'UserID' in request.session:
        try:
            del request.session['UserID']
        except:
            pass
    request.session['UserID'] = UID
    request.session.modified = True
    request.session.set_expiry(60*30) #存在30分鐘
    return HttpResponseRedirect("/")


#paypal
def PAYPAL(request):
    host = request.get_host()
    orderid = CLIST.objects.latest('ORDID')
    ordid=orderid.ORDID
    price=orderid.PRICE
    paypal_dict = {
        'business': settings.PAYPAL_REVEIVER_EMAIL,
        'amount': price,
        'item_name': "AI智慧喜訂單 訂單編號:"+ordid,
        'invoice': str(uuid.uuid4()),
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url':  f'http://{host}{reverse("paypal-reverse")}',
        'cancel_return':  f'http://{host}{reverse("paypal-cancel")}',
        'currency_code':"TWD",
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)

def paypal_ipn(request):
    messages.success(request,'!')
    return redirect('payment')

def paypal_reverse(request):
    messages.success(request,'支付成功!')
    return redirect('/Delivery')

def paypal_cancel(request):
    messages.success(request,'取消付款')
    return redirect('payment')

#訂單qrcode
def qrcode(request):
    return render(request, "qrcode.html")

#取件qrcode
def qrcode_take(request):
    return render(request, "qrcode_take.html")

#訂單成立
def established(request):
    return render(request, "qrcodeafter.html")

#外送資訊
def Uber_order(request):
    return render(request, "order_uber.html")