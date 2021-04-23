# Generated by Django 3.1.6 on 2021-02-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0007_verificationinfo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationinfo',
            name='admin_status',
            field=models.CharField(choices=[('under scrutiny', 'Under Scrutiny'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='under scrutiny', max_length=30),
        ),
    ]
