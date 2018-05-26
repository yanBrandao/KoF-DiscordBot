from django.db import models

# Create your models here.
class Player(models.Model):
    discordUser = models.CharField(max_length=100, primary_key=True)
    nickname = models.CharField(max_length=100)
    victories = models.IntegerField()
    defeats = models.IntegerField()
    country = models.CharField(max_length=50)

class Championship(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    

class Game_version(models.Model):
	id = models.IntegerField(primary_key=True)
	year = models.IntegerField()
	version = models.CharField(max_length=100)

class Characters(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	game = models.ForeignKey(Game_version, on_delete=models.CASCADE)
	picked = models.IntegerField()
	round_win = models.IntegerField()
	round_loss = models.IntegerField()

class Team(models.Model):
	id = models.IntegerField(primary_key=True)
	characterOne = models.ForeignKey(Characters, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
	characterTwo = models.ManyToManyField(
        OtherModel,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
	characterThree = models.ForeignKey(Characters, on_delete=models.CASCADE)

class Matches(models.Model):
	id = models.IntegerField(primary_key=True)
	playerOne = models.ForeignKey(Player, on_delete=models.CASCADE)
	playerTwo = models.ForeignKey(Player, on_delete=models.CASCADE)

class Round_Score(models.Model):
	team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
	char_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
	roundWin = models.IntegerField()
	roundDefeated = models.IntegerField()
		
class Podium(models.Model):
	championship_id = models.ForeignKey(Championship, on_delete=models.CASCADE)
	player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
	playerPosition = models.IntegerField()