from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Rating

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Enter a valid email address.")
    profile_photo = forms.ImageField(label="Select a profile image")
    bio = forms.CharField(max_length=500, label="Bio", help_text="Tell us about yourself.", widget=forms.Textarea(
            attrs={"placeholder": "Add a description of yourself",}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_photo', 'bio')

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'photo', 'description', 'link')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content')
