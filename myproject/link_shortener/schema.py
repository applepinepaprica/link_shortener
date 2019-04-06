import graphene

from graphene_django.types import DjangoObjectType

from myproject.link_shortener.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(object):
    link = graphene.Field(LinkType,
                          id=graphene.Int(),
                          short_link=graphene.String(),
                          full_link=graphene.String())

    all_links = graphene.List(LinkType)

    def resolve_all_links(self, info, **kwargs):
        return Link.objects.all()

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
