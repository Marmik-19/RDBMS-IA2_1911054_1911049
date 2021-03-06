# Generated by Django 3.1.6 on 2021-02-19 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0005_auto_20210219_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalsinfo',
            name='address',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='criminalsinfo',
            name='crime',
            field=models.CharField(choices=[('cyber', 'Cyber'), ('extortion', 'Extortion'), ('chain snatching', 'Chain Snatching'), ('dacotiy', 'Dacoity'), ('theft', 'Theft'), ('others', 'Others')], default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='criminalsinfo',
            name='current_status',
            field=models.CharField(choices=[('in prison', 'In Prison'), ('on bail', 'On Bail'), ('released', 'Released')], default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='criminalsinfo',
            name='desc',
            field=models.CharField(default='null', max_length=250),
        ),
        migrations.AlterField(
            model_name='criminalsinfo',
            name='pincode',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='criminalsinfo',
            name='prison_sentence',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
