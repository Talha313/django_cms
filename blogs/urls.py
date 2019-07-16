from django.conf.urls import url
from django.conf.urls import include, url


from blogs import  views


app_name = "blogs"
urlpatterns = [
    url(r'^blogs', views.BlogView.as_view(), name='blogs'),

    url(r'^blog_detail/(?P<slug>[-\w\d]+)/$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^blog/(?P<slug>[-\w\d]+)/comment$', views.BlogCommentView.as_view(), name='blog-comment'),

    # url(r'^blog/(?P<slug>[-\w\d]+)/comment$', views.BlogCommentView.as_view(), name='blog-comment'),
    # url(r'^blog/<slug:slug>/comment', views.BlogCommentView.as_view(), name='blog-comment'),

    # url(r'^blog_detail/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    # url(r'^blog/<slug:slug>/comment/$', views.BlogCommentView.as_view(), name='blog-comment'),
]