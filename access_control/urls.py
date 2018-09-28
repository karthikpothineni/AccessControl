from django.conf.urls import url, include
from .views.organizationViews import *
from .views.userViews import *
from .views.productViews import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/organization', OrganizationViewSet ,base_name='organizations')
router.register(r'api/v1/user', UserViewSet ,base_name='user')
router.register(r'api/v1/product', ProductViewSet ,base_name='product')
router.register(r'api/v1/product-group', ProductGroupViewSet ,base_name='product-group')
router.register(r'api/v1/product-feature', ProductFeatureViewSet ,base_name='product-feature')
router.register(r'api/v1/product-feature-group', ProductFeatureGroupViewSet ,base_name='product-feature-group')
router.register(r'api/v1/product-org', ProductOrgViewSet ,base_name='product-org')
router.register(r'api/v1/user-product-group', UserProductGroupViewSet ,base_name='user-product-group')


urlpatterns = [
    url(r'^api/v1/login', LoginViewSet.as_view({ 'post': 'login'}), name='login'),
    url(r'^api/v1/get-features', UserViewSet.as_view({ 'post': 'get_features'}), name='get_features'),
    url(r'^api/v1/health',  healthcheck_view.as_view()),
    url(r'^', include(router.urls)),
]
