# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mUrWEeCTE1w_Saz3SgmtbR4Mb_AC8puH
"""

import pandas as pd
df = pd.read_csv("WHO COVID-19 cases.csv")
monaco_data = df[df["Country"] == "Monaco"]
print(monaco_data)