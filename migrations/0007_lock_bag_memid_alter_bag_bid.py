# Generated by Django 4.1.4 on 2023-01-03 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sa_final', '0006_bag'),
    ]

    operations = [
        migrations.CreateModel(
            name='lock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCKID', models.CharField(max_length=20, verbose_name='鎖櫃編號')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('INDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='放入時間')),
                ('OUTDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='取出時間')),
            ],
        ),
        migrations.AddField(
            model_name='bag',
            name='MEMID',
            field=models.CharField(default=0, max_length=20, verbose_name='使用者編號'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='BID',
            field=models.CharField(max_length=20, verbose_name='洗衣袋編號'),
        ),
    ]