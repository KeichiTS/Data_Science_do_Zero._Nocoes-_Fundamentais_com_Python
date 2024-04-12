# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:40:32 2024

@author: KeichiTS
"""
import matplotlib.pyplot as plt 
import pandas as pd

#lista de salários e tempo de experiência de cientistas de dados 

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6.0),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10), 
                        (48000, 1.9), (63000, 4.2)
                        ]

df = pd.DataFrame(salaries_and_tenures, columns = ['Salaries', 'Tenures'])

plt.scatter(df.Tenures, df.Salaries)