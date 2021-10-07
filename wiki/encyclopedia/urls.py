from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.displayEntry, name="entry"),
    path("search/",views.searchResult, name="searchResult"),
    path("createNewPage", views.createNewPage, name="createNewPage"),
    path("addTitle", views.add, name="addTitle" ),
    path("edit", views.edit, name="edit"),
    path("postEdit", views.postEdit, name="postEdit"),
    path("getRandom",views.getRandom, name="random"),
]
