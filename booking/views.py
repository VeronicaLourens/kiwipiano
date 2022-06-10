from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Lesson
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm, UserProfileForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def home(request):
    """
    To render the home view.
    """
   
    return render(request, 'index.html')

# class Home(View):

#     def get(self, request):
#         return render(request, 'index.html')




def register(request):
    """
    To render the register view.
    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account registration is successful!')


            return redirect('feedback')
            
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def feedback(request):
    """
    To render the registration feedback view after 
    user registered on the register view.
    """
    return render(request, 'accounts/register_feedback.html')


def login_view(request):
    """
    To render the login page to log user in the account.
    """

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect('profile')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})



@login_required
def profile(request):
    """
    To render the user profile page.
    """
    
    
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_profile_form.is_valid() and profile_update_form.is_valid():
            user_profile_form.save()
            profile_update_form.save()

            messages.success(request, f'Your profile has been updated.')

            return redirect('profile')

        else:
            messages.error(request, f'Please try again.')

    else:
        user_profile_form = UserProfileForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

   
    context = {
        #'user': request.user,
        #'profile': Profile.objects.all()
        #'user': User.objects.get(user=request.user),
        #'profile': Profile.objects.get(user=request.user),
        'user_profile_form': user_profile_form,
        'profile_update_form': profile_update_form,
        'messages': messages

    }
   
    return render(request, 'accounts/profile.html', context)
   


def update_profile(request):
    """
    To render the update profile page.
    """

    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your profile has been updated.')

            return redirect('profile')

        else:
            messages.error(request, 'Please try again.')

    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profile.html', {'form': form})



def logout_view(request):
    """
    To render the logout page.
    """

    logout(request)

    return render(request, 'accounts/logout.html')



