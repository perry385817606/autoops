# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20170830_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_center_list', models.CharField(max_length=128, null=True, verbose_name='数据中心')),
            ],
            options={
                'verbose_name': '数据中心',
                'verbose_name_plural': '数据中心',
                'db_table': 'data_centers',
            },
        ),
        migrations.AlterField(
            model_name='asset',
            name='data_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.data_centers', verbose_name='产品线'),
        ),
        migrations.AlterModelTable(
            name='product_lines',
            table='product_lines',
        ),
    ]