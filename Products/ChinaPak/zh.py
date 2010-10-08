#  FileName    : zh.py 
#  Author      : Feather.et.ELF <andelf@139.com> 
#  Created     : Fri Oct  8 22:11:04 2010 by Feather.et.ELF 
#  Copyright   : Feather Workshop (c) 2010 
#  Description : A zope.i18n normalizer for zh 
#  Time-stamp: <2010-10-08 23:49:30 andelf> 

from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implements
from plone.i18n.normalizer.base import mapUnicode

# Chinese character mapping
from .pinyin import PinYinDict as mapping

class Normalizer(object):
        """
        This normalizer can normalize any unicode string and returns a version
        that only contains of ASCII characters.
        
        Let's make sure that this implementation actually fulfills the API.
        
        >>> from zope.interface.verify import verifyClass
        >>> verifyClass(INormalizer, Normalizer)
        True
                                          """
        implements(INormalizer)
        
        def normalize(self, text, locale=None, max_length=None):
            """
            Returns a normalized text. text has to be a unicode string.
            """
            return mapUnicode(text, mapping=mapping)
        
normalizer = Normalizer()
