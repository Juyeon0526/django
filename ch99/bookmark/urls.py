from django.urls import path
from bookmark import views

app_name = 'bookmark'
urlpatterns = [

    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    path('add/', views.BookmarkCreateView.as_view(), name="add"),
    path('change/', views.BookmarkChangeLV.as_view(), name="change"),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete"),

    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # Example: /bookmark/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]