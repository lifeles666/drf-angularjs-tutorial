from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CategoryList, CategoryDetail, CategoryListView, CategoryDetailView

urlpatterns = patterns('news.views',
    url(
        regex = r'^$', 
        view = CategoryList.as_view(),
        name = 'news-category-list'),
    url(
        regex = r'^/(?P<slug>[a-zA-Z0-9-]+)$', 
        view = CategoryDetail.as_view(),
        name = 'news-category-detail'),
                       
    url(r'^/templates/category-list.html', 
        view = CategoryListView.as_view()
        ),
    url(r'^/templates/category-detail.html', 
        view = CategoryDetailView.as_view()
        ),                   
                       
)

urlpatterns = format_suffix_patterns(urlpatterns)