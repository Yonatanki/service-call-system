# Generated by Django 4.1.3 on 2022-12-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_rename_customer_user_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
