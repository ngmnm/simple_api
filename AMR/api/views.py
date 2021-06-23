from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from .pagination import CustomPagination
from .serializers import deviceSerializer, VenderSerializer
from .models import Vender, DeviceModel


class VenderView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = VenderSerializer
    queryset = Vender.objects.all()

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk)

    def delete(self, request, pk, format=None):
        return self.destroy(request, pk)


class VenderViewAll(generics.ListCreateAPIView, generics.ListAPIView):
    serializer_class = VenderSerializer
    queryset = Vender.objects.all()
    paganation_class = CustomPagination


class DeviceModelView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = deviceSerializer
    queryset = DeviceModel.objects.all()

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk)

    def delete(self, request, pk, format=None):
        return self.destroy(request, pk)


class DeviceModelViewAll(generics.ListCreateAPIView, generics.ListAPIView):
    serializer_class = deviceSerializer
    queryset = DeviceModel.objects.all()
    paganation_class = CustomPagination
