from __future__ import unicode_literals

from django.db import models
from .base import BaseModel


class Organization(BaseModel):

    org_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    currency = models.CharField(max_length=10, default='USD')
    timezone = models.CharField(max_length=100, default='UTC')

    class Meta(BaseModel.Meta):
        app_label = 'access_control'
        db_table = 'organizations'
        unique_together = [("name", "country")]

    def __str__(self):
        return self.name




class User(BaseModel):

    id = models.AutoField(primary_key=True, auto_created=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    last_name = models.CharField( max_length=100)
    first_name = models.CharField( max_length=100)
    organization = models.ForeignKey(Organization, db_column='organization', to_field='org_id')
    timezone = models.CharField(max_length=100, default='UTC')
    is_admin = models.BooleanField(default=False)

    class Meta:
        app_label = 'access_control'
        db_table = 'users'

    def __str__(self):
        return self.email



class Product(BaseModel):

    product_id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, unique=True)
    product_description = models.CharField(max_length=1000)

    class Meta:
        app_label = 'access_control'
        db_table = 'products'

    def __str__(self):
        return self.name



class ProductGroup(BaseModel):
    pg_id = models.AutoField(primary_key=True, auto_created=True )
    product_id = models.ForeignKey(Product, to_field='product_id')
    group_name = models.CharField(max_length=100)

    class Meta:
        app_label = 'access_control'
        db_table = 'product_group'
        unique_together = [("product_id", "group_name")]

    def __str__(self):
        return self.group_name



class ProductFeature(BaseModel):
    pf_id = models.AutoField(primary_key=True, auto_created=True)
    product_id = models.ForeignKey(Product, to_field='product_id')
    feature_name = models.CharField(max_length=100)

    class Meta:
        app_label = 'access_control'
        db_table = 'product_features'
        unique_together = [("product_id", "feature_name")]

    def __str__(self):
        return self.feature_name




class ProductOrg(models.Model):
    po_id = models.AutoField(primary_key=True, auto_created=True)
    product_id = models.ForeignKey(Product, to_field='product_id')
    org_id = models.ForeignKey(Organization, to_field='org_id')

    class Meta:
        app_label = 'access_control'
        db_table = 'product_org_map'
        unique_together = [("product_id", "org_id")]

    def __str__(self):
        return str(self.po_id)




class ProductFeatureGroup(models.Model):
    pfg_id = models.AutoField(primary_key=True, auto_created=True)
    product_group_id = models.ForeignKey(ProductGroup, to_field='pg_id')
    product_group_feature_id = models.ForeignKey(ProductFeature, to_field='pf_id')
    product_id=models.ForeignKey(Product, to_field='product_id',null=True,blank=True)

    class Meta:
        app_label = 'access_control'
        db_table = 'product_feature_group_map'
        unique_together = [("product_group_id", "product_group_feature_id")]

    def __str__(self):
        return str(self.pfg_id)



class UserProductGroup(models.Model):
    upg_id = models.AutoField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, to_field='id')
    prod_group_id = models.ForeignKey(ProductGroup, to_field='pg_id')
    product_id = models.ForeignKey(Product, to_field='product_id')

    class Meta:
        app_label = 'access_control'
        db_table = 'userproductgroup'
        unique_together = [("user_id","prod_group_id")]

    def __str__(self):
        return str(self.upg_id)


class TokenValidation(BaseModel):
    token_id = models.AutoField(primary_key=True, auto_created=True )
    email = models.EmailField()
    token_md5 = models.CharField(max_length=100)


    class Meta:
        app_label = 'access_control'
        db_table = 'token_validation'

    def __str__(self):
        return str(self.token_id)



