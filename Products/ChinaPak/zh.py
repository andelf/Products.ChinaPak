#  FileName    : zh.py 
#  Author      : Feather.et.ELF <andelf@139.com> 
#  Created     : Fri Oct  8 22:11:04 2010 by Feather.et.ELF 
#  Copyright   : Feather Workshop (c) 2010 
#  Description : A zope.i18n normalizer for zh 
#  Time-stamp: <2010-10-09 00:29:15 andelf> 

from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implements
from plone.i18n.normalizer.base import baseNormalize # , mapUnicode

# Chinese character mapping
from .pinyin import PinYinDict as mapping


def mapUnicode(text, mapping=()):
    """
    NOET: rewrite by andelf to insert '-' between characters or english words.
    This method is used for replacement of special characters found in a
    mapping before baseNormalize is applied.
    """
    res = []
    word = u''                          # handle english words
    for ch in text:
        ordinal = ord(ch)
        if ordinal< 127:
            word += ch
            continue
        elif word:
            res.append(word)
            word = u''
        if ordinal in mapping:
            res.append(mapping.get(ordinal))
        else:
            res.append(ch)
    res = filter(lambda u: u and not u.isspace(), res)
    # always apply base normalization
    return baseNormalize(u' '.join(res))
                                                    

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
