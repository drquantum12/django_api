from pyexpat import model
from rest_framework import serializers
from .models import blog_content

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog_content
        fields = ['id','title','content','author','pub_date','last_updated','img_1','img_2']