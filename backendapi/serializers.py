from rest_framework import serializers

from .models import News, Pins, Documents, Benefits, StudentsContacts, TeachersContacts


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
        read_only_fields = ["id"]


class PinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pins
        fields = "__all__"
        read_only_fields = ["id"]


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"
        read_only_fields = ["id"]


class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = "__all__"
        read_only_fields = ["id"]


class StudentsContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsContacts
        fields = "__all__"
        read_only_fields = ["id"]


class TeachersContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersContacts
        fields = "__all__"
        read_only_fields = ["id"]
