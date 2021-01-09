from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from .schema import schema
from TonersManagement import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TonersManagement.urls')),
    path('toners/',views.Toenrs, name='toners'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls'))
]

