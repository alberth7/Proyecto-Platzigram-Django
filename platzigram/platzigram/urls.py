from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hora/',local_views.helloWorld, name='hello_world' ),
    path('blackpink/', local_views.blackpink, name='blackpink'),
    path('hi/', local_views.hi, name='blackpink' ),
    path('sorted/', local_views.sorted, name='sort'),
    path('say_hi/<str:name>/<int:age>', local_views.say_hi),

    path('posts/', posts_views.list_post, name='feed'),

    path('users/login', users_views.login_view, name='login' ),
    path('users/logout', users_views.logout_view, name='logout'),

    path('users/signup/', users_views.signup, name='signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
