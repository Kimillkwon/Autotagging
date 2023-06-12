from django.urls import path
from .views import *

from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name='main'

urlpatterns=[
    path('',views.index ,name="index"),
    path('blog/',blog),
    path("upload/", views.uploadFile, name = "uploadFile"),
    path('test/',test),
    path('result/',result)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
