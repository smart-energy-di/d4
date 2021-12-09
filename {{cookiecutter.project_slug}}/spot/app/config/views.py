import os

from authlib.integrations.django_client import OAuth
from django.shortcuts import render, redirect
from django.urls import reverse

oauth = OAuth()
oauth.register(
    name='keycloak',
    client_id=os.getenv("D4SERVICE_OAUTH2_CLIENT_ID"),
    client_secret=os.getenv("D4SERVICE_OAUTH2_CLIENT_SECRET"),
    access_token_url=os.getenv("D4SERVICE_OAUTH2_TOKEN_ENDPOINT"),
    authorize_url=os.getenv("D4SERVICE_OAUTH2_AUTH_ENDPOINT"),
    jwks_uri=os.getenv("D4SERVICE_OAUTH2_JWKS_URI"),
    client_kwargs={
        'scope': 'openid email profile'
    }
)


def user(request):
    user = request.session.get('user')
    return render(request, 'pages/user.html', context={'user': user})


def login(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.keycloak.authorize_redirect(request, redirect_uri)


def auth(request):
    token = oauth.keycloak.authorize_access_token(request)
    user = oauth.keycloak.parse_id_token(request, token)
    request.session['user'] = user
    return redirect('/user')


def logout(request):
    request.session.pop('user', None)
    return redirect('/user')
