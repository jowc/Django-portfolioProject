from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    title= models.CharField(max_length= 200)
    date= models.DateTimeField(null=True)
    image= models.ImageField(upload_to="images/")
    content= models.TextField()
    #userComment= models.ForeignKey(User, on_delete= models.CASCADE)

    def summary(self):
        return self.content[:100]

    def __str__(self):
        return self.title
    
    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y')
    

