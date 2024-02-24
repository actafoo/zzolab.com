from rest_framework import serializers
from study.models import Study


class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'
        read_only_fields = ("id", "created_at", "updated_at")
