from django.contrib import admin
from .models import Compte, Contributeur, Tweet, Corpus, Type_Annotation, Categorie_Sentiment, Annotation, Est_Contradictoire

admin.site.register(Compte)
admin.site.register(Contributeur)
admin.site.register(Corpus)
admin.site.register(Tweet)
admin.site.register(Type_Annotation)
admin.site.register(Categorie_Sentiment)
admin.site.register(Annotation)
admin.site.register(Est_Contradictoire)

# Register your models here.
