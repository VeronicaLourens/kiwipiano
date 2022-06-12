from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Booking, Session


class UserRegisterForm(UserCreationForm):
    """ 
    The register form is to be filled in with 
    user information for account registration.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserProfileForm(forms.ModelForm):
    """
    The profile form is for user to edit user's profile information."
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
      


class ProfileUpdateForm(forms.ModelForm):
    """
    To update user profile image.
    """

    class Meta:
        model = Profile
        fields = ['profile_image', 'phone_number']



class DatePicker(forms.DateInput):
    """
    To use the datepicker for the booking form.
    """
    input_type = 'date'
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])




class BookingForm(forms.ModelForm):
    """
    The booking form is for user to fill in certain information for booking a secssion.
    """

    class Meta:
        model = Booking
        fields = ['user', 'session_name', 'date', 'start_time']

        widgets = {
            'date': DatePicker()
        }


