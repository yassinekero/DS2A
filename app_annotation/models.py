from django.db import models

class Compte(models.Model):
    login = models.CharField("Login", max_length=100, primary_key=True)
    password = models.CharField("Password", max_length=150, null=False)
    est_admin = models.BooleanField("Est_admin", default=False) 
    def __str__(self):
        return self.login

class Contributeur(models.Model):
    login = models.ForeignKey(Compte, on_delete=models.CASCADE, primary_key= True)
    nom = models.CharField("Nom", max_length=100,default="", null=False)
    prenom = models.CharField("Prenom", max_length=100,default="", null=False)
    bloque = models.BooleanField("Bloque", default=False)
    email = models.CharField("Email", max_length=100, null=True)
    profession = models.CharField("Profession", max_length=100, null=True)
    tele = models.IntegerField("Tele", max_length=20, null=True)
    def __str__(self):
        return self.login.login


class Type_Annotation(models.Model):
    nom_type = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom_type


class Corpus(models.Model):
    titre_corpus = models.CharField("Titre Corpuse", max_length=200,default="Corpus sans titre", null=False)
    masque = models.BooleanField("Masqué", default=False, null=False)
    type_annotation = models.ForeignKey(Type_Annotation, on_delete=models.CASCADE)
    annot = models.BooleanField("Annote", default=False, null=False)
    def __str__(self):
        return ("Corpus-" + (str)(self.id))
    

class Tweet(models.Model):
    text = models.CharField("Text", max_length=1000, default="", null=True)
    annotation_general = models.CharField("Annotation General", max_length=150, null=True)
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)
   
    def __str__(self):
        return ("Tweet-" + (str)(self.id) + "_Corpus-" + (str)(self.corpus.id)) 


    
class Categorie_Sentiment(models.Model):
    nom_categorie = models.CharField(max_length=200, null=True)
    type_annotation = models.ForeignKey(Type_Annotation, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_categorie

class Est_Contradictoire(models.Model):
    cat1 = models.ForeignKey(Categorie_Sentiment, related_name='cat1',  on_delete=models.CASCADE)
    cat2 = models.ForeignKey(Categorie_Sentiment,  related_name='cat2', on_delete=models.CASCADE)
    type_annotation = models.ForeignKey(Type_Annotation, on_delete=models.CASCADE)
    def __str__(self):
        return ((str)(self.cat1.nom_categorie) + "_"  + (str)(self.cat2.nom_categorie))

class Annotation(models.Model):
    avis = models.IntegerField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    contributeur = models.ForeignKey(Contributeur, null= True, on_delete=models.SET_NULL)
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return "Annot_" +(str)(self.id) + "-Tweet_" + (str)(self.tweet) + "-Contr_" + (str)(self.contributeur) + "-Corpus_ " + (str)(self.corpus)
