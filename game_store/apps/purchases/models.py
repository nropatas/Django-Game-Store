from django.db import models
from game_store.apps.users.models import UserProfile
from game_store.apps.games.models import Game

class Purchase(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.user.username + " - " + self.game.title