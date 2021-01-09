from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings 
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TonersManagement.urls')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls'))
]

