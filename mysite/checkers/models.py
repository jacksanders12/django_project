from django.db import models

class Game(models.Model):
    winning_color = models.CharField(max_length=10)
    date = models.DateTimeField('date published')
    player_name = models.CharField(max_length=200)

class Turns(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    game_state = models.CharField(max_length=1000)
