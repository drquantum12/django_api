from django.http import HttpResponse
from django.shortcuts import render

from .serializers import BlogSerializer
from .models import blog_content
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def blog(request):
    blogs = blog_content.objects.all()
    for blog in blogs:
       output = blog.content
    
    return HttpResponse(output)

class BlogViewSet(viewsets.ModelViewSet):
   serializer_class = BlogSerializer
   queryset = blog_content.objects.all()
   # authentication_classes = (TokenAuthentication,)            # using these techniques, restrictions can be applied for a particular viewset
   # permission_classes = (IsAuthenticated,)
