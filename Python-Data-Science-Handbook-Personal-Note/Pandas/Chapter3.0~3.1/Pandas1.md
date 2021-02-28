# Pandas的各種用法 - 讀書筆記本 - Python Data Science Handbook - Python數據科學 - Pandas 中的DataFrame 和 Series 介紹與基本數據處理使用- 筆記#8





## 3.0章使用Pandas進行數據處理 Data Manipulation with Pandas






### 1. Pandas 是什麼?   

+ 重要觀念: 它提供了對於DataFrame高效的實現
+ DataFrame: 本質上為一個具有附加行和列標籤的多維數組合，而且具有異質類型和(或)缺失值班，除了對於標籤資料擁有方便的存儲接口味，它還具有非常強大的數據操作能力，像是用戶習慣的資料框架和表格程序





### 2. NumPy 和解Pandas 的關係比較 

+ 關係: Pandas 為在NumPy基礎上構建的第三方庫
+ NumPy的ndarray缺點: 當需要更靈活的應用時，就不太行了
  + 幫數據提供標籤詩，處理缺失值等等
  + 對數據進行的處理超過廣播(Broadcasting)的範疇時候，像是分組、數據透視等等
 + 解決方法: Pandas提供了Series和DataFrame的功能力，在NumPy的基礎上提供了上面的那些數據操作密集，這樣可以減少許多數據科學在處理數據的時間





### 3. 安裝和使用Pandas

+ Pandas 的原碼是由C語言和Cython所編寫的

+ 載入Pandas套件數，並查看版本資訊

```Python
import pandas as pd

pd.__version__
```
```
'1.0.5'
```





### 提醒 - 內建的幫助文檔

+ 檢視Pandas命名空間的所有內容

```Python
pd.<Tab鍵>
```
+ 顯示Pandas的內建文件

```Python
pd?
```





## 3.1章 Pandas 對象介紹 - Introducing Pandas Objects





**重要觀念**

可以把Pandas的物件(Objects)當成是NumPy結構化數組的升級版本，它有一個很有用的方式子，就是它的行和列可以使用標籤來指定，對於數據處理上幫了一個很大的忙忙，而NumPy則是只能使用數據的位置序號來指定



+ 導入NumPy和Pandas套件

```Python
import numpy as np
import pandas as pd

```





### 1. Pandas 的Series物件(對象)  The Pandas Series Objects

+ Series: 為一個一維帶索引序號的數組，可以透過列表或數組構建

```Python
data = pd.Series([2.0, 2.5, 3.0, 3.5, 4.0])
data

```

**執行結果**

```
0    2.0
1    2.5
2    3.0
3    3.5
4    4.0
dtype: float64
```

+ 結果: Series封裝了一個值的序列和一個索引號的序列表，可以透過values和index屬性訪問



+ values屬性: 結果為NumPy數組

```Python
## 元素值
data.values
```

**執行結果**

```
array([2. , 2.5, 3. , 3.5, 4. ])
```



+ index是一個類似於數組的對象徵，它的類型是pd.Index

```Python
## 索引
data.index
```

**執行結果**

```
RangeIndex(start=0, stop=5, step=1)
```



+ 和NumPy數組一樣，可以透過Python中括號填入對應的索引號來獲取數據值

```Python
data[2]
```
**執行結果**

```
3.0
```



```Python
data[1:4]
```

**執行結果**

```
1    2.5
2    3.0
3    3.5
dtype: float64
```





### 2. Series作為通用數組 Series As Generalized NumPy Array





+ 重要觀念

在前面提到的用法中，Series對象(Objects)和一維NumPy數組看起來是可以互換的概念，那基本上它們的差別在於索引的存在形式:

  + NumPy數組具有隱式定義(Implicitly defined)的整數索引值，用來訪問值
  + 而Pandas系列則具有與訪問值相關聯的顯式定義(Explicitly defined)索引值

  

**顯式定義的索引方式提供了Series對象額外的能力**  






+ 舉例: 索引值不用一定要是整數據，可以使用任何需要的數據類型來定義索引，像是使用字符串來作為索引

```Python
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





然後跟預期的一樣，透過相應的索引值來訪問數據值

```Python
## 查看索引序號為c的值
data['c']
```

**執行結果**

```
0.6
```





也可以使用非連續或非序列的索引值

```Python
data = pd.Series([0.2, 0.4, 0.6, 0.8, 1], index = [2, 6, 3, 7, 8])

