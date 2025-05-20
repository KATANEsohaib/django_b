from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .models import Voiture, User, Commentaire, Reservation
from .serializers import VoitureSerializer, UserSerializer, CommentaireSerializer, ReservationSerializer

@api_view(['GET'])
def get_all_voitures(request):
    voitures = Voiture.objects.all()
    serializer = VoitureSerializer(voitures, many=True)
    return Response({"voitures": serializer.data})

@api_view(['GET'])
def get_by_id_voiture(request, pk):
    voiture = get_object_or_404(Voiture, id=pk)
    serializer = VoitureSerializer(voiture, many=False)
    return Response({"voiture": serializer.data})

@api_view(['PUT'])
def update_voiture(request, pk):
    try:
        voiture = Voiture.objects.get(pk=pk)
    except Voiture.DoesNotExist:
        return Response({"error": "Voiture introuvable"}, status=404)

    serializer = VoitureSerializer(voiture, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_voiture(request, pk):
    try:
        voiture = Voiture.objects.get(pk=pk)
    except Voiture.DoesNotExist:
        return Response({"error": "Voiture introuvable"}, status=404)

    voiture.delete()
    return Response({"message": "Voiture supprimée"}, status=204)

@api_view(['POST'])
def create_voiture(request):
    serializer = VoitureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"users": serializer.data})

@api_view(['GET'])
def get_user_by_id(request, pk):
    user = get_object_or_404(User, id=pk)
    serializer = UserSerializer(user)
    return Response({"user": serializer.data})

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_commentaires(request):
    commentaires = Commentaire.objects.all()
    serializer = CommentaireSerializer(commentaires, many=True)
    return Response({"commentaires": serializer.data})

@api_view(['POST'])
def ajouter_commentaire(request):
    serializer = CommentaireSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_commentaire(request, pk):
    try:
        commentaire = Commentaire.objects.get(pk=pk)
    except Commentaire.DoesNotExist:
        return Response({"error": "Commentaire introuvable"}, status=404)

    serializer = CommentaireSerializer(commentaire, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_commentaire(request, pk):
    try:
        commentaire = Commentaire.objects.get(pk=pk)
    except Commentaire.DoesNotExist:
        return Response({"error": "Commentaire introuvable"}, status=404)

    commentaire.delete()
    return Response({"message": "Commentaire supprimé"}, status=204)

@api_view(['GET'])
def get_all_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({"error": "Reservation non trouvée"}, status=404)

    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)

@api_view(['POST'])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({"error": "Reservation non trouvée"}, status=404)

    serializer = ReservationSerializer(reservation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({"error": "Reservation non trouvée"}, status=404)

    reservation.delete()
    return Response({"message": "Réservation supprimée"}, status=204)