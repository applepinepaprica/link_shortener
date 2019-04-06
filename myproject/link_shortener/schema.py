import graphene

from graphene_django.types import DjangoObjectType

from myproject.link_shortener.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(object):
    all_links = graphene.List(LinkType)

    def resolve_all_links(self, info, **kwargs):
        return Link.objects.all()