from django.db import models
from django.db.models.fields import DateField

# Create A Blog models
# Titele
# Publication date
# Text Body
# Image

# Add Blog app to the settings
# Create a migration
# Migrate
# Add to admin

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pubDate = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    def pubDatePretty(self):
        return self.pubDate.strftime('%b %e %Y')