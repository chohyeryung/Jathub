from django.urls import path

from jat import views

app_name = 'jat'

urlpatterns = [
    path('', views.RepositoryListView.as_view(), name='repository_list'),    #name은 맘대로 지정하는 것임
    path('repository/<int:pk>/', views.RepositoryDetailView.as_view(), name='repository_detail'),
    path('repository/<int:repository_pk>/introduction/<int:pk>/', views.IntroductionDetailView.as_view(), name='introduction_detail'),
    path('repository/add/', views.RepositoryCreateView.as_view(), name='repository_add'),
    path('repository/<int:pk>/modify/', views.RepositoryUpdateView.as_view(), name='repository_modify'),
    path('repository/<int:pk>/delete/', views.RepositoryDeleteView.as_view(), name='repository_delete'),
]