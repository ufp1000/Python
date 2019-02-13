# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:39:36 2018

@author: Rahul.Mishra1
"""

import cx_Oracle
con = cx_Oracle.connect('apps/apps@ussecvlfh496buz.ey.net:1521/VIS')
                 
ver = con.version.split(".")
print(ver)
              
con.close()