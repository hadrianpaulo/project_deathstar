from rest_framework import serializers

from .models import Document


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'date', 'doctype', 'docnum', 'created', 'modified')


class DocumentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'