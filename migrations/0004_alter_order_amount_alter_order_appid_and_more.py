# Generated by Django 4.1.4 on 2023-01-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa_final', '0003_delivery_alter_order_amount_alter_order_appid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='AMOUNT',
            field=models.IntegerField(verbose_name='消費總金額'),
        ),
        migrations.AlterField(
            model_name='order',
            name='APPID',
            field=models.IntegerField(verbose_name='app編號'),
        ),
        migrations.AlterField(
            model_name='order',
            name='C_AMOUNT',
            field=models.IntegerField(verbose_name='花費的碳稅'),
        ),
        migrations.AlterField(
            model_name='order',
            name='GPOINT',
            field=models.IntegerField(verbose_name='獲得的點數'),
        ),
    ]