from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:ag_name>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('offer/<int:of_id>/', views.offer, name='offer'),
    #path('requestt/<int:of_id>',views.requestt, name='requestt')
    
]