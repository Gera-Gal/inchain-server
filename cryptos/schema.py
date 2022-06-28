from pyexpat import model
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Crypto

class CryptoType(DjangoObjectType):
    class Meta:
        model = Crypto
        filter = '__all__'

class CryptoNode(DjangoObjectType):
    class Meta:
        model = Crypto
        filter_fields = {
            'category': ['exact'],
            'tags': ['icontains'],
        }
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    crypto = graphene.relay.Node.Field(CryptoNode)
    all_cryptos = DjangoFilterConnectionField(CryptoNode)
    '''
    all_cryptos = graphene.List(CryptoType)
    filtered_cryptos = graphene.Field(
        CryptoType,
        name=graphene.String()
    )

    def resolve_all_cryptos(root, info):
        return Crypto.objects.all()

    def resolve_filtered_cryptos(root, info, name):
        try:
            return Crypto.objects.filter(name=name)
        except Crypto.DoesNotExist:
            return None
    '''

class Mutation:
    pass