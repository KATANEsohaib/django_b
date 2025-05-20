from rest_framework import serializers
from .models import Voiture, Feature, User, Commentaire, Reservation
from django.utils import timezone

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['name']

class VoitureSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True)

    class Meta:
        model = Voiture
        fields = ['id', 'marque', 'modele', 'annee', 'immatriculation', 'prix', 'disponible', 'image', 'category', 'transmission', 'features']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nom', 'prenom', 'email', 'telephone', 'adresse', 'usertype']

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'client', 'voiture', 'date_debut', 'date_fin', 'montant_total']
        extra_kwargs = {
            'client': {'required': True},
            'voiture': {'required': True},
            'date_debut': {'required': True},
            'date_fin': {'required': True}
        }