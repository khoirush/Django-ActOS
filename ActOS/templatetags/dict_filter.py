# my_filters.py
# Some custom filters for dictionary lookup.
from django.template.defaultfilters import register


@register.filter(name='lookup')
def lookup(vdict, index):
    if index in vdict:
        return vdict[index]
    return ''


@register.filter(name='splitby')
def splitby(vlist, separator):
    return vlist.split(separator)
