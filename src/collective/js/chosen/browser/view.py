#!/usr/bin/env python
# -*- coding: utf-8 -*-
__docformat__ = 'restructuredtext en'


from zope import component, interface
from zope.component import getAdapter, getMultiAdapter, queryMultiAdapter, getUtility

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from Products.ATContentTypes.interfaces.interfaces import IATContentType
from Acquisition import aq_parent
from Acquisition import aq_parent
from zope.publisher.interfaces import IPublishTraverse


import json

class IMyView(interface.Interface):
    """Marker interface"""
    def search(self):
        """."""
class MyView(BrowserView):
    """MY view doc"""
    interface.implements((IMyView, IPublishTraverse))
    template = ViewPageTemplateFile('template.pt')
    def __call__(self, **params):
        """."""
        params = {}
        return self.template(**params)
    def publishTraverse(self, request, name):
        return getattr(self, name, None) 
    def search(self):
        """."""
        term  = self.request.form.get('term', '').strip()
        if not term: return
        data = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Virgin Islands', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        results = [(a.lower(), a) 
                   for a in data 
                   if term.lower() in a.lower()]
        results.sort(key=lambda a:a[0])
        rjson = json.dumps(results) 
        self.request.response.setHeader('Content-Type', 'application/javascript')
        return rjson

# vim:set et sts=4 ts=4 tw=80:

