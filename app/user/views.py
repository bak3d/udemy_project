from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import UserSerializer,AuthTokenSerializers

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializer

class CreateTokeView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializers
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES