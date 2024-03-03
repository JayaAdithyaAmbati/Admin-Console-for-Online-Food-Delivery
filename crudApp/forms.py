from django import forms
from .models import Restaurant, Signup
from django.core.validators import MaxValueValidator,MinValueValidator

class Restaurantform(forms.ModelForm):
    rating = forms.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    class Meta:
        model = Restaurant
        fields='__all__'

class Regform(forms.ModelForm):
    #Aid = forms.IntegerField(validators=[MaxValueValidator(30),MinValueValidator(2)])
    #Apswd = forms.IntegerField(validators=[MaxValueValidator(30),MinValueValidator(3)])
    Rid = forms.CharField()
    Rpswd = forms.CharField()
    class Meta:
        model= Signup
        fields= ['Rid','Rpswd']