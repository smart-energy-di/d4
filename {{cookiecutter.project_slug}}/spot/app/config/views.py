from authlib.integrations.django_client import OAuth
from django.shortcuts import render, redirect
from django.urls import reverse

CONF_URL = 'http://keycloak:8080/auth/realms/testing-project-realm/.well-known/openid-configuration'
oauth = OAuth()
oauth.register(
    name='keycloak',
    server_metadata_url=CONF_URL,
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
