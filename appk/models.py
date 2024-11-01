# models.py
from django.db import models
from django.utils import timezone

class Piece(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'En cours'),
        ('completed', 'Terminée')
    ]
    name = models.CharField(max_length=100, default='Pièce 1')   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def start(self):
        self.status = 'in_progress'
        self.start_date = timezone.now()
        self.end_date = None   
        self.save()

    def stop(self):
        self.status = 'completed'
        self.end_date = timezone.now()
        self.save()
    
    def __str__(self):
        return f"{self.name} - {self.status}"
