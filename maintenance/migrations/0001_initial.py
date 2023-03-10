# Generated by Django 4.1.3 on 2022-12-04 18:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category_name', models.CharField(max_length=200)),
                ('category_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('department_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('department_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employee_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employee_name', models.CharField(blank=True, max_length=200, null=True)),
                ('employee_username', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('employee_created', models.DateTimeField(auto_now_add=True)),
                ('employee_email', models.EmailField(blank=True, max_length=500, null=True)),
                ('employee_phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, null=True)),
                ('employee_department_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.department')),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('location_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('location_city', models.CharField(blank=True, max_length=200, null=True)),
                ('location_building', models.CharField(blank=True, max_length=200, null=True)),
                ('location_floor', models.CharField(blank=True, max_length=200, null=True)),
                ('location_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('message_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='Users.customer')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.customer')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
        migrations.CreateModel(
            name='privileges',
            fields=[
                ('privileges_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('privileges_name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('privileges_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='request',
            fields=[
                ('request_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('request_description', models.TextField(blank=True, null=True)),
                ('request_img', models.ImageField(blank=True, null=True, upload_to='images_uploaded')),
                ('request_video', models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('request_created', models.DateTimeField(auto_now_add=True)),
                ('request_customer_id', models.ManyToManyField(blank=True, to='Users.customer')),
                ('request_employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.employee')),
                ('request_location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.location')),
                ('request_message_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.message')),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('status_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status_state', models.CharField(blank=True, max_length=200, null=True)),
                ('status_date_changed_state', models.DateField(auto_now=True)),
                ('status_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('sub_category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sub_category_name', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_category_created', models.DateTimeField(auto_now_add=True)),
                ('sub_category_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.category')),
            ],
        ),
        migrations.CreateModel(
            name='status_request',
            fields=[
                ('status_request_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('status_request_description', models.TextField(blank=True, null=True)),
                ('status_request_created', models.DateTimeField(auto_now_add=True)),
                ('status_request_employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.employee')),
                ('status_request_request_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.request')),
                ('status_request_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.status')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='request_sub_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.sub_category'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_privileges',
            field=models.ManyToManyField(blank=True, to='maintenance.privileges'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_department_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maintenance.department'),
        ),
    ]
