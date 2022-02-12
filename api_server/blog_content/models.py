from django.db import models

# Create your models here.
class blog_content(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=10000)
    author = models.CharField(max_length=50, null=False)
    pub_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    img_1 = models.ImageField(upload_to='covers/', blank=True)
    img_2 = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title
