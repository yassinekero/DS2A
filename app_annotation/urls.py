from django.urls import path
from . import views

urlpatterns = [
  path("login/", views.login, name="login"),
  path("login/username-exists", views.login_user_exist, name="login_user_exist"),
  path("login/account-created", views.login_after_registration, name="login_after_registration"),
  path("login/wrong-password", views.login_wrong_password, name="login_wrong_password"),
  path("login/user-not-found", views.login_user_not_found, name="login_user_not_found"),
  path("login/account-blocked", views.account_blocked, name="account_blocked"),
  path("login/authenticate/", views.authenticate, name="authenticate"),
  path("register/", views.register, name="register"),
  path("account/admin/dashboard", views.dashboard_admin, name="admin_dashboard"),
  path("account/contributeur/dashboard", views.dashboard_contributeur, name="contributeur_dashboard"),
  path("logout/admin", views.logout_admin, name="logout_admin"),
  path("logout/contributeur", views.logout_contri, name="logout_contri"),
  path("account/admin/upload-corpus", views.upload_corpus, name="upload_corpus"),
  path("account/admin/creer-corpus", views.creer_corpus, name="creer_corpus"),
  path("account/admin/modifier-corpus", views.modifier_corpus, name="modifier_corpus"),
  path("account/admin/modifier-corpus-id=<int:corpus_id>", views.modifier_corpus_id, name="modifier_corpus_id"),
  path("account/admin/supprimer-corpus-id=<int:corpus_id>", views.supprimer_corpus_id, name="supprimer_corpus_id"),
  path("account/admin/masque-corpus-id=<int:corpus_id>", views.masquer_corpus, name="masquer_corpus"),
  path("account/admin/ajouter-type-annotation", views.ajouter_type_annotation, name="ajouter_type_annotation"),
  path("account/admin/modifier-type-annotation-id=<int:type_id>-etiquettes-contradictoires", views.ajouter_etiquette_contradictoire, name="ajouter_etiquette_contradictoire"),
  path("account/admin/modifier-type-annotation-id=<int:type_id>-etiquettes-contradictoires-avec-succes", views.ajouter_etiquette_contradictoire_done, name="ajouter_etiquette_contradictoire_done"),
  path("account/admin/modifier-type-annotation", views.modifier_type_annotation, name="modifier_type_annotation"),
  path("account/admin/modifier-type-annotation-id=<int:type_id>", views.modifier_type_annotation_id, name="modifier_type_annotation_id"),
  path("account/admin/supprimer-type-annotation-id=<int:type_id>", views.supprimer_type_annotation_id, name="supprimer_type_annotation_id"),
  path("account/admin/ajouter-etiquette", views.ajouter_etiquette, name="ajouter_etiquette"),
  path("account/admin/chercher-tweets", views.chercher_tweets, name="chercher_tweets"),
  path("account/admin/chercher-tweets-query=<str:query>-tweets-<int:limit>", views.chercher_tweets_keyword, name="chercher_tweets_keyword"),

  #Contributeur 


  path("account/contributeur/consulter-corpus", views.afficher_corpus_contr, name="afficher_corpus_contr"),
  path("account/contributeur/annoter-corpus-id=<int:corpus_id>", views.annoter_corpus, name="annoter_corpus"),
  path("account/contributeur/supprimer-annotation-corpus-id=<int:corpus_id>-login=<str:contributeur>", views.supprimer_annotation, name="supprimer_annotation"),
  path("account/contributeur/mes-annotations", views.mes_annotations, name="mes_annotations"),
  path("account/contributeur/mes-annotations-id=<int:corpus_id>", views.mes_annotations_id, name="mes_annotations_id"),
  path("account/contributeur/mon-compte", views.mon_compte, name="mon_compte"),


  #Resultats Annotation

  path("account/admin/resultat/afficher-corpus", views.afficher_corpus_res, name="afficher_corpus_res"),
  path("account/admin/resultat/resultat-corpus-id=<int:corpus_id>", views.corpus_resultat, name="corpus_resultat"),
    path("account/admin/resultat/resultat-graph-corpus-id=<int:corpus_id>", views.corpus_resultat_graph, name="corpus_resultat_graph"),
  
  #Gere Compte Admin

  path("account/admin/gerer-contributeur-login=<str:contr_id>", views.gerer_contr, name="gerer_contr"),
  path("account/admin/bloquer-contributeur-login=<str:contr_id>", views.bloquer, name="bloquer_contr"),

 
  #Navigation Admin

  path("account/admin/corpus", views.corpus, name="corpus"),
  path("account/admin/type-annotation", views.type_annotation, name="type_annotation"),
  path("account/admin/resultat", views.resultat, name="resultat"),
  path("account/admin/contributeurs", views.contributeurs, name="contributeurs"),



  path("account/admin/resultat/annotation-globale-corpus-id=<int:corpus_id>", views.annotation_globale, name="annotation_globale"),
  path("account/admin/resultat/exporter-resultat-corpus-id=<int:corpus_id>", views.exporter_resultat, name="exporter_resultat"),
  path("account/admin/resultat/annotation-globale-corpus-id=<int:corpus_id>-modifier", views.annotation_globale_modifier, name="annotation_globale_modifier"),

#Redirection 
path("account/admin/upload-corpus-avec-succes", views.upload_corpus_done, name="upload_corpus_done"),
path("account/admin/upload-corpus-avec-erreur", views.upload_corpus_error, name="upload_corpus_error"),
path("account/admin/creer-corpus-avec-succes", views.creer_corpus_done, name="creer_corpus_done"),
path("account/admin/modifier-corpus-id=<int:corpus_id>-avec-succes", views.modifier_corpus_id_done, name="modifier_corpus_id_done"),
path("account/admin/ajouter-type-annotation-avec-succes", views.ajouter_type_annotation_done, name="ajouter_type_annotation_done"), 
path("account/admin/ajouter-etiquette-done", views.ajouter_etiquette_done, name="ajouter_etiquette_done"),
path("account/admin/modifier-type-annotation-id=<int:type_id>-avec-succes", views.modifier_type_annotation_id_done, name="modifier_type_annotation_id_done"),
path("account/contributeur/annoter-corpus-id=<int:corpus_id>-avec-succes", views.annoter_corpus_done, name="annoter_corpus_done"),
path("account/admin/resultat/annotation-globale-corpus-id=<int:corpus_id>-modifier-avec-succes", views.annotation_globale_modifier_done, name="annotation_globale_modifier_done"),
 path("account/contributeur/mon-compte-modifie-avec-succes", views.mon_compte_done, name="mon_compte_done"),


  

]