data
```

**執行結果**

```
2    0.2
6    0.4
3    0.6
7    0.8
8    1.0
dtype: float64
```





```Python
## 訪問索引序號為7的值
data[7]
```

**執行結果**

```
0.8
```



### 3. Series作為特殊的字典





**重要觀念**

作者認為我們可以將Pandas的Series當成是Python字典的特殊情況



#### Python Dictionary vs Pandas Series

+ Python Dictionary: 將任意的關鍵字key和任意的值對應起來
+ Pandas Series: 將特定類型的關鍵字key和特定類型的值value對應起來





Pandas Series這種靜態類型非常重要，像是NumPy數組的靜態類型，它能提供編譯好的程式碼，這樣性能上比Python list 操作更好，而Pandas Series也能提供編譯好的程式碼，比Python Dictionary性能表現上更好



#### 實作


Series-as-dictionary這個概念可以更清楚地比喻為使用一個Python字典來創建一個Series

```Python
city_population_dict = {'HsinChu': 534262,
'Taipei': 612450, 
'Taichung': 520468,
'Kaohsiung': 642836,
'Hualien': 264186,}

population_series = pd.Series(city_population_dict)
```





預設的情況下，會根據排序關鍵字來創建Series，接著就可以使用標準的Python字典語法來訪問值了

```Python
population_series['HsinChu']
```

**執行結果**

```
534262
```

Series可以支援數組(array-style)的操作方式，像是對字典進行切片(Slicing)，而這是Python Dictionary沒辦法做到的

```Python
population_series['Taipei':'Kaohsiung']
```

**執行結果**

```
Taipei       612450
Taichung     520468
Kaohsiung    642836
dtype: int64
```





### 4. 創建Series對象 Constructing Series Objects


+ 構造的方式

```Python
pd.Series(data, index = index)
```





index為一個可選擇的參數據，而data可以是很多種的實體之一(也就是多種的數據集合)


+ 舉例: data可以為一個列表或NumPy數組array，而index的預設情況為整數序列

```Python
pd.Series([2, 6, 8])
```

**執行結果**

```
0    2
1    6
2    8
dtype: int64
```





data 可以是一個標量(Scalar)，這種情形下，標量的值會自動填充到序列的索引index中

```Python
pd.Series(100, index = ['Student A', 2, 'Student B', 8])
```

**執行結果**

```
Student A    100
2            100
Student B    100
8            100
dtype: int64
```





data 是一個字典的情況下，index預設為關鍵字key的排序序列

```Python
pd.Series({2: 'a', 6:'b', 8:'c'})
```

**執行結果**

```
2    a
6    b
8    c
dtype: object
```



每種情形下，index都為明確地指定索引方式，結果會根據index參數來變化
```Python
pd.Series({2: 'a', 6:'b', 8:'c'}, index = [8, 2])
```

**執行結果**

```
8    c
2    a
dtype: object
```





結果中，數值為index參數指定字典裡關鍵字key中的值




### 5. Pandas 的 DataFrame對象 The  Pandas DataFrame Object


DataFrame: Pandas 的另一種基礎數據結構，和Series一樣既可以作為更通用的NumPy數組，也可以作為一種特殊的Python字典



### 6. DataFrame作為一種通用的NumPy數組 DataFrame As A Generalized NumPy Array


**重要觀念**

+ 如果將Series比喻為一個具有靈活索引的一維數組，那DataFrame就是同時具有靈活行索引和列名稱索引的二維數組
+ 可以把DataFrame想像成一系列的Series堆疊在一起，但這些Series需擁有相同的索引序列值



這邊創建兩個Series(台灣一些城市的人口、房屋數)
```Python
## 創建兩個Series

## 人口
city_population_dict = {'HsinChu': 534262,
'Taipei': 612450, 
'Taichung': 520468,
'Kaohsiung': 642836,
'Hualien': 264186,}

populaition_series = pd.Series(city_population_dict)
print(population_series)

## 房屋數

city_house_dict = {'HsinChu': 600000,
'Taipei': 8012450, 
'Taichung': 1220468,
'Kaohsiung': 6242836,
'Hualien': 2364186,}

house_series = pd.Series(city_house_dict)
house_series

```

**執行結果**

```
HsinChu      534262
Taipei       612450
Taichung     520468
Kaohsiung    642836
Hualien      264186
dtype: int64
```



```
HsinChu       600000
Taipei       8012450
Taichung     1220468
Kaohsiung    6242836
Hualien      2364186
dtype: int64
```





使用一個字典囊括兩個Series，來創建二維對象 - DataFrame

```Python
## 結合兩個Series，並創建DataFrame

city = pd.DataFrame({'population': population_series, 'house': house_series})

city
```

**執行結果**

![image1](images\image1.PNG)



DataFrame和Series一樣有index屬性，查詢所有的索引標籤

```Python
## 查看索引值
city.index

```

**執行結果**

```
Index(['HsinChu', 'Taipei', 'Taichung', 'Kaohsiung', 'Hualien'], dtype='object')
```





由於DataFrame是二維的，所以它額外擁有一個columns屬性，它也是一個index對象，用來存放所有列的標籤

```Python
## 查看特徵欄位
city.columns

