import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import *


#-------------------------------------------TYPES-----------------------------------------
class TonerType(DjangoObjectType): 
    class Meta:
        model =  Toner 

class DirectionType(DjangoObjectType):
    class Meta:
        model = Direction

class CustomerType(DjangoObjectType): 
    class Meta:
        model = Customer

class ReleaseVoucherType(DjangoObjectType):
    class Meta:
        model = ReleaseVoucher 
    
class ConsumptionType(DjangoObjectType):
    class Meta:
        model = Consumption

#-------------------------------------------END-TYPES-------------------------------------

#-------------------------------------------QUERIES---------------------------------------
class Query(ObjectType):
    toner = graphene.Field(TonerType, id=graphene.Int())
    direction = graphene.Field(DirectionType, id=graphene.Int())
    customer = graphene.Field(CustomerType, id=graphene.Int())
    release_voucher = graphene.List(ReleaseVoucherType, id=graphene.Int())
    consumption = graphene.List(ConsumptionType, id = graphene.Int())

    toners = graphene.List(TonerType)
    directions = graphene.List(DirectionType)
    customers = graphene.List(CustomerType)
    release_vouchers = graphene.List(ReleaseVoucherType)
    consumptions = graphene.List(ConsumptionType)


    #TonerTyple Resolver ------------------------------
    def resolve_toner(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Toner.objects.get(pk=id)
        return None


    def resolve_toners(self, info, **kwargs):
        return Toner.objects.all()

    #DirectionTyple Resolver --------------------------
    def resolve_direction(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Direction.objects.get(pk=id)
        return None


    def resolve_directions(self, info, **kwargs):
        return Direction.objects.all()


    #DirectionTyple Resolver ----------------------------
    def resolve_release(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return ReleaseVoucher.objects.get(pk=id)
        return None


    def resolve_releases(self, info, **kwargs):
        return ReleaseVoucher.objects.all()

    #CustomerTyple Resolver ------------------------------
    def resolve_customer(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Customer.objects.get(pk=id)
        return None


    def resolve_customers(self, info, **kwargs):
        return Customer.objects.all()


     #ConsumptionTyple Resolver ------------------------------
    def resolve_consumption(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Consumption.objects.get(pk=id)
        return None


    def resolve_consumption(self, info, **kwargs):
        return Consumption.objects.all()