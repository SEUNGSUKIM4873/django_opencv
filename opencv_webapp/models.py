from django.db import models


# Create your models here.
class ImageUploadModel(models.Model):

    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to = 'images/%Y/%m/%d')
    #경로명을 다큐먼트에 저장
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
