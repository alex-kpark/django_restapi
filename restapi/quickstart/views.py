# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from restapi.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render

# Create your views here.

#사용자(User)를 보거나 편집하는 API
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

#그룹(Group)을 보거나 편집하는 API
class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
