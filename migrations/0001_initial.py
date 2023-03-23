# Generated by Django 4.1.4 on 2023-01-01 09:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('MEMID', models.CharField(max_length=20, verbose_name='使用者編號')),
                ('APPID', models.DateField(max_length=20, verbose_name='app編號')),
                ('C_AMOUNT', models.EmailField(max_length=20, verbose_name='花費的碳稅')),
                ('GPOINT', models.CharField(max_length=20, verbose_name='獲得的點數')),
                ('AMOUNT', models.CharField(max_length=20, verbose_name='消費總金額')),
                ('CDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='成立時間')),
            ],
        ),
    ]