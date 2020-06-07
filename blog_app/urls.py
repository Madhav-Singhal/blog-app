from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog_app'

urlpatterns = [
   
    path('', views.list, name = 'list'),
    path('create/', views.create, name = 'create'),
    path('create/<int:id>/login/', views.login, name = 'login'),
    path('create/login/', views.login, name = 'login'),
    path('create/register/', views.register, name = 'register'),
    path('create/<int:id>/register/', views.register, name = 'register'),

    path('create/logout/', views.logout, name = 'logout'),
    path('create/user_list/logout/', views.logout, name = 'logout'),
    path('create/user_list/', views.user_list, name = 'user_list'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('create/user_list/edit/<int:id>', views.edit, name = 'edit'),
    path('create/user_list/delete/<int:id>', views.delete, name = 'delete'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
