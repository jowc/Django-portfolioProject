from django.db import models

# Create your models here.
class job(models.Model):
    title= models.CharField(max_length= 40 , null= True)
    image= models.ImageField(upload_to="images/")
    summary= models.CharField(max_length= 200)

    def __str__(self):
        return self.title