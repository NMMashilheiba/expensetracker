from email import message
from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        messages.success(request, "Success Alert message")
        messages.warning(request, "Warning Alert message")
        messages.info(request, "Info Alert message")
        messages.error(request, "Error Alert message")
        
        return render(request, 'authentication/register.html')

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error' : 'Email not valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error' : 'This email is already taken'}, status=409)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error' : 'Username should be alphanumeric'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error' : 'This username is already taken'}, status=409)
        return JsonResponse({'username_valid': True})