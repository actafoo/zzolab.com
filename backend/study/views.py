from rest_framework.generics import ListCreateAPIView, ListAPIView

from study.models import Study, Category
from study.serializers import StudySerializer, CategorySerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StudyListCreate(ListCreateAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
