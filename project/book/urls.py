from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('add/', views.AddPhoneFormView.as_view(), name="add"),
    path('delete/<int:pk>', views.DeletePhoneView.as_view(), name="delete")
]
