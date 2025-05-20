from django.db import models
from django.utils import timezone  # Fixed indentation: no leading spaces

# Define choices globally so they can be shared across models
CATEGORY_CHOICES = [
    ('sedan', 'Sedan'),
    ('suv', 'SUV'),
    ('hatchback', 'Hatchback'),
    ('coupe', 'Coupe'),
    ('van', 'Van'),
]

TRANSMISSION_CHOICES = [
    ('automatic', 'Automatic'),
    ('manual', 'Manual'),
]

FEATURE_CHOICES = [
    ('gps', 'GPS'),
    ('ac', 'Air Conditioning'),
    ('bluetooth', 'Bluetooth'),
    ('usb', 'USB Port'),
    ('sunroof', 'Sunroof'),
]

class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    mot_de_passe = models.CharField(max_length=128)
    
    # usertype = False → client, True → administrateur
    usertype = models.BooleanField(default=False)

    def __str__(self):
        role = "Admin" if self.usertype else "Client"
        return f"{role} : {self.nom} {self.prenom}"

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    immatriculation = models.CharField(max_length=20, unique=True)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='voitures/', null=True, blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='sedan',
        help_text='The category of the car (e.g., SUV, Sedan).'
    )

    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES,
        default='automatic',
        help_text='The transmission type of the car.'
    )

    features = models.ManyToManyField(
        'Feature',
        blank=True,
        help_text='The features available in the car.'
    )

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"

class Feature(models.Model):
    name = models.CharField(
        max_length=50,
        choices=FEATURE_CHOICES,
        unique=True,
        help_text='The name of the feature.'
    )

    def __str__(self):
        return self.name

class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name="reservations")
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réservation #{self.id} - {self.client.nom}"

class Commentaire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Commentaire de {self.nom}"