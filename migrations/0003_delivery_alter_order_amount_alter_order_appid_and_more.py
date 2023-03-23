# Generated by Django 4.1.4 on 2023-01-02 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sa_final', '0002_alter_order_appid_alter_order_c_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('SHOPID', models.CharField(max_length=20, verbose_name='店鋪編號')),
                ('PHONE', models.CharField(max_length=10, verbose_name='使用者電話')),
                ('ADDRESS', models.CharField(max_length=40, verbose_name='使用者地址')),
                ('GDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='取件時間')),
                ('S_CODE', models.CharField(max_length=20, verbose_name='取件條碼')),
                ('G_CODE', models.CharField(max_length=20, verbose_name='送件條碼')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='AMOUNT',
            field=models.IntegerField(max_length=20, verbose_name='消費總金額'),
        ),
        migrations.AlterField(
            model_name='order',
            name='APPID',
            field=models.IntegerField(max_length=10, verbose_name='app編號'),
        ),
        migrations.AlterField(
            model_name='order',
            name='C_AMOUNT',
            field=models.IntegerField(max_length=20, verbose_name='花費的碳稅'),
        ),
        migrations.AlterField(
            model_name='order',
            name='GPOINT',
            field=models.IntegerField(max_length=20, verbose_name='獲得的點數'),
        ),
    ]