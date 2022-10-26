from enroll import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Signup/', views.Sign_up),
    path('login/', views.Log_in),
]
