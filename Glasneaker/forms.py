from django import forms
from django.contrib.auth.models import User
from Glasneaker.models import UserProfile

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) #hide passwords

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(
#         choices=PRODUCT_QUANTITY_CHOICES,
#         coerce=int)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)