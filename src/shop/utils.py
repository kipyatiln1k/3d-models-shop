from django.db.models import QuerySet
from mdls.models import Mdl


def filter_by_tags(qs, tags) -> QuerySet:
    return sum([Mdl.objects.get(tags__contains=tag) for tag in tags])