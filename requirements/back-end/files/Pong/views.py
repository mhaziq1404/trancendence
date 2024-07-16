import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from .models import User  # Ensure User model is imported

# Replace with your Node.js JWT service URL
JWT_SERVICE_URL = 'http://JWT:3000'

# Replace with your 2FA server URL
TWO_FA_SERVICE_URL = 'http://2FA:3001'

def generate_2fa_secret():
    response = requests.post(f'{TWO_FA_SERVICE_URL}/generate-secret')
    if response.status_code == 200:
        return response.json().get('secret')
    return None

def verify_2fa_token(secret, token):
    response = requests.post(f'{TWO_FA_SERVICE_URL}/verify-token', json={'secret': secret, 'token': token})
    return response.json().get('verified')

def send_2fa_token(email, secret):
    response = requests.post(f'{TWO_FA_SERVICE_URL}/send-token', json={'email': email, 'secret': secret})
    return response.status_code == 200

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
            login(request, user)

            # Generate JWT token and store in session
            jwt_token = generate_jwt_token(user.username)
            if jwt_token:
                request.session['jwt_token'] = jwt_token

            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

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

def verify_2fa(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        secret = request.session.get('2fa_secret')
        user_id = request.session.get('user_id')
        if verify_2fa_token(secret, token):
            user = User.objects.get(id=user_id)
            login(request, user)
            # Generate JWT token and store in session
            jwt_token = generate_jwt_token(user.username)
            if jwt_token:
                request.session['jwt_token'] = jwt_token
            return redirect('index')
        else:
            return redirect('login')
    return render(request, '2fa_verify.html')

