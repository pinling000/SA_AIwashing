from django.contrib import admin

# Register your models here.
from sa_final.models import order
from sa_final.models import WMODE
from sa_final.models import LMODE
from sa_final.models import FMODE
from sa_final.models import CLIST
from sa_final.models import delivery
from sa_final.models import shop
from sa_final.models import bag
from sa_final.models import lock
from sa_final.models import LOGIN
from sa_final.models import solve
from sa_final.models import USER

class CLISTadmin(admin.ModelAdmin):
    list_display=('id','ORDID','WMODE','LMODE','FMODE','SMELL','BAGNUM','TIME','PRICE',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(CLIST, CLISTadmin)

class WMODEadmin(admin.ModelAdmin):
    list_display=('id','WMODE','MONEY','POINTS','MEMISSIONS','TIME',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(WMODE, WMODEadmin)

class LMODEadmin(admin.ModelAdmin):
    list_display=('id','LMODE','MONEY','POINTS','MEMISSIONS','TIME',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(LMODE, LMODEadmin)

class FMODEadmin(admin.ModelAdmin):
    list_display=('id','FMODE','MONEY','POINTS','MEMISSIONS','TIME',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(FMODE, FMODEadmin)

class DELIVERYadmin(admin.ModelAdmin):
    list_display=('id','ORDID','SHOPID','PHONE','ADDRESS','GDATE',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(delivery, DELIVERYadmin)

class ORDERadmin(admin.ModelAdmin):
    list_display=('id','ORDID','MEMID','APPID','C_AMOUNT','GPOINT','AMOUNT','CDATE')
    list_filter=('id',)
    ordering=('id',)
admin.site.register(order, ORDERadmin)

admin.site.register(shop)
admin.site.register(bag)
admin.site.register(lock)


class LOGINAdmin(admin.ModelAdmin):
    list_display=('FKcheck','Rstate','Raccesscode',)
    ordering=('FKcheck',)

admin.site.register(LOGIN, LOGINAdmin)

admin.site.register(USER)

class solveadmin(admin.ModelAdmin):
    list_display=('id','QTYPE','QTEXT',)
    list_filter=('id',)
    ordering=('id',)
admin.site.register(solve, solveadmin)
