from django.shortcuts import render
from .models import SeedPhrase
from .serializers import SeedPhraseSerializer
from rest_framework import generics

class SeedPhraseView(generics.ListCreateAPIView):
    queryset = SeedPhrase.objects.all()
    serializer_class = SeedPhraseSerializer