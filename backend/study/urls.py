from django.urls import path
from .views import StudyListCreate

app_name = 'api/study'


urlpatterns = [
    path('', StudyListCreate.as_view()),
]