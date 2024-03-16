from django.contrib import admin
from django.urls import path, include
import environ

env = environ.Env()
env.read_env(env.str("ENV_PATH", ".env"))

urlpatterns = [
    path(env('ADMIN_SITE', default='admin/'), admin.site.urls),
    path('api/study/', include('study.urls'))
]
