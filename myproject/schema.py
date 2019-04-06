import graphene

import myproject.link_shortener.schema


class Query(myproject.link_shortener.schema.Query, graphene.ObjectType):
    pass


class Mutation(myproject.link_shortener.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
