#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:19:03 2019

@author: hang-star
"""

from lxml import etree
text ='''
<div>
<u1>
<li class="item-0 la" name="tony"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link13.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</u1>
</div>
'''
html =etree.HTML(text)
#result = etree.tostring(html)
out = html.xpath('//li[contains(@class,"la")and @name="tony"]/a/text()')
print (out)
