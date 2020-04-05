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
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strtftime('%b %e %Y')
