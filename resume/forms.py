from django import forms
from resume.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=100, required=True)
    birth_date = forms.CharField(max_length=100)
    education = forms.CharField(max_length=100, required=True)
    experience = forms.CharField(max_length=200)
    skills = forms.CharField(max_length=150, required=True)
    portfolio = forms.URLField()


    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'photo',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'birth_date',
            'education',
            'experience',
            'skills',
            'portfolio',
            'city',
            'position',
            'gender'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user