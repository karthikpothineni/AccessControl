import hashlib

from rest_framework import viewsets
from ..serializers.accessSerializers import *
from rest_framework.response import Response
from rest_framework import status
from ..generics import Generics
import string, random
import pdb


class UserViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        try:
            if 'password' in request.data:
                request.data['password'] = hashlib.md5(request.data['password'].encode('utf-8')).hexdigest()
            result = Generics.createGeneric(User, "User", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create users", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(User, "User", request, pk, "id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve user", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(User, "User", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list users", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, *args, pk=None):
        try:
            if 'password' in request.data:
                request.data['password'] = hashlib.md5(request.data['password'].encode('utf-8')).hexdigest()
            result = Generics.updateGeneric(User, "User", request, pk, "id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Update User", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(User, "User", request, pk, "id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete User", status=status.HTTP_500_INTERNAL_SERVER_ERROR)




    @staticmethod
    def get_features(request, *args):
        try:
            result_dict = dict()
            if 'token' not in request.data:
                return Response("Please provide token in input",status=status.HTTP_400_BAD_REQUEST)

            token_obj = TokenValidation.objects.filter(token_md5=request.data['token'],soft_delete=False)
            if not token_obj:
                return Response("Please provide valid token",status=status.HTTP_400_BAD_REQUEST)

            user_obj = User.objects.filter(email=token_obj.values()[0]['email'],soft_delete=False)
            if user_obj:
                user_map_obj = UserProductGroup.objects.filter(user_id_id=user_obj.values()[0]['id'])
                if user_map_obj:
                    product_feat_grp_map_obj = ProductFeatureGroup.objects.filter(product_group_id__in=user_map_obj.values('prod_group_id'))
                    if product_feat_grp_map_obj:
                        prod_feat_obj = ProductFeature.objects.filter(pf_id__in=product_feat_grp_map_obj.values('product_group_feature_id'))
                        result_dict['permissions'] = prod_feat_obj.values_list('feature_name', flat=True)
                        return Response(result_dict,status=status.HTTP_200_OK)
                    else:
                        return Response("No Features are present for user",status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("No Mapping present for user",status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("User with respective token doesnot exist",status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response("Unable to get features", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


##################################################################################################################################



class LoginViewSet(viewsets.ModelViewSet):

    @staticmethod
    def login(request, *args):
        try:
            user_info = dict()
            if 'email' not in request.data or 'password' not in request.data:
                return Response("Please provide email and password",status=status.HTTP_400_BAD_REQUEST)

            password = hashlib.md5(request.data['password'].encode('utf-8')).hexdigest()
            user_obj = User.objects.filter(email=request.data['email'],soft_delete=False)
            if not user_obj or user_obj.values()[0]['password'] != password:
                return Response("Invalid credentials",status=status.HTTP_403_FORBIDDEN)

            token = hashlib.md5((request.data['email']+request.data['password']).encode('utf-8')).hexdigest()+LoginViewSet.id_generator()
            user_info['email'] = user_obj.values()[0]['email']
            user_info['token_md5'] = token
            token_obj = TokenValidation.objects.filter(email=user_obj.values()[0]['email'],soft_delete=False)
            token_obj.update(soft_delete=True)
            serializer = TokenValidationSerializer(data=user_info)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response("Unable to login", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @staticmethod
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))



######################################################################################################################################


class UserProductGroupViewSet(viewsets.ModelViewSet):

    def create(self, request, *args):
        if 'user_id' in request.data and 'prod_group_id' in request.data:
            user_obj = User.objects.filter(id=request.data['user_id'],soft_delete=False)
            if user_obj:
                grp_obj = ProductGroup.objects.filter(pg_id=request.data['prod_group_id'], soft_delete=False)
                if grp_obj:
                    request.data['product_id'] = grp_obj.values()[0]['product_id_id']
                    user_map_obj = UserProductGroup.objects.filter(user_id_id=request.data['user_id'], product_id_id=grp_obj.values()[0]['product_id_id'])
                    if user_map_obj:
                        return Response("User already mapped to product group for this product",status=status.HTTP_400_BAD_REQUEST)

                    prod_org_obj = ProductOrg.objects.filter(product_id_id=grp_obj.values()[0]['product_id_id'])
                    if prod_org_obj:
                        if user_obj.values()[0]['organization_id'] != prod_org_obj.values()[0]['org_id_id']:
                            return Response("User organization does not match with product organization", status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response("Product And Organization not mapped",status=status.HTTP_400_BAD_REQUEST)


        try:
            result = Generics.createGeneric(UserProductGroup, "User Product Group", request)
            return Response(result.data,result.status_code)

        except:
            return Response("Unable to create User Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, *args, pk=None):
        try:
            result = Generics.retrieveGeneric(UserProductGroup, "User Product Group", request, pk, "upg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to retrieve User Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request, *args):
        try:
            result = Generics.listGeneric(UserProductGroup, "User Product Group", request)
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to list User Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def destroy(self, request, *args, pk=None):
        try:
            result = Generics.destroyGeneric(UserProductGroup, "User Product Group", request, pk, "upg_id")
            return Response(result.data,result.status_code)
        except:
            return Response("Unable to Delete User Product Group", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

