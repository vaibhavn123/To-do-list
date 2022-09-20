from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inserttodolistview/',inserttodolistview),
    path('deletetodolistbyid/<int:pk>',deletetodolistview),
    path('searchtodolist/',searchtodolistview),
    path('updatetodolistbyid/<int:pk>',updatetodolistview),
    path('searchtodolistbyid/<int:pk>',searchtodolistbyidview),
]