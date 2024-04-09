from django.urls import path
from .import views

app_name='blog_app'
urlpatterns=[
    path('detail/<int:pk>', views.post_detail, name="article_detail"),
    path('list', views.ArticleList.as_view(), name='article_list'),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.search_article, name="search_articles"),
    path('countact', views.countacts_us, name='countact_us')
   
]  
#     path('contact', views.contactus, name="contact_us"),
# ]

    
