from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self) -> str:
        return self.name
    
