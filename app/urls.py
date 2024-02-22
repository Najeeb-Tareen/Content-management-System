from django.urls import path
from .import views

urlpatterns = [
 path('person/', views.person_data, name='person'),
 path('category/', views.Categories_data, name='Categories_data'),
path('add_article/', views.add_article, name='article'),



























    
    #
    # path('add_article/', views.add_article, name='article'),
    # 
    # path('home/', views.home, name='home'),
    # path('detailart/<title>/', views.detail_article, name='detail_article'),
]
