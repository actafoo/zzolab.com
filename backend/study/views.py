from rest_framework.generics import ListCreateAPIView

from study.models import Study
from study.serializers import StudySerializer


class StudyListCreate(ListCreateAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
