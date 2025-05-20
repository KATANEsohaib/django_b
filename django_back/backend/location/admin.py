from django.contrib import admin
from .models import User, Voiture, Feature, Reservation, Commentaire

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'usertype', 'telephone')
    list_filter = ('usertype',)
    search_fields = ('nom', 'prenom', 'email')

@admin.register(Voiture)
class VoitureAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'annee', 'immatriculation', 'prix', 'disponible')
    list_filter = ('disponible', 'category', 'transmission')
    search_fields = ('marque', 'modele', 'immatriculation')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'voiture_info', 'date_debut', 'date_fin', 'montant_total', 'created_at')
    list_filter = ('date_debut', 'date_fin')
    search_fields = ('client__nom', 'client__prenom', 'voiture__marque', 'voiture__modele')
    date_hierarchy = 'date_debut'

    def client_name(self, obj):
        return f"{obj.client.nom} {obj.client.prenom}"
    client_name.short_description = 'Client'

    def voiture_info(self, obj):
        return f"{obj.voiture.marque} {obj.voiture.modele}"
    voiture_info.short_description = 'Voiture'

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message')
    search_fields = ('nom', 'email', 'message')