from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from members.models import UserProfile

@login_required(login_url='login')
def user_profile(request): 
    me = request.user
    user_profile = UserProfile.objects.get( user = me)
    return render(request, 'user_profile.html',{'user_profile' : user_profile})