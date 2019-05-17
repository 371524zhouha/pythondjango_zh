from . import views
from django.urls import path

app_name='image'

urlpatterns=[
	path('list-images/', views.list_images,name="list_images"),
	path('upload-image/', views.upload_image,name="upload_image"),
	path('del_image/', views.del_image,name="del_image"),
]