from django.db import models
from django.contrib.auth.models import User
CHOICES = [
    ('AN', 'Anime'),
    ('TW', 'TV/WebSeries'),
    ('MV', 'Movie'),
]


class ReviewModel(models.Model):
    ReviewUser = models.ForeignKey(User, on_delete=models.CASCADE)
    ReviewTitle = models.CharField(max_length=100)
    ReviewMessage = models.TextField(max_length=500)
    ReviewImageURL = models.CharField(max_length=1000)
    Upload_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Type = models.CharField(
        max_length=2, choices=CHOICES, default='AN')

    def __str__(self) -> str:
        return f"{self.ReviewTitle}"
