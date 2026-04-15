class Car(models.Model):
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
