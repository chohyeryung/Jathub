from django.urls import path

from jat import views

app_name = 'jat'

urlpatterns = [
    path('', views.RepositoryListView.as_view(), name='repository_list'),    #name은 맘대로 지정하는 것임
    path('repository/<int:pk>/', views.RepositoryDetailView.as_view(), name='repository_detail'),
]