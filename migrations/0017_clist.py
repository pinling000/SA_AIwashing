# Generated by Django 4.1.5 on 2023-01-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa_final', '0016_delete_clist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('WMODE', models.CharField(max_length=20, verbose_name='洗滌模式')),
                ('LMODE', models.CharField(max_length=20, verbose_name='乾燥模式')),
                ('FMODE', models.CharField(max_length=20, verbose_name='摺衣模式')),
                ('BAGNUM', models.IntegerField(default=1, verbose_name='袋數')),
                ('TIME', models.IntegerField(blank=True, null=True, verbose_name='總時長')),
                ('PRICE', models.IntegerField(blank=True, null=True, verbose_name='總金額')),
            ],
        ),
    ]
