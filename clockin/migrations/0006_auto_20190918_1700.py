# Generated by Django 2.2.5 on 2019-09-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0005_auto_20190918_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaulttype',
            name='name',
            field=models.CharField(blank=True, max_length=40, unique=True, verbose_name='默认类型名称'),
        ),
    ]