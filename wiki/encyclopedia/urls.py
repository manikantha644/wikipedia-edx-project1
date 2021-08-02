from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search,name="search"),
    path("wiki/<str:entry>", views.wiki, name="wiki"),
    path("random",views.random,name="random"),
    path("newpage",views.newpage,name="newpage"),
    path("savenewpage",views.savenewpage,name="savenewpage"),
    path("edit/<str:entryedit>",views.edit,name="edit"),
    path("saveedit",views.saveedit,name = 'saveedit')

]
