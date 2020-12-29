# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:53:09 2020

@author: Hadi Hassan
"""

import Web_Glassdoor_Scraper as gs
import pandas as pd
path ="C:/Users/Hadi Hassan/Desktop/salary_project/chromedriver" 

df = gs.get_jobs('data scientist',15,False,path,15)
