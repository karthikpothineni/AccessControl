import traceback

from rest_framework import viewsets
from ..serializers.accessSerializers import *
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
import datetime
from django.http import HttpResponse
from ..generics import Generics
import pdb



class OrganizationViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            result = Generics.createGeneric(Organization, "Organization", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to create organizations", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(Organization, "Organization", request, pk, "org_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve Organization", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(Organization, "Organization", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list Organizations", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, pk=None):
        try:
            result = Generics.updateGeneric(Organization, "Organization", request, pk, "org_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Update Organization", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(Organization, "Organization", request, pk, "org_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete Organization", status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# Healthcheck Methods
class healthcheck_view(View):
    def get(self, request):
        return HttpResponse()
