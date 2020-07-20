from django.db import models
from django.conf import settings
# Create your models here.


class Document(models.Model):
	upload_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="uploaded_documents",on_delete=models.CASCADE)
	datetimestamp = models.DateTimeField(auto_now_add=True)
	document  =  models.FileField(upload_to='uploads/')

class AnalyticsDocument(models.Model):
	title =  models.CharField(max_length=42)
	document =  models.ForeignKey(Document,on_delete=models.CASCADE)
