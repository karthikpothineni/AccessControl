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



class ProductViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            result = Generics.createGeneric(Product, "Product", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create products", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(Product, "Product", request, pk, "product_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve Product", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(Product, "Product", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list Products", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, pk=None):
        try:
            result = Generics.updateGeneric(Product, "Product", request, pk, "product_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Update Product", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(Product, "Product", request, pk, "product_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete Product", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################################################################################################################################


class ProductGroupViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            result = Generics.createGeneric(ProductGroup, "Product Group", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(ProductGroup, "Product Group", request, pk, "pg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(ProductGroup, "Product Group", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, pk=None):
        try:
            result = Generics.updateGeneric(ProductGroup, "Product Group", request, pk, "pg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Update Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(ProductGroup, "Product Group", request, pk, "pg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



######################################################################################################################################


class ProductFeatureViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            result = Generics.createGeneric(ProductFeature, "Product Feature", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create Product Feature", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(ProductFeature, "Product Feature", request, pk, "pf_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve Product Feature", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(ProductFeature, "Product Feature", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list Product Feature", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, pk=None):
        try:
            result = Generics.updateGeneric(ProductFeature, "Product Feature", request, pk, "pf_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Update Product Feature", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(ProductFeature, "Product Feature", request, pk, "pf_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete Product Feature", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



######################################################################################################################################


class ProductFeatureGroupViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            if 'product_group_id' in request.data and 'product_group_feature_id' in request.data:
                grp_obj = ProductGroup.objects.filter(pg_id=request.data['product_group_id'],soft_delete=False)
                if grp_obj:
                    feat_obj = ProductFeature.objects.filter(pf_id=request.data['product_group_feature_id'], soft_delete=False)
                    if feat_obj:
                        if grp_obj.values()[0]['product_id_id'] != feat_obj.values()[0]['product_id_id']:
                            return Response("Feature And Group Product Ids are different",status=status.HTTP_400_BAD_REQUEST)
                        request.data['product_id'] = grp_obj.values()[0]['product_id_id']

            result = Generics.createGeneric(ProductFeatureGroup, "Product Feature Group", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create Product Feature Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(ProductFeatureGroup, "Product Feature Group", request, pk, "pfg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve Product Feature Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(ProductFeatureGroup, "Product Feature Group", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list Product Feature Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(ProductFeatureGroup, "Product Feature Group", request, pk, "pfg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete Product Feature Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################################################################################################################################


class ProductOrgViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            result = Generics.createGeneric(ProductOrg, "Product Org", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create Product Org", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(ProductOrg, "Product Org", request, pk, "po_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve Product Org", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(ProductOrg, "Product Org", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list Product Org", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(ProductOrg, "Product Org", request, pk, "po_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete Product Org", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
