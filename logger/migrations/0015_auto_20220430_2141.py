# Generated by Django 3.1.4 on 2022-04-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0014_auto_20200713_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='actual_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='activity',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
