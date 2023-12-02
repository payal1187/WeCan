from django.db import models


class ContactModel(models.Model):
    email = models.EmailField(max_length=200, unique=True,blank=False)
    concern = models.TextField()
   
    
    def __str__(self):
        return  f'{self.email}'
    