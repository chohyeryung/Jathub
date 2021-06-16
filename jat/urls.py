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
    # path('repository/<int:repository_pk>/introduction/add/', views.IntroductionCreateView.as_view(), name='introduction_add'),
    path('repository/<int:repository_pk>/introduction/add/', views.add_introduction, name='introduction_add'),
    path('repository/<int:repository_pk>/introduction/<int:pk>/modify/', views.IntroductionUpdateView.as_view(), name='introduction_update'),
    path('repository/<int:repository_pk>/introduction/<int:pk>/delete/', views.IntroductionDeleteView.as_view(), name='introduction_delete'),
    path('repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/add/', views.CommentCreateView.as_view(), name='comment_add'),
    path('repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/<int:pk>/modify/', views.CommentUpdateView.as_view(),name='comment_update'),
    path('repository/<int:repository_pk>/introduction/<int:introduction_pk>/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(),name='comment_delete'),
]