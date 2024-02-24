from django.urls import path
from .views import StudyListCreate, CategoryList

app_name = 'api/study'

urlpatterns = [
    path('category', CategoryList.as_view()),
    path('list', StudyListCreate.as_view()),
]
