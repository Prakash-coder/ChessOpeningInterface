from django.db import models

class YourOpening(models.Model):
    opening_name = models.CharField(max_length=120)
    opening_moves = models.IntegerField()
    opening_sequence = models.CharField(max_length=1000)

class YourRepertiore(YourOpening):
    repertiore_moves = models.IntegerField()
    repertiore_sequence = models.CharField(max_length=120)

    

    
