# Generated by Django 3.1.6 on 2021-02-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintsinfo',
            name='admin_message',
            field=models.CharField(default='Your complaint is under review.We will get back to you soon.', max_length=250),
        ),
    ]
