Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================================== RESTART: C:\Users\Daisy\AppData\Local\Programs\Python\Python39\ThinkStats2.py\code\nsfg.py =====================================
(13593, 244)
All tests passed.
>>> import nsfg
>>> df=nsfg.ReadFemPreg()
d
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
>>> pregordr=df['pregordr']
>>> pregordr
0        1
1        2
2        1
3        2
4        3
        ..
13588    1
13589    2
13590    3
13591    4
13592    5
Name: pregordr, Length: 13593, dtype: int64
>>> type(pregordr)
<class 'pandas.core.series.Series'>
>>> pregordr[0]
1
>>> pregordr[1]
2
>>> pregordr[2:5]
2    1
3    2
4    3
Name: pregordr, dtype: int64
>>> pregordr=df.pregordr
>>> pregordr
0        1
1        2
2        1
3        2
4        3
        ..
13588    1
13589    2
13590    3
13591    4
13592    5
Name: pregordr, Length: 13593, dtype: int64
>>> import numpy as np
>>> np.nan/100.0
nan
>>> df.outcome
0        1
1        1
2        1
3        1
4        1
        ..
13588    1
13589    2
13590    2
13591    1
13592    1
Name: outcome, Length: 13593, dtype: int64
>>> df.columns['outcome']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df.columns['outcome']
  File "C:\Users\Daisy\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\indexes\base.py", line 4604, in __getitem__
    return getitem(key)
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
>>> df.outcome
0        1
1        1
2        1
3        1
4        1
        ..
13588    1
13589    2
13590    2
13591    1
13592    1
Name: outcome, Length: 13593, dtype: int64
>>> df.outcome.value_counts().sort_index()
1    9148
2    1862
3     120
4    1921
5     190
6     352
Name: outcome, dtype: int64
>>> df.birthwgt_lb.value_counts(sort=False)
8.0     1889
7.0     3049
9.0      623
6.0     2223
4.0      229
5.0      697
10.0     132
12.0      10
14.0       3
3.0       98
1.0       40
11.0      26
2.0       53
13.0       3
0.0        8
15.0       1
Name: birthwgt_lb, dtype: int64
>>> 