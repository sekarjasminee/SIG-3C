# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:46:35 2019

@author: User
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
sf.bbox #membaca boundary box atau batas kotak

# In[]