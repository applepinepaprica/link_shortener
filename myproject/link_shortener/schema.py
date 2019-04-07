import graphene

from graphene_django.types import DjangoObjectType
import string
import random

from myproject.link_shortener.models import Link, LinkInfo


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class LinkInfoType(DjangoObjectType):
    class Meta:
        model = LinkInfo


class LinkInput(graphene.InputObjectType):
    fullLink = graphene.String()


class CreateLink(graphene.Mutation):
    class Arguments:
        input = LinkInput(required=True)

    ok = graphene.Boolean()
    link = graphene.Field(LinkType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        link_instance = Link(full_link=input.fullLink)
        link_instance.short_link = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        link_instance.save()
        return CreateLink(ok=ok, link=link_instance)


class Query(graphene.ObjectType):
    link = graphene.Field(LinkType,
                          id=graphene.Int(),
                          short_link=graphene.String(),
                          full_link=graphene.String())

    all_links = graphene.List(LinkType)

    all_link_infos = graphene.List(LinkInfoType)

    @staticmethod
    def resolve_all_links(self, info, **kwargs):
        return Link.objects.all()

    @staticmethod
    def resolve_all_link_infos(self, info, **kwargs):
        return LinkInfo.objects.all()

    @staticmethod
    def resolve_link(self, info, **kwargs):
        id = kwargs.get('id')
        short_link = kwargs.get('short_link')
        full_link = kwargs.get('full_link')

        if id is not None:
            return Link.objects.get(pk=id)

        if short_link is not None:
            return Link.objects.get(short_link=short_link)

        if full_link is not None:
            return Link.objects.get(full_link=full_link)

        return None


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
