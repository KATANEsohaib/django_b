from django.urls import path
from .views import (
    get_all_voitures, get_by_id_voiture,create_voiture, update_voiture, delete_voiture,
    get_all_users, get_user_by_id, create_user,
    get_all_commentaires, ajouter_commentaire, update_commentaire, delete_commentaire,
    get_all_reservations, get_reservation, create_reservation, update_reservation, delete_reservation
)

urlpatterns = [
    path('voitures/', get_all_voitures),
    path('voitures/<int:pk>/', get_by_id_voiture),
    path('voitures/create/', create_voiture),
    path('voitures/<int:pk>/', update_voiture),
    path('voitures/<int:pk>/', delete_voiture),
    path('users/', get_all_users),
    path('users/<int:pk>/', get_user_by_id),
    path('users/create/', create_user),
    path('commentaires/', get_all_commentaires),
    path('commentaires/ajouter/',ajouter_commentaire),
    path('commentaires/update/<int:pk>/',update_commentaire),
    path('commentaires/delete/<int:pk>/',delete_commentaire),
    path('reservations/',get_all_reservations),
    path('reservations/<int:pk>/',get_reservation),
    path('reservations/create/',create_reservation),
    path('reservations/update/<int:pk>/',update_reservation),
    path('reservations/delete/<int:pk>/',delete_reservation),
]
