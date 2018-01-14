from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rostermaker.models import Paddler
from rostermaker.serializers import UserSerializer, GroupSerializer, PaddlerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PaddlerViewSet(viewsets.ModelViewSet):
    queryset = Paddler.objects.all().order_by('id')
    serializer_class = PaddlerSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer