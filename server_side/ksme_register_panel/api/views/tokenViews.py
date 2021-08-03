from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.response import Response

# creates the uid and token, to be send to the user email ---
def emailVerificationArguments(user, request):
    current_site = get_current_site(request)
    return {
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
        'domain': current_site.domain
    }