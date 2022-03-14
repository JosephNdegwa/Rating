from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.ImageField(upload_to="images/")
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Project(models.Model):
    title = models.TextField(max_length=150)
    photo = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=500, blank=True)
    link = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rating(models.Model):
    design = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        primary_key=True,
    )
