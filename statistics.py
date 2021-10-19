Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\Daisy\AppData\Local\Programs\Python\Python39\ThinkStats2.py\code\nsfg.py
(13593, 244)
All tests passed.
>>> import nsfg
>>> df=nsfg.ReadFemPreg()
>>> df
       caseid  pregordr  howpreg_n  ...  sest  cmintvw  totalwgt_lb
0           1         1        NaN  ...     9      NaN       8.8125
1           1         2        NaN  ...     9      NaN       7.8750
2           2         1        NaN  ...    12      NaN       9.1250
3           2         2        NaN  ...    12      NaN       7.0000
4           2         3        NaN  ...    12      NaN       6.1875
...       ...       ...        ...  ...   ...      ...          ...
13588   12571         1        NaN  ...    78      NaN       6.1875
13589   12571         2        NaN  ...    78      NaN          NaN
13590   12571         3        NaN  ...    78      NaN          NaN
13591   12571         4        NaN  ...    78      NaN       7.5000
13592   12571         5        NaN  ...    78      NaN       7.5000

[13593 rows x 244 columns]
>>> df.columns
Index(['caseid', 'pregordr', 'howpreg_n', 'howpreg_p', 'moscurrp', 'nowprgdk',
       'pregend1', 'pregend2', 'nbrnaliv', 'multbrth',
       ...
       'laborfor_i', 'religion_i', 'metro_i', 'basewgt', 'adj_mod_basewgt',
       'finalwgt', 'secu_p', 'sest', 'cmintvw', 'totalwgt_lb'],
      dtype='object', length=244)
>>> df.columns[1]
'pregordr'
>>> df.columns[0]



