from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    signup_enabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

class Signup(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='signups')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} → {self.event.title}"