from django.db import models
from django.contrib.auth.models import User
from django import forms

class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


class Place(models.Model):
    price = models.CharField(max_length=10)
    images = models.FileField(null=True)
    description = models.CharField(max_length=400)
    addres = models.CharField(max_length=300, null=True)
    gmaddres = models.CharField(max_length=300, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    name = models.CharField(max_length=20)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True, null=True) 

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'addres', 'price', 'images']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 6}),
            'addres': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Addres', 'rows': 2}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
            'images': forms.FileInput(attrs={'class': 'form-control', 'multiple': True})
        }



class Image(models.Model):
    place = models.ForeignKey(Place, default=None, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images', blank=True, null=True)



# class Rating(models.Model):
#     place = models.ForeignKey(Place, default=None, on_delete=models.PROTECT)
#     user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
#     rating = models.IntegerField()


# class PlaceLikes(models.Model):
#     place = models.ForeignKey(Place, default=None, on_delete=models.PROTECT)
#     user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)


# class PlaceComment(models.Model):
#     place = models.ForeignKey(Place, default=None, on_delete=models.PROTECT)
#     user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

