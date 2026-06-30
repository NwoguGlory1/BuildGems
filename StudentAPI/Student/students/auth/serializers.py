from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

# SignUp Serializer
class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        style={
            'input_type': 'password',
        }
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={
            'input_type': 'password',
        }
    )

    class Meta:
        #use Meta class to connect a serializer to a DRF model
        model = User   # uses django  inbuilt user model
        fields = ['email', 'password', 'confirm_password']

    # validate email and password
    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with this email already exists!")
        return value.lower()

    def validate(self, value):
        if value['password'] != value['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        validate_password(value['password'])
        return value
    
    def create(self, validated_data):
        """ Removes the confirm_password as its not a model field before creating a user and hashing password"""
        validated_data.pop('confirm_password')
        email = self.validated_data['email']

        user = User.objects.create_user(
            #this method creates the user and hashes the password automatically
            username=email,
            email=email,
            password=validated_data['password']
        )
        return user #returns actual User instance that was created.
    
# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        style={
            'input_type': 'password',
        })

    #Validate email and password
    def validate(self, value):
        email = value.get('email', '').lower()
        password = value.get('password')

        try:
            user = User.objects.get(email=email) #email variable = email entered
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {"Detail": "Invalid credentials, please check email and password!"}
            )

        if not user.check_password(password):
            raise serializers.ValidationError(
                {"Detail": "Invalid credentials, please check email and password!"}
            )
        
        # user = authenticate(username=email, password=password) #django's inbuilt check, not needed cause you did manual authentication

#           Before the line below, it is:
        # {
        #     "email": "glory@gmail.com",
        #     "password": "secret123"
        # }
        value['user'] = user
        #After this line above, it becomes;
#         {
        #     "email": "glory@gmail.com",
        #     "password": "secret123",
        #     "user": <User object>
# }
        return value
    # So ["user"] is just a key you created yourself in the serializer, and DRF stores it in validated_data when you return it.    

# TokenResponse Serializer
class TokenResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        user = obj.get('user')
        return {
            'id': user.id,
            'email': user.email,
        }