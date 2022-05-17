from django.db import models

class SeedPhrase(models.Model):
    seed = models.CharField(max_length=25)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Seed Phrase"
    
    def __str__(self):
        return self.seed
    