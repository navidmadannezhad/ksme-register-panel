from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from management.models import Activity
from .tokenViews import emailVerificationArguments
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render

# email imports
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from ..serializers import UserSerializer , Level1Serializer, Level2Serializer, Level3Serializer


class UsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized_data = UserSerializer(users, many=True)

        return Response(serialized_data.data)


class Level1(APIView):
    def post(self, request):

        serializer = Level1Serializer(data=request.data)

        try:
            if serializer.is_valid():
                return Response(True, status=200)

            else:
                return Response(serializer.errors, status=400)
        except:
            context = {
                'server error': 'An error has occured on the server'
            }
            return Response(context, status=500)



class Level2(APIView):
    def post(self, request):

        serializer = Level2Serializer(data = request.data)

        try:
            if serializer.is_valid():
                return Response(True, status=200)

            else:
                return Response(serializer.errors, status=400)
        except:
            context = {
                'server error': 'An error has occured on the server'
            }
            return Response(context, status=500)


class Level3(APIView):
    def post(self, request):

        serializer = Level3Serializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(email=request.data['email'])
            context = {
                'uid': emailVerificationArguments(user=user, request=request)['uid'],
                'token': emailVerificationArguments(user=user, request=request)['token'],
                'domain': emailVerificationArguments(user=user, request=request)['domain'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name']
            }
            html_content = render_to_string('email/email.html', context)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                'فعال کردن حساب کاربری',
                text_content,
                'ksme.kiau@gmail.com',
                [request.data['email']],
            )

            email.attach_alternative(html_content, 'text/html')
            email.send()

            return Response(True, status=200)
        else:
            return Response(serializer.errors, status=400)


class Activate(APIView):
    def get(self, request, uidb64, token):
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if user is not None and default_token_generator.check_token(user, token):
            activity = Activity.objects.get(user=user)
            if activity.activity is not True:
                activity.activity = True
                activity.save()
                return render(request, 'management/email_success.html')
            else:
                return render(request, 'management/email_fail.html')
        else:
            return render(request, 'management/email_fail.html')

