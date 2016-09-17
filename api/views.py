# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status, filters, permissions


class DjangoModelPermissionsMixin(generics.GenericAPIView):
    permission_classes = (permissions.DjangoModelPermissions,)


@api_view(('GET',))
def api_root(request, format=None):
    """

    """

    from api import urls
    from django.core.urlresolvers import RegexURLPattern, RegexURLResolver

    URL_NAMES = []
    def load_url_pattern_names(namespace, patterns):
        """Retrieve a list of urlpattern names"""
        URL_NAMES = []
        
        for pat in patterns:
            if pat.__class__.__name__ == 'RegexURLResolver':            # load patterns from this RegexURLResolver
                URL_NAMES.append(load_url_pattern_names(pat.namespace, pat.url_patterns))
            elif pat.__class__.__name__ == 'RegexURLPattern':           # load name from this RegexURLPattern
                # fully qualified pattern name :) (namespace::name)
                
                if pat.name is not None and pat.name not in URL_NAMES:
                    URL_NAMES.append((pat.name, pat.callback.__doc__))
        return (namespace, URL_NAMES)

    #root_urlconf = __import__(settings.ROOT_URLCONF)        # access the root urls.py file
    url_tree = load_url_pattern_names(None, urls.urlpatterns)   # access the "urlpatterns" from the ROOT_URLCONF

    response = {}
    for namespace_set in url_tree[1]:
        namespace = namespace_set[0]
        urls = namespace_set[1]
        namespace_urls = {}
        for ur in urls:
            if namespace:
                fqpn = '{}:{}'.format(namespace, ur[0])
                rev = ""
                try:
                    rev = reverse(str(fqpn), request=request, format=format)
                except:
                    try:
                        rev = reverse(str("api:{}".format(fqpn)), request=request, format=format)
                    except:
                        try:
                            rev = reverse(str(fqpn), request=request, format=format, kwargs={'pk':1})
                        except:
                            try:
                                rev = reverse(str("api:{}".format(fqpn)), request=request, format=format, kwargs={'pk':1})
                            except:
                                print "something went wrong.. who cares :)"
                                pass
                            pass
                        pass
                    pass

                description = "{}".format(ur[1])
                namespace_urls[rev] = description.strip()
        response[namespace] = namespace_urls

    return Response(response)

