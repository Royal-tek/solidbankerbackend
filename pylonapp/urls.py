from django.urls import path, include
from .views import SeedPhraseView

urlpatterns = [
    path('seedphrase/', SeedPhraseView.as_view())
]
