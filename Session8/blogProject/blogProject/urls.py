from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", views.list, name="list"),
    path("new", views.new, name="new"),
    path("detail/<str:category_number>", views.detail, name="detail"),
]