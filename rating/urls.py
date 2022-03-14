from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('profile', views.profile, name="profile"),
    path('project/<project>', views.project, name="project"),
    path('add-project/', views.add_project, name="add-project"),
    path('search/', views.search_results, name="search-results"),
    path('add-rating/<project>', views.add_rating, name="add-rating"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)