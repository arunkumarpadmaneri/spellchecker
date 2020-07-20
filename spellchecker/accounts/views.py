from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, authentication_classes, permission_classes

# from django.contrib.auth import get_user_model, logout
# from django.core.exceptions import ImproperlyConfigured
# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from . import serializers
# from .utils import get_and_authenticate_user, create_user_account
# User = get_user_model()

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,instance=request.user)
        print(form.is_valid(),form.errors)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
        else:
            return render(request, "registration/signup.html", {"form":form})
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {"form":form})

def home(request):
    print("home")
    if request.user.is_authenticated:
        is_anonymous_user = False
    else:
        is_anonymous_user = True
    return render(request,"home.html",{"is_anonymous_user":is_anonymous_user,"user":request.user})    

def upload_docs(request):
    print("uploaded docs",request)
    if request.user.is_authenticated:        
        return render(request, "upload_docs.html", {})
    else:
        return redirect("/accounts/login")


# class AuthViewSet(viewsets.GenericViewSet):
#     permission_classes = [AllowAny, ]
#     serializer_class = serializers.EmptySerializer
#     serializer_classes = {
#         'login': serializers.UserLoginSerializer,
#     }

#     @action(methods=['POST', ], detail=False)
#     def login(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = get_and_authenticate_user(**serializer.validated_data)
#         data = serializers.AuthUserSerializer(user).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     @action(methods=['POST', ], detail=False)
#     def register(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = create_user_account(**serializer.validated_data)
#         data = serializers.AuthUserSerializer(user).data
#         return Response(data=data, status=status.HTTP_201_CREATED)        
    
#     @action(methods=['POST', ], detail=False)
#     def logout(self, request):
#         logout(request)
#         data = {'success': 'Sucessfully logged out'}
#         return Response(data=data, status=status.HTTP_200_OK)

#     @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
#     def password_change(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         request.user.set_password(serializer.validated_data['new_password'])
#         request.user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get_serializer_class(self):
#         if not isinstance(self.serializer_classes, dict):
#             raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

#         if self.action in self.serializer_classes.keys():
#             return self.serializer_classes[self.action]
#         return super().get_serializer_class()