from rest_framework import serializers
from study.models import Study, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class StudySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Study
        fields = '__all__'
        read_only_fields = ("id", "created_at", "updated_at")

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(**category_data)
        study = Study.objects.create(category=category, **validated_data)
        return study
