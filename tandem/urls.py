from django.conf.urls import patterns, url, include
from profiles.views import UserViewSet
from simulations.views import SimresultViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'simresults', SimresultViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^noise_vs_x/', 'simulations.views.noise_vs_x', name='noise_vs_x'),
    url(r'^auth/', include('rest_framework.urls',
                       namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
)
