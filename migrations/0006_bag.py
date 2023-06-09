# Generated by Django 4.1.4 on 2023-01-03 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sa_final', '0005_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BID', models.CharField(max_length=20, verbose_name='店鋪編號')),
                ('GDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='租借時間')),
                ('RDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='歸還時間')),
            ],
        ),
    ]
