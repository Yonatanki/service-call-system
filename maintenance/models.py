from django.db import models
from django.core.validators import FileExtensionValidator
from phone_field import PhoneField
from Users.models import customer
# from Users.utils import *
import uuid


# Create your models here.


class location(models.Model):
    __tablename__ = "Location"
    location_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                   primary_key=True, editable=False)
    location_city = models.CharField(max_length=200, blank=True, null=True)
    location_building = models.CharField(max_length=200, blank=True, null=True)
    location_floor = models.CharField(max_length=200, blank=True, null=True)
    location_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.location_city} - {self.location_building}'

    class Meta:
        ordering = ['location_city']


class department(models.Model):
    __tablename__ = "Department"  # in admin panel
    department_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                     primary_key=True, editable=False)
    department_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Department Name: {self.department_name} Department ID:  {str(self.department_id)}'


class employee(models.Model):
    __tablename__ = "Employee"
    employee_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                   primary_key=True, editable=False)
    employee_user_name = models.ForeignKey(customer, blank=True, null=True, on_delete=models.CASCADE)
    employee_department_id = models.ForeignKey('department', blank=True, null=True, on_delete=models.CASCADE)
    employee_privileges = models.ManyToManyField('privileges', blank=True)
    # employee_privileges = models.ManyToOneRel('employee_privileges', 'privileges', 'employee_privileges')
    employee_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee_user_name}'

    class Meta:
        ordering = ['employee_id', '-employee_created']


class privileges(models.Model):
    __tablename__ = "Privileges"
    privileges_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                     primary_key=True, editable=False)
    privileges_name = models.CharField(max_length=200, unique=True)
    privileges_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.privileges_name


class category(models.Model):
    __tablename__ = "Category"
    category_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                   primary_key=True, editable=False)
    category_name = models.CharField(max_length=200)
    category_department_id = models.ForeignKey('department', blank=True, null=True, on_delete=models.CASCADE)
    category_created = models.DateTimeField(auto_now_add=True)

    # to be able to see category name in admin panel.
    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['category_name']


class sub_category(models.Model):
    __tablename__ = "Sub Category"
    sub_category_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                       primary_key=True, editable=False)
    sub_category_category_id = models.ForeignKey('category', blank=True, null=True, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=200, blank=True, null=True)
    sub_category_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_category_name

    class Meta:
        ordering = ['sub_category_name']


class call_request(models.Model):
    __tablename__ = "Request"
    request_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    request_number = models.AutoField(primary_key=True)
    request_customer_id = models.ForeignKey(customer, blank=True, null=True, on_delete=models.SET_NULL)
    request_category_id = models.ForeignKey('category', blank=True, null=True, on_delete=models.SET_NULL)
    request_sub_category_id = models.ForeignKey('sub_category', blank=True, null=True, on_delete=models.SET_NULL)
    request_location_id = models.ForeignKey('location', blank=True, null=True, on_delete=models.SET_NULL)
    request_employee_id = models.ManyToManyField('employee', blank=True, null=True)
    request_description = models.TextField(null=True, blank=True)
    request_img = models.ImageField(upload_to='requests_images', default="/user.png", blank=True, null=True)
    request_video = models.FileField(upload_to='requests_videos', blank=True, null=True,
                                     validators=[FileExtensionValidator(
                                         allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    # request_message = models.ForeignKey('message', on_delete=models.CASCADE, blank=True, null=True)
    request_status = models.ForeignKey('status', blank=True, null=True, on_delete=models.CASCADE)
    # request_message = models.TextField(max_length=255, null=True, blank=True)
    request_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.request_number)} :     {self.request_category_id}:    {self.request_sub_category_id}'

    class Meta:
        ordering = ['request_number']


class status(models.Model):
    __tablename__ = "Status"
    status_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                 primary_key=True, editable=False)
    status_state = models.CharField(max_length=200, blank=True, null=True)
    status_date_changed_state = models.DateField(auto_now=True)
    status_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status_state}'

    class Meta:
        ordering = ['status_state']


class status_request(models.Model):
    __tablename__ = "Status Request"
    status_request_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                         primary_key=True, editable=False)
    status_request_status = models.ForeignKey('status', blank=True, null=True, on_delete=models.CASCADE)
    status_request_description = models.TextField(null=True, blank=True)
    status_request_employee_id = models.ForeignKey('employee', blank=True, null=True, on_delete=models.CASCADE)
    status_request_created = models.DateTimeField(auto_now_add=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.request_number = None

    def __str__(self):
        return f'{self.status_request_status}'


class message(models.Model):
    __tablename__ = "Message"
    message_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                  primary_key=True, editable=False)
    # message_request_id = models.ForeignKey(call_request, on_delete=models.SET_NULL, null=True, blank=True)
    message_request_id = models.ForeignKey(call_request, on_delete=models.SET_NULL, null=True, blank=True)
    sender = models.ForeignKey(
        customer, on_delete=models.SET_NULL, null=True, blank=True)
    # recipient = models.ForeignKey(
    #     customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}'

    class Meta:
        ordering = ['is_read', '-created']

# class image(models.Model):
#     __tablename__ = "Images"
#     image_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     image_service_request_number = models.ForeignKey(call_request, on_delete=models.SET_NULL, null=True, blank=True)
#     request_img = models.ImageField(upload_to=wrapper, default="/user.png", blank=True, null=True)
#
#     def __str__(self):
#         return self.image_service_request_number
#
#     class Meta:
#         ordering = ['service_request_id']
