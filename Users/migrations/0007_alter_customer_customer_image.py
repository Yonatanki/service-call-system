# Generated by Django 4.1.3 on 2022-12-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_remove_customer_customer_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_image',
            field=models.ImageField(blank=True, default='static/images/customers/user-default.png', null=True, upload_to='static/images/customers'),
        ),
    ]
