from django.db import models


# Create your models here.
# create a blog model
# title
# pub_date
# body
# image
# add the blog app to settings
# create a migration
# migrate
# add to the admin

class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateField()
    body = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/')
