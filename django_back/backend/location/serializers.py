from rest_framework import serializers
from .models import Voiture
from .models import User
from .models import Commentaire
from .models import Reservation


class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'        


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'        




