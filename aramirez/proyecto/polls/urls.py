from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view() , name='index'),

    path('<int:pk>/', views.DetailView.as_view() , name='detail'),

    path('<int:pk>/results/', views.ResultsView.as_view() , name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('classificacion/', views.ClassificationView.as_view(), name='classification'),

    path('classification/<int:pk>/', views.ClassificationViewss.as_view(), name='classificationss'),

    
]

