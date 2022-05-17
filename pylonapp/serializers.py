from rest_framework import serializers
from .models import SeedPhrase

class SeedPhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedPhrase
        exclude = ("id", )