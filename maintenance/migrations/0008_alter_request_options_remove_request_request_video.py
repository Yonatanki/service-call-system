# Generated by Django 4.1.3 on 2022-12-13 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0007_alter_category_options_alter_location_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['request_number']},
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_video',
        ),
    ]
