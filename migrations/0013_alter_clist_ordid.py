# Generated by Django 4.1.5 on 2023-01-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sa_final', '0012_alter_clist_ordid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clist',
            name='ORDID',
            field=models.CharField(default=1, max_length=20, verbose_name='訂單編號'),
        ),
    ]