## 轉成ndarray
## city.columns.values
```

**執行結果**

```
Index(['population', 'house'], dtype='object')
```





**結論**

DataFrame可以作為二維NumPy數組的通用形式，它的行和列都具有通用的索引序列來訪問數據值




### 7. DataFrame作為特殊的字典 DataFrame As A Specialiized Dictionary

**重要觀念**

一般的字典會將一個關鍵字映射成一個對應的值value，而DataFrame將一個列標籤映射成一組對應的Series對象(Object)



像是當我們訪問house屬性，會返回一個Series對象包括所有我們放入的房屋數量值
```Python
city['house']
```

**執行結果**

```
HsinChu       600000
Taipei       8012450
Taichung     1220468
Kaohsiung    6242836
Hualien      2364186
Name: house, dtype: int64
```





### 8. 構建DataFrame對象 Constructing DataFrame Objects



+ 透過Series建立

```Python
pd.DataFrame(house_series, columns = ['house'])
```

**執行結果**

![image2](images\image2.PNG)



+ 透過字典列表
```Python
data = [{'a': i,'b': i **2} for i in range(6)]

pd.DataFrame(data)
```

**執行結果**

![image3](images\image3.PNG)





當有些關鍵字key沒有出現時候，Pandas會自動填補成NaN(不是一個數字)值

```Python

pd.DataFrame([{'a': 2, 'c': 6}, {'b': 8, 'a': 10}])

```

**執行結果**

![image4](images\image4.PNG)






+ 透過Series對象的字典
```Python
pd.DataFrame({'population': population_series, 'house': house_series})
```

**執行結果**

![image5](images\image5.PNG)






+ 透過二維NumPy數組
```Python
pd.DataFrame(np.random.rand(4, 2),
                       columns = ['test1', 'test2'], index = ['a', 'b', 'c', 'd'])
```

**執行結果**

![image6](images\image6.PNG)






+ 透過NumPy結構化數組

```Python
A = np.zeros(3, dtype = [('A', 'i8'), ('B', 'f8')])

A
```
**執行結果**

```
array([(0, 0.), (0, 0.), (0, 0.)], dtype=[('A', '<i8'), ('B', '<f8')])
```





```Python
pd.DataFrame(A)
```

**執行結果**



![image7](images\image7.PNG)



### 9. Pandas 索引對象 The Pandas Index Object


**重要觀念**

+ Series 和 DataFrame對象(Object)都具有顯式索引
+ 顯事索引可以讓使用者引用和修改數據
+ 顯式索引可以被看成是不可變數組(Immutable) 或有序集合(Ordered set) - 技術層面上說是多集(multi-set)，因為index對象裡面可能包含重複值



舉例: 這邊我們先從整數列表創建一個index
```Python
ind = pd.Index([2, 4, 5, 7, 8, 10, 18])

ind
```

**執行結果**

```
Int64Index([2, 4, 5, 7, 8, 10, 18], dtype='int64')
```



### 10. Index 為不可變數組 Index As Immutable Array


+ Index在很多地方上都像Array一樣操作密集，像是我們可以使用標準的值班Python索引符號來訪問值或切片
```Python
ind[2]
```

**執行結果**

```
5
```



+ Index對象也具有熟悉NumPy數組屬性

```Python
print(ind.size, ind.shape, ind.ndim, ind.dtype)
```

**執行結果**

```
7 (7,) 1 int64
```






+ 重要差別: Index對象和NumPy數組的差別在於Index是不可變，也就是說明，它不能透過常規方法進行修改
```Python
ind[0] = 6
```

**執行結果**

![image8](images\image8.PNG)




+ 結論: 這種不可變的特性使得多個DataFrame和數組之間共享Index更加安全，才不會因為不小心地修改到索引，而產生副作用




### Index為有序集 Index As Ordered Set

**重要觀念**

+ Pandas對象被設計來促進諸如跨數據集的聯接等的操作，而這取決於集合算術的許多方面
+ Index對象遵循Python內建的set數據結構(Set data structure)，所以可以使用熟悉的方式來計算聯集、交集合、差集和其他集合





```Python
indA = pd.Index([1, 4, 6, 7, 9, 10])
indB = pd.Index([2, 4, 6, 7, 9, 8])
```


```Python
## 交集 interesectio
indA & indB
```

**執行結果**

```
Int64Index([4, 6, 7, 9], dtype='int64')
```



```Python
## 聯集 union
indA | indB
```

**執行結果**

```
Int64Index([1, 2, 4, 6, 7, 8, 9, 10], dtype='int64')
```





```Python
## 差集合symmetric difference
indA ^ indB
```

**執行結果**

```
Int64Index([1, 2, 8, 10], dtype='int64')
```




+ 還可以透過對象方法，像是indA.intersection(indB)來進行操作 

```Python
print(indA.intersection(indB))
print(indA.union(indB))
print(indA.symmetric_difference(indB))
print(indA.difference(indB))

```

**執行結果**

```Python
Int64Index([4, 6, 7, 9], dtype='int64')
Int64Index([1, 2, 4, 6, 7, 8, 9, 10], dtype='int64')
Int64Index([1, 2, 8, 10], dtype='int64')
Int64Index([1, 10], dtype='int64')
```












































































