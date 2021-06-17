from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.registration, name='registration'),
    path('calculator/', views.calculator, name='calculator'),
    path('login/', views.login, name='login'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('insertUpdateDelete/', views.insertUpdateDelete, name='insertUpdateDelete'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('updateDetails/', views.updateDetails, name ='updateDetails'),
    path('delete/', views.delete, name='delete'),
    path('posts/', views.posts, name='posts'),
    path('postUpload/', views.postUpload, name='postUpload'),
    path('userDetails/', views.userDetails, name='userDetails'),
    path('logout', views.logout, name='logout'),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

