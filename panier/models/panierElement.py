from django.db import models
from .panier import Panier
from .article import Article



class PanierElement(models.Model):
    panierId = models.ForeignKey(Panier, on_delete=models.CASCADE)
    aricleId = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)


    def prixTotal(self):
        return self.aricleId.articlePrice * self.quantite
    
    # def __str__(self):
    #     return f"Élément du panier de {self.panierId.utilisateur.username}"