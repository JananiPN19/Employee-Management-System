# Generated by Django 3.1.2 on 2020-10-18 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20201012_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='basic_pay',
            field=models.DecimalField(decimal_places=3, default=1000.0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='net_salary',
            field=models.DecimalField(decimal_places=3, default=20000.0, max_digits=20),
            preserve_default=False,
        ),
    ]
