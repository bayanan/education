from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/log', auth_views.LogoutView.as_view(), name='logout'),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('', CourseListView.as_view(), name='course_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
