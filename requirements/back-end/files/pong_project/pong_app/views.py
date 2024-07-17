from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm




# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# works until here only
# Replace with your Node.js JWT service URL
JWT_SERVICE_URL = 'http://localhost:3000'
def generate_jwt_token(username):
    response = requests.post(f'{JWT_SERVICE_URL}/generateToken', json={'username': username})
    if response.status_code == 200:
        return response.json().get('token')
    return None

def validate_jwt_token(token):
    response = requests.post(f'{JWT_SERVICE_URL}/validateToken', json={'token': token})
    if response.status_code == 200:
        return True
    return False

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Password will be hashed automatically

            # Generate JWT token and store in session
            jwt_token = generate_jwt_token(user.username)
            if jwt_token:
                request.session['jwt_token'] = jwt_token

            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()

            secret = generate_2fa_secret()
            if secret:
                send_2fa_token(user.email, secret)
                request.session['2fa_secret'] = secret
                request.session['user_id'] = user.id
                return redirect('verify_2fa')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    jwt_token = request.session.get('jwt_token')
    if not jwt_token or not validate_jwt_token(jwt_token):
        return redirect('login')

    # Continue with authenticated logic
    return render(request, 'index.html')