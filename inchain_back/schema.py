import graphene

from cryptos.schema import Query as CryptosQuery, Mutation as CryptosMutation

class Query(CryptosQuery, graphene.ObjectType):
    pass

class Mutation(CryptosMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)