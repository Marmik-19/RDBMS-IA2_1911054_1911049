# Generated by Django 3.1.6 on 2021-02-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingPerson', '0004_missingpersoninfo_ack_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingpersoninfo',
            name='admin_status',
            field=models.CharField(choices=[('under scrutiny', 'Under Scrutiny'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='under scrutiny', max_length=50),
        ),
    ]
