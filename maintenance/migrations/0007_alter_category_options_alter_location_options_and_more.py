# Generated by Django 4.1.3 on 2022-12-13 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0006_alter_request_request_category_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['location_city']},
        ),
        migrations.AlterModelOptions(
            name='sub_category',
            options={'ordering': ['sub_category_name']},
        ),
        migrations.AddField(
            model_name='request',
            name='request_number',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='request_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
