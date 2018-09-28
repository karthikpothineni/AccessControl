from ..models.accessModels import *
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ("created_at", "updated_at")

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.timezone = validated_data.get('timezone', instance.timezone)
        instance.soft_delete = validated_data.get('soft_delete', instance.soft_delete)
        instance.save()
        return instance



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ("created_at", "updated_at","password")


    def create(self, validated_data, exclude=None):
        if self.context['password']:
            validated_data['password'] = self.context['password']
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.timezone = validated_data.get('timezone',instance.timezone)
        instance.password = validated_data.get('password',instance.password)
        instance.soft_delete=validated_data.get('soft_delete',instance.soft_delete)
        instance.save()
        return instance



class UserProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductGroup
        fields = '__all__'

    def create(self, validated_data):
        return UserProductGroup.objects.create(**validated_data)



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ("created_at", "updated_at")

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.product_description = validated_data.get('product_description', instance.product_description)
        instance.soft_delete = validated_data.get('soft_delete', instance.soft_delete)
        instance.save()
        return instance



class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        exclude = ("created_at", "updated_at")

    def create(self, validated_data):
        return ProductGroup.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.group_name = validated_data.get('group_name', instance.group_name)
        instance.soft_delete = validated_data.get('soft_delete', instance.soft_delete)
        instance.save()
        return instance




class ProductOrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOrg
        fields = '__all__'

    def create(self, validated_data):
        return ProductOrg.objects.create(**validated_data)



class ProductFeatureGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductFeatureGroup
        fields = '__all__'

    def create(self, validated_data):
        return ProductFeatureGroup.objects.create(**validated_data)




class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        exclude = ("created_at", "updated_at")

    def create(self, validated_data):
        return ProductFeature.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.feature_name = validated_data.get('feature_name', instance.feature_name)
        instance.soft_delete = validated_data.get('soft_delete', instance.soft_delete)
        instance.save()
        return instance



class TokenValidationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TokenValidation
        fields = '__all__'

    def create(self, validated_data, exclude=None):
        return TokenValidation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.soft_delete=validated_data.get('soft_delete',instance.soft_delete)
        instance.save()
        return instance
