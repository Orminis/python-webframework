from django.urls import path

from fmw.cbv_01.views import cbv_index

urlpatterns = (
    path('', cbv_index, name='cbv index'),
)