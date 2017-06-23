from django.conf.urls import url
from . import views

urlpatterns=[
  url('^$', views.home),
  url('^writings/', views.writings),
  url('^home/', views.home),
  url('^about/', views.about)
]
