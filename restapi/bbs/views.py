# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from bbs.models import Bbs
from bbs.serializers import BbsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# Create your views here.
class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer

class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializer