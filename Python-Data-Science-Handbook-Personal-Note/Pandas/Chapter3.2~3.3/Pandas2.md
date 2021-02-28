# Pandas的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - Series 和 DataFrame的數據索引(Indexing)和選擇(Selection) - Pandas 中保留索引和對齊索引的操作 - 筆記#9



## 3.2 章 數據索引和選擇 Data Indexing and Selection


### 前言

之前我們學習過各種在 NumPy 數組中獲得、設定和修改元素或子數組的方法，包含:

+ 索引 indexnig - e.g. arr[4, 2]
+ 切片 slicing - e.g. arr[:, [6:8]]
+ 遮罩 masking - e.g. arr[arr > 2]
+ 高級索引 fancy indexing - e.g. arr[0, [2, 6]]
+ 組合上述方法 - e.g. arr[:, [6, 8]]



這次我們要學習如何在 Pandas 中獲得和修改 Series 和 DataFrame 對象(objects)的方法



### 1. 在 Series 中選擇數據


**觀念:** Series 在很多方面都與

+ 一個一維 NumPy數組
+ 一個標準的 Python 字典

相似





#### 把 Series 看成是字典 Series as dictionary

+ 與字典(Dict)相同，Series 對象提供了關鍵字集合，來對應值集合的映射

```Python
import pandas as pd

data = pd.Series([0.2, 0.4, 0.6, 0.8, 1.0],
                               index = ['a', 'b', 'c', 'd', 'e'])


data
```
**執行結果**

```
a    0.2
b    0.4
c    0.6
d    0.8
e    1.0
dtype: float64
```





```Python
data['a']
```

**執行結果**

```
0.2
```






+ 還能使用標準的 Python 字典表達式和方法來檢查 Series 的關鍵字和值

```Python
'c' in data
```

**執行結果**

```
True
```



```Python
data.keys()
```

**執行結果**

```
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```





```Python
list(data.items())
```

**執行結果**

```
[('a', 0.2), ('b', 0.4), ('c', 0.6), ('d', 0.8), ('e', 1.0)]
```





+ Series 對象也可以使用如字典操作的方式進行元素修改，也可以跟字典一樣透過給新的關鍵字來賦值，新增一個index關鍵字來擴充 Series

```Python
data['f'] = 1.2
data['g'] = 1.4

data

```
**執行結果**

```
a    0.2
b    0.4
c    0.6
d    0.8
e    1.0
f    1.2
g    1.4
dtype: float64
```





#### 將 Series 看成是一維數組 Series as one-dimentionl array


+ Series對象建構在像字典一樣的介面上，並且提供了和 NumPy 數組機制一樣的數據選擇方法，像是切片(slices)、遮罩(masking)和高級索引(fancy indexing)

##### 顯式索引

```Python
## 顯式索引 - 指定索引值進行切片
data['a':'d']
```

**執行結果**

```
a    0.2
b    0.4
c    0.6
d    0.8
dtype: float64
```





##### 隱式索引

```Python
## 隱式索引
data[0:3]
```

**執行結果**

```
a    0.2
b    0.4
c    0.6
dtype: float64
```





##### 遮罩

```Python
## 遮罩
data[(data > 0.2) & (data < 1.4)]
```

**執行結果**

```
b    0.4
c    0.6
d    0.8
e    1.0
f    1.2
dtype: float64
```





##### 高級索引

```Python
## 高級索引
data[['a', 'g']]
```

**執行結果**

```
a    0.2
g    1.4
dtype: float64
```





##### 關於顯式索引和隱式索引的重要觀念:

**切片的不同**

1. 顯式索引 - 使用索引的名稱當成切片依據，結束位置的元素會包含於切片之中，ex. data['a':'d']
2. 隱式索引 - 使用元素的位置當成切片的依據，結束位置的元素不會被包含於切片之中，ex. data[0:3]





**替代的解決方法:** loc、iloc





##### 索引符號: loc、iloc和ix - Indexers: loc, iloc, and ix





**動機:** 由於上述的切片方式容易造成混亂，像是如果有一個 Series 對象稱為 data，它有顯式的整數索引，那data[1]的操作就會是顯式索引，但是data[1:3]的操作會變成是利用隱式索引


```Python
## 拿整數值當索引
data = pd.Series(['a', 'b', 'c', 'd', 'e'], index = [1, 3, 5, 7, 9])
data
```

**執行結果**

```
1    a
3    b
5    c
7    d
9    e
dtype: object
```





```Python
## 顯式索引
data[1]
```

**執行結果**

```
'a'
```



```Python
## 隱是索引
data[1:5]
```

**執行結果**

```
3    b
5    c
7    d
9    e
dtype: object
```



**解決方法:** Pandas中提供了一些特殊的索引屬性(loc、iloc、ix)來明確的指定使用哪種索引方式，它們並不是函數，而是特定的切片接口，用來訪問 Series 數據的屬性


+ loc: 此屬性允許當使用者進行索引和切片時，永遠是使用顯式索引

```Python
data.loc[1]
```

**執行結果**

```
'a'
```





```Python
data.loc[1:5]
```

**執行結果**

```
1    a
3    b
5    c
dtype: object
```





+ iloc: 此屬性允許當使用者進行索引和切片時，永遠是使用隱式索引
```Python
data.iloc[1]
```

**執行結果**

```
'b'
```



```Python
data.iloc[1:5]
```

**執行結果**

```
3    b
5    c
7    d
9    e
dtype: object
```





+ ix: 此屬性屬於 loc 和 iloc 的混合，而對於 Series 對象而言，它同等於標準的[]索引，會在後面的 DataFrame 對象中更能體現出來





**重要觀念**

Python 程式碼有一個很大的原則就是 "explicit is better than implicit"，也就是說明明確定義優於隱含意義，作者也認為 loc 和 iloc 屬性的明確定義使得程式在維護和易讀性上非常的有幫助，也就能夠避免前面混淆的情形，所以作者非常推薦使用它們來操作











### 2. 在 DataFrame 中的數據選擇





3.1 章 作者提到過 DataFrame 既像二維或結構化數組，也像是由具有共同索引值的 Series 對象組合而成的字典





#### 將 DataFrame 看成是字典






+ 我們將兩個 Series 對象組合成 DataFrame
```Python
city_population = pd.Series({'Hsinchu': 543286, 'Taipei': 612458, 'Taichung': 530456, 'Kaohsiung': 632937, 'Hualien': 264385})

city_house = pd.Series({'Hsinchu': 600000, 'Taipei': 8012450, 'Taichung': 1220468, 'Kaohsiung': 6242358, 'Hualien': 2584328})

## 組合成DataFrame
data = pd.DataFrame({'pop': city_population, 'house': city_house})

data

```

**執行結果**

![image1](images\image1.PNG)






+ 這兩個 Series 對象可以使用字典風格的關鍵字索引方式進行訪問
```Python
## 關鍵字索引方式
data['house']

```

**執行結果**

```
Hsinchu       600000
Taipei       8012450
Taichung     1220468
Kaohsiung    6242358
Hualien      2584328
Name: house, dtype: int64
```





+ 當然也可以使用屬性的方式進行訪問，但前提是列名為字串

```Python
## 屬性方式
data.house

```

**執行結果**

```
Hsinchu       600000
Taipei       8012450
Taichung     1220468
Kaohsiung    6242358
Hualien      2584328
Name: house, dtype: int64
```





+ 關鍵字索引方式和屬性方式訪問到的對象是一樣的

```Python
data.house is data['house']
```

**執行結果**

```
True
```






+ 上面的例子是可以用這種屬性的縮寫方式訪問，但是屬性的方式並不是可以一直使用的，像是如果列名不是字符串，或是和 DataFrame 中的方法名稱一樣，這樣就會沒辦法使用屬性方法，例如 DataFrame 中有 pop() 的方法，所以當使用 data.pop的時候，並不會是訪問 pop 這一列的數據

```Python
data.pop is data['pop']
```

**執行結果**

```
False
```






+ 提醒: 要盡量避免使用屬性的方式賦值，像是應該使用 data['pop'] = 10，而不是使用 data.pop = 1
+ 和 Series 一樣，可以透過一個賦值給一個新的關鍵字索引，來對 DataFrame 進行擴充
```Python
## 增加一個新的列, 記錄每個城市平均一間房子要給幾個人住
data['average'] = data['pop'] / data['house']

data

```

**執行結果**

![image2](images\image2.PNG)









#### 將DataFrame 看成二維數組





+ 透過 values 屬性來檢視 DataFrame 對象底層的數組

```Python
## 轉換成底層數組
data.values
```

**執行結果**

```
array([[5.43286000e+05, 6.00000000e+05, 9.05476667e-01],
       [6.12458000e+05, 8.01245000e+06, 7.64382929e-02],
       [5.30456000e+05, 1.22046800e+06, 4.34633272e-01],
       [6.32937000e+05, 6.24235800e+06, 1.01393896e-01],
       [2.64385000e+05, 2.58432800e+06, 1.02303191e-01]])
```






+ 透過 T 屬性將 DataFrame 中的行和列進行交換，稱為矩陣的倒置

```Python
## 倒置 - 將行和列交換
data.T
```

**執行結果**

![image3](images\image3.PNG)





**遇到的問題:**

+ 當需要對 DataFrame 對象進行索引時，因為列具有的字典關鍵字索引方式，讓我們很難像 NumPy 數組一樣簡單地處理，像是我們要獲取第一行數據

```Python
## 取得第一行數據
data.values[0]
```

**執行結果**

```
array([5.43286000e+05, 6.00000000e+05, 9.05476667e-01])
```






+ 獲取一個列

```Python
## 獲取一個列
data['pop']
```

**執行結果**

```
Hsinchu      543286
Taipei       612458
Taichung     530456
Kaohsiung    632937
Hualien      264385
Name: pop, dtype: int64
```





**解決方法:** loc、iloc、ix

+ iloc: 等於使用顯式索引，Pandas 會把 DataFrame 當成底層的 NumPy數組來處理，但行和列的索引值依然會保留於結果之中

```Python
data.iloc[:4, :2]
```

**執行結果**

![image4](images\image4.PNG)






+ loc: 等同於使用隱式索引

```Python
data.loc[:'Kaohsiung', :'house']
```

**執行結果**

![image5](images\image5.PNG)





+ ix: 為 loc 和 iloc 的混合體

提醒: ix 已經在新版的 Pandas 中被刪除了，所以會報錯喔

```Python
data.ix[:4, :'pop']
```



提醒: 在具有整數的索引情況時，ix一樣會產生前面講的混亂情況




+ 任何的 NumPy 操作都能在上面提到的索引符號中使用，像是在 loc 中結合遮罩和高級索引

```Python
## 找到average大於0.2的城市, 並顯示其'pop'和'house'列
data.loc[data.average > 0.2, ['pop', 'house']]
```

**執行結果**

![image6](images\image6.PNG)




+ 上面提到的索引方式也可用於設置或修改數據

```Python
data.iloc[1, 0] = 100

data
```

**執行結果**

![image7](images\image7.PNG)





### 3. 額外的索引規則 Additional Indexing Conventions


除了上面介紹過的，其實還有一些額外的索引規則與前面的規則不一樣，但在現實中卻也很有用


+ 索引(indexing)是根據列(columns)的，而切片(slicing)是根據行(rows)的


+ 透過行的索引值

```Python
## 透過行的索引值
data['Hsinchu':'Taichung']
```

**執行結果**

![image8](images\image8.PNG)





+ 透過行的序號

```Python
data[2:4]
```

**執行結果**

![image9](images\image9.PNG)






+ 一樣的概念，如果直接進行遮罩的操作，也會針對行而不是列


```Python
data[data.average > 0.2]
```

**執行結果**

![image10](images\image10.PNG)



這兩個規則和 NumPy 數組的規則是一樣的，但和 Pandas 風格卻不太一致





## 3.3 章 在 Pandas 中操作數據 - Operating On Data In Pandas






### 前言

+ NumPy 有一項關鍵要素在於它能夠迅速進行逐個元素計算，包含基礎數學運算(加法、減法、乘法等)和更複雜的計算(三角函數、冪指函數、對數函數等)，而這個關鍵能力就是來自 ufuncs，而 Pandas 當然也繼承了這項能力





### Ufuncs: Pandas vs NumPy


**Pandas 擁有一些 NumPy 不具有的特性**


+ 對於一元運算(如取負和三角函數): 運算結果中保留原來的 index 和 columns 標籤
+ 對於二元運算(如加法和乘法): 在運算結果之中對數據集進行索引對齊操作


有了這兩項特性，使 Pandas 能夠在進行數據操作後保留數據原本的訊息，而不具備這兩個特性的 NumPy，容易在不同數據集操作時和需要保留原數據訊息的狀況下出錯



## 1. Ufuncs: 保留索引 - Ufuncs: Index Preservation


**重要觀念**

Pandas 是設計來和 NumPy 一起進行工作的，所以任何的 NumPy ufuncs 都能在 Pandas 的 Series 和 DataFrame 對象中使用


+ 構建一個簡單的Series和DataFrame對象


```Python
## 導入所需的套件
import pandas as pd
import numpy as np
```





```Python
## 構建一個Series, 裡面的元素從1到50中隨機取六個數
rng = np.random.RandomState(6)
series_obj = pd.Series(rng.randint(0, 50, 6))

series_obj
```

**執行結果**

```
0    10
1     9
2    35
3    20
4    42
5    45
dtype: int32
```





```Python
## 構建一個3X5的DataFrame, 並隨機從0到50取數填入
df = pd.DataFrame(rng.randint(0, 50, (3, 5)), columns = ['A', 'B', 'C', 'D', 'E']

)

df
```

**執行結果**

![image11](images\image11.PNG)





+ 進行一元ufuncs運算 - 產生一個Pandas對象，並保留索引

```Python
## 計算指數函數
np.exp(series_obj)
```

**執行結果**

```
0    2.202647e+04
1    8.103084e+03
2    1.586013e+15
3    4.851652e+08
4    1.739275e+18
5    3.493427e+19
dtype: float64
```




+ 複雜的計算

```Python
## 對df進行複雜的運算
np.sin(df * np.pi / 6)
```

**執行結果**

![image12](images\image12.PNG)





前面單元提到過的ufuncs方法都能依照這樣的操作方式進行計算喔









### 2. Ufuncs: 索引對齊 - Ufuncs: Index Alignment





針對兩個 Series 或 DataFrame 進行二元運算時，Pandas會在計算過程中將兩個數據集的索引進行對齊的操作，這對於要處理不完整數據集的狀況下非常方便

#### Series的對齊 - Index Alignment In Series


+ 假設我們要結合兩個不同的數據集，它們分別取得城市中的人口數和房屋數

```Python
## 構建一個Series(人口數據集)
ciity_population = pd.Series({'Hsinchu': 534266, 'Taipei': 632450, 'Taichung': 560266}, name = 'pop')

## 構建一個Series(房屋數據集)
ciity_house = pd.Series({'Taipei': 8212456,  'Taichung': 1420566, 'Kaohsiung': 6842738 }, name = 'house')
```





+ 將人口數除以房屋數，得到各城市中每棟房子應該要容納多少人

```Python
city_population / city_house
```

**執行結果**

```
Hsinchu      0.905477
Taipei       0.076438
Taichung     0.434633
Kaohsiung    0.101394
Hualien      0.102303
dtype: float64
```






+ 結果中的索引會包含兩個數據集的聯集，可以透過標準的Python集合計算獲得

```Python
city_population.index | city_house.index
```

**執行結果**

```
Index(['Hsinchu', 'Taipei', 'Taichung', 'Kaohsiung', 'Hualien'], dtype='object')
```






+ 兩個不同的數據集彼此不存在的元素都會被設置成 NaN (非數值)，也就是 Pandas 標注缺失值的方式
+ 索引的對齊方法使用在任何Python內建的算數計算上，任何缺失值都會被設置成 NaN

```Python
x = pd.Series([1, 3, 5, 7], index = [0, 1, 2, 3])
y = pd.Series([2, 4, 6, 8], index = [0, 2, 3, 4])
x + y
```

**執行結果**

```
0     3.0
1     NaN
2     9.0
3    13.0
4     NaN
dtype: float64
```





+ 如果設置為 NaN 值並不是我們想要的結果，可以使用相對應的ufuncs函數來計算，然後於函數中設置相對應的填充值參數，像是使用 A.add(B) 和 A + B 是一樣的，但是可以使用額外的參數來設定缺失值的替換值，像是下面的例子中，我將替換值設置為0，也就是只要在相加的過程中有一方沒有這個元素就用0來當它的值，像是:
```Python
x.add(y, fill_value = 0)
```

**執行結果**

```
0     3.0
1     3.0
2     9.0
3    13.0
4     8.0
dtype: float64
```





#### DataFrame的對齊索引 - Index Alignment In DataFrame

+ DataFrame: 類似於前面的對齊方式，但對齊的方式會同時在列和索引(行)展現

```Python
## 構建一個 3 X 3 的df, 隨機從0到50取數
x = pd.DataFrame(rng.randint(0, 50, (3, 3)),
                                  columns = list('ABC'))
                                  
x
```

**執行結果**

![image13](images\image13.PNG)

```Python
## 構建一個 4 X 4 的df, 隨機從0到50取數
y = pd.DataFrame(rng.randint(0, 50, (4, 4)),
                                  columns = list('BACD'))
                                  
y
```

**執行結果**

![image14](images\image14.PNG)





```Python
## 拿3 X 3的df 去加油4 X 4的df
x + y
```

**執行結果**

![image15](images\image15.PNG)





+ 注意: 不論索引在原數據集的順序，都不會影響結果中索引對齊的情況


+ 和Series相同，可以使用ufuncs函數來替換標準運算操作，使用fill_value參數來替代NaN填入我們定義的值，下面的例子中先將A堆疊(stack())，也就是取所有值相加，然後再計算平均值(mean())並填入缺失值


```Python
fill = x.stack().mean()
x.mul(y, fill_value = fill)
```

**執行結果**

![image16](images\image16.PNG)






+ 表格中為Python的運算操作對應Pandas的函數方法

|Python 操作符|Pandas 方法|
|---|---|
|+|add()|
|-|sub, subtract()|
|*|mul(), multiply|
|/|truediv(), div(), divide()|
|//|floordiv()|
|%|mod()|
|**|pow()|




### 3. Ufuncs: DataFrame和Series之間的操作 -Operations Between DataFrame and Series

+ 當在DataFrame和Series之間進行操作時，索引(行)和列 的對齊機制依然會存在，在DataFrame和Series間操作，就像是在一維和二維數組之間操作
+ 範例: 二維數組和它其中一行的差

```Python
## 構建一個3 X 5的二維數組
x = rng.randint(0, 10, size = (3, 5))

x
```

**執行結果**

```
array([[9, 1, 2, 2, 9],
       [5, 4, 1, 6, 3],
       [1, 4, 9, 8, 4]])
```





```Python
## 將x中的所有行減掉第二行的數據
x - x[1]
```

**執行結果**

```
array([[ 4, -3,  1, -4,  6],
       [ 0,  0,  0,  0,  0],
       [-4,  0,  8,  2,  1]])
```



+ 根據NumPy的廣播規則，二維數組的每一行都會減掉它的第二行
+ 預設的狀況下，Pandas也是採用這種廣播機制


```Python
df = pd.DataFrame(x, columns = list('ABCDE'))
print(df)

## df中的所有行減掉其第二行
df - df.iloc[1]
```

**執行結果**

![image17](images\image17.PNG)





+ 如果想根據列來進行減法，就要使用相對應的ufuncs函數，並設定axis參數

```Python
## 依照列來進行減法
df.subtract(df['C'], axis = 0)
```

**執行結果**

![image18](images\image18.PNG)






+ 上述的DataFrame和Series操作，都會自動對計算的數據集進行索引對齊配置

```Python
## 取第一行的B、D列
half_row = df.iloc[0, 1::2]

half_row
```

**執行結果**

```
B    1
D    2
Name: 0, dtype: int32
```





```Python
df - half_row
```

**執行結果**

![image19](images\image19.PNG)



### 結論

這章節介紹了保留和對齊索引(行)與列的方法，表示了在Pandas進行數據操作時會保留數據的上下文資訊，這可以避免掉使用NumPy數組操作時，可能會因為未對齊數據和異構數據所發生的錯誤






