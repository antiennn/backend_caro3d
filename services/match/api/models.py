from djongo import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Match(BaseModel):
    id = models.AutoField(primary_key=True)

    class STATE(models.TextChoices):
        WAITING = "waiting",
        PLAYING = "playing",
        ENDED = "ended",
    state = models.CharField(max_length=12, choices=STATE.choices, null=False, default=STATE.WAITING)
    winner = models.TextField(max_length=20, null=True)

