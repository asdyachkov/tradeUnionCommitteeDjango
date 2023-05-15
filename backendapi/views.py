from rest_framework import generics

from .models import News, Pins, Documents, Benefits, StudentsContacts, TeachersContacts
from .serializers import (
    NewsSerializer,
    PinsSerializer,
    DocumentsSerializer,
    BenefitsSerializer,
    StudentsContactsSerializer,
    TeachersContactsSerializer,
)


class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class PinsApiView(generics.ListAPIView):
    queryset = Pins.objects.all()
    serializer_class = PinsSerializer


class DocumentsApiView(generics.ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class DocumentApiView(generics.RetrieveAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer


class BenefitsApiView(generics.ListAPIView):
    queryset = Benefits.objects.all()
    serializer_class = BenefitsSerializer


class StudentsContactsApiView(generics.ListAPIView):
    queryset = StudentsContacts.objects.all()
    serializer_class = StudentsContactsSerializer


class TeachersContactsApiView(generics.ListAPIView):
    queryset = TeachersContacts.objects.all()
    serializer_class = TeachersContactsSerializer
