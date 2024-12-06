from django.urls import path
from django.contrib import admin

from memes.views.mem import (
    MemListView, MemRetrieveView, MemDestroyView,
    MemCreateView, MemUpdateView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mems/', MemListView.as_view(), name='mem_list'),
    path('mems/<int:pk>/', MemRetrieveView.as_view(), name='mem_detail'),
    path('mems/update/<int:pk>/', MemUpdateView.as_view(), name='mem_update'),
    path('mems/create/', MemCreateView.as_view(), name='mem_create'),
    path('mems/delete/<int:pk>/', MemDestroyView.as_view(), name='mem_delete'),
]


