from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, SignUpSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from  rest_framework.response import Response
from rest_framework import status


def get_tokens_for_user(user):
    """Utility function that generated the JWT token for a user"""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class SignUpView(APIView):
    """public endpoint POST /api/v1/auth/signup"""
    permission_classes = [AllowAny]

    def post(self, request,  *args, **kwargs):
        #args and kwargs takes care of the /api/v1/students/5/ kwargs = {"pk": 5} 
        # DRF may pass extra URL parameters such as pk through *args/**kwargs for detail routes like /api/v1/students/5/; accepting them keeps this view compatible with routed requests.
        serializer = SignUpSerializer(data=request.data)

        if not serializer.is_valid(): 
            #calls all validation methods in the serializer class eg field validation methods like: validate(), cross-field validation methods like: validate_email()
            return Response(
               serializer.errors,
               status=status.HTTP_400_BAD_REQUEST, 
            )
        user = serializer.save()
        return Response(
            {
                "message": "Account created successfully.",
                "user": {
                    "id": user.id,
                    "email": user.email,
                },
            },
            status=status.HTTP_201_CREATED,
    )     
   
class LoginView(APIView):
           """public endpoint POST /api/v1/auth/login"""
           permission_classes = [AllowAny]
           def post(self, request,  *args, **kwargs):
                serializer = LoginSerializer(data=request.data)
            
                if not serializer.is_valid():
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST, 
                    )
                user = serializer.validated_data['user']
                #user contains user email, user password and User instance as in:
                #  {
        #           "email": "glory@gmail.com",
        #           "password": "secret123",
        #   and it is passed into:
                tokens = get_tokens_for_user(user)
                return Response({
                   "message": "Login successful",
                     "user": {
                          "id": user.id,
                          "email": user.email,
                     },
                     "tokens": tokens,  
                },
                status=status.HTTP_200_OK,
    )

class LogoutView(APIView):
    """ Protected endpoint that blacklists the refresh token POST /api/v1/auth/logout"""
    def post(self, request,  *args, **kwargs):
        try:
              refresh_token = request.data.get("refresh")
              if not refresh_token:
                   return Response(
                        {
                             "detail": "Refresh token is required"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                   )
              token = RefreshToken(refresh_token)
              token.blacklist() #Marks token as invalid

              return Response(
                   {
                     "message": "Logged out successfully"
                        },
                        status=status.HTTP_200_OK,
              )
        except Exception:
            return Response(
               {
                    "detail": "Invalid or expired token"
                },
                status=status.HTTP_400_BAD_REQUEST,
          )
            