from django.db import models

class Crypto(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    rank = models.SmallIntegerField()
    category = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    quote = models.FloatField()
    max_supply = models.IntegerField(blank=True, null=True)
    circulating_supply = models.FloatField()
    total_supply = models.FloatField()
    tags = models.TextField()

    def __str__(self):
        return self.symbol + ' ' + self.name

    def get_details(self):
        return "Asset:\t{}\n\tTicker: {}\n\tBalance: {}".format(
            self.name,
            self.symbol,
            self.balance
        )