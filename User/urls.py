from django.urls import path
from User import views

urlpatterns = [
    path('user/', views.user_list),
    path('user/<int:pk>', views.user_detail),
]
