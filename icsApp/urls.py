from django.conf.urls import url
from . import views

app_name = "icsApp"

urlpatterns = [
    url(r'^inventory/$', views.inventory_list, name='inventory_list'),
    url(r'^test_search_results/$', views.search, name='search'), # <- url for searchresults
    url(r'^inventory/(?P<pk>\d+)/quantity/increase/$', views.quantity_increase, name='quantity_increase'),
    url(r'^inventory/(?P<pk>\d+)/quantity/decrease/$', views.quantity_decrease, name='quantity_decrease'),
    url(r'^inventory/(?P<pk>\d+)/edit/$', views.inventory_edit, name='inventory_edit'),
    url(r'^inventory/(?P<pk>\d+)/delete/$', views.inventory_delete, name='inventory_delete'),
    url(r'^inventory/create/$', views.inventory_new, name='inventory_new'),
    url(r'^inventory/import/$', views.import_data, name='import_data'),
    url(r'^inventory/export/$', views.export_data, name='export_data'),
    url(r'^inventory/sortAsc-itemN$', views.ascending_item, name='ascending_item'),
    url(r'^inventory/sortDsc-itemN$', views.descending_item, name='descending_item'),
    url(r'^inventory/sortAsc-ctgry$', views.ascending_category, name='ascending_category'),
    url(r'^inventory/sortDesc-ctgry$', views.descending_category, name='descending_category'),
    url(r'^inventory/sortAsc-vndr$', views.ascending_vendor, name='ascending_vendor'),
    url(r'^inventory/sortDesc-vndr$', views.descending_vendor, name='descending_vendor'),
]
