# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:11:00 2018

@author: MIKE
"""

import pandas as pann
dt = pann.read_html('https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=en&country=US')
print(dt)