import graphene

from graphene_django.types import DjangoObjectType

from myproject.link_shortener.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(object):
    link = graphene.Field(LinkType,
                              id=graphene.Int(),
                              shortLink=graphene.String(),
                              fullLink=graphene.String())

    all_links = graphene.List(LinkType)

    def resolve_all_links(self, info, **kwargs):
        return Link.objects.all()

    def resolve_link(self, info, **kwargs):
        id = kwargs.get('id')
        shortLink = kwargs.get('shortLink')
        fullLink = kwargs.get('fullLink')

        if id is not None:
            return Link.objects.get(pk=id)

        if shortLink is not None:
            return Link.objects.get(short_link=shortLink)

        if fullLink is not None:
            return Link.objects.get(full_link=fullLink)

        return None