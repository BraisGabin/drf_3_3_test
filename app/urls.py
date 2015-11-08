from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    url(r'^media/$', views.UploadMedia.as_view(), name='upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
