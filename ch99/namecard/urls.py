from django.urls import path
from namecard import views

app_name = 'namecard'
urlpatterns = [
    path('', views.NamecardLV.as_view(), name='index'),
    path('<int:pk>/', views.NamecardDV.as_view(), name='detail'),

    path('add/', views.NamecardCreateView.as_view(), name="add"),
    path('change/', views.NamecardChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.NamecardUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.NamecardDeleteView.as_view(), name="delete"),
]