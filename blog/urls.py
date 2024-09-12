from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/view', BlogDetailView.as_view(), name='blog_view'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
]
