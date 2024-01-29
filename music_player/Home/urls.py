
from django.urls import path,include
from .views import Index,Upload,UploadAlbums,download_file,Update,Api,delete,lay,Add

urlpatterns = [
    path('',Index.as_view(),name="home"),
    path('upload',Upload.as_view(),name="upload"),
    path('play/<int:pk>/',lay,name="play"),
    path('add/',Add,name="add"),
    
    path('artist/(?P<slug>[-a-zA-Z0-9_]+)/\\Z/',UploadAlbums.as_view(),name="artist"),
    path('download/<int:pk>/',download_file,name="download"),
    path('delete/<int:pk>/',delete,name="delete"),

    path('api',Api.as_view()),
    path('api/update/<int:pk>',Update.as_view())
    
]