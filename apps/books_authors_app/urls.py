from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.display_author),
    url(r'^add_book$', views.add_book),
    url(r'^add_author$', views.add_author),
    url(r'^book_dets/(?P<book_id>\d+)$', views.display_book_dets),
    url(r'^author_to_book$', views.add_author_to_book),
    url(r'^author_dets/(?P<auth_id>\d+)$', views.display_author_dets),
    url(r'^book_to_author$', views.add_book_to_author),
]