from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    num=models.CharField(max_length=200)

class Office(models.Model):
    office_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()
    province = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=1)
    size = models.CharField(max_length=100)
    status_flag = models.CharField(max_length=1)
    update_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Result(models.Model):
    result_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    book_number = models.CharField(max_length=100)
    status_flag = models.CharField(max_length=1)
    result_flag = models.CharField(max_length=1)
    descriptions = models.TextField()
    create_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_by = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class ResultDetails(models.Model):
    resultdetails_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)
    specifications = models.CharField(max_length=100)
    result_flag = models.CharField(max_length=1)
    remark = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resultdetails_id)

class Files(models.Model):
    files_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    path = models.FileField()
    
    def __str__(self):
        return str(self.files_id)



#---------- ครุภัณฑ์ ----------
class Location(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.location_id)

class Assettype(models.Model):
    assettype_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    status_flag = models.CharField(max_length=1)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.assettype_id)

class Asset(models.Model):
    asset_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    assettype_id = models.ForeignKey(Assettype, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    expire_date = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.ForeignKey(User, default=None, on_delete=models.CASCADE)