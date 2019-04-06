import graphene

import myproject.link_shortener.schema


class Query(myproject.link_shortener.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)