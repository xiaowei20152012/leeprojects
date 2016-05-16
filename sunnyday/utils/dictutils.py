from django.db.models import DateTimeField
from django.db.models.fields.related import ManyToManyField
from utils.md5util import md5

def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(instance).values_list('pk', flat=True))

        elif isinstance(f, DateTimeField):
            data[f.name] = f.value_from_object(instance).strftime("%Y-%m-%d")
        else:
            data[f.name] = f.value_from_object(instance)
    return data

def get_sign(dict_user):
    sort_user = sorted(dict_user.iteritems(),key = lambda asd:asd[0],reverse = False)
    sort_str = ''
    for sort in sort_user:
        sort_str = sort_str + sort[0]+'='+sort[1]+'&'
    newstr = sort_str[:-1] +'||u9Y%)!a1z'
    return md5(str(newstr))


def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)


