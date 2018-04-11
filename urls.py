"""sample_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from myapp.blog import BlogListView ,BlogDetailView, BlogCommentCreateView
from myapp.login_blog_view import MyView
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^myapp/','myapp.views.hello',name = 'hello'),
    #url(r'^myapp2/','myapp.views.amit',name = 'hello_Amit'),
#urlpatterns = patterns('myapp.view',
    #url(r'^myapp3/','myapp.views2.login'),
    #url(r'^myapp4/','myapp.views2.delete'),
    #url(r'^myapp5/','myapp.views3.user_name'),
    #url(r'^myapp6/','myapp.view_new.soical'),
    #url(r'^myapp8/','myapp.view_new.delete'),
    #url(r'^myapp7/','myapp.view_new2.status'),
   # url(r'^myapp9/','myapp.views_form.soical'),
    #url(r'^myapp10/','myapp.view_form2.social_edit'),
    #url(r'^pub/',SoicalListView.as_view()),
    #url(r'^pub2/',SoicalEdit.as_view()),
    url(r'^login/',MyView.as_view()),
    url(r'^blog/',BlogListView.as_view()),
    url(r'^(blog_detail/)(?P<slug>[0-9a-z\-]+)/$',BlogDetailView.as_view(), name = 'blog_detail'),
    url(r'^blog_comment/$',BlogCommentCreateView.as_view(), name = 'blog_comment'),

    #url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    #url(r'^login/', 'login', name = 'login')
    #url(r'^appname/', "<app_name.views.<function_name>"),

)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

