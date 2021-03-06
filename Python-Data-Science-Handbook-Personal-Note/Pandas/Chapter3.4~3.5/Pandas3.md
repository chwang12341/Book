# Pandas的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - 如何處理數據中的缺失值 - 筆記#10





## 3.4 章 處理缺失值 - Handiing Missing Data






### 前言

過去我們在教學資源裡面所看到的數據集，和真實世界的數據集的差別就是在真實的數據集很少是清理乾淨和同質的，很多有趣的數據集中都有缺失值，而不同數據源的數據集用來表示缺失值的方式也可能不同






### 1. 缺失數據約定的權衡取捨 - Trade-offs in Missing Data Conventions





在數據表或DataFrame中，用來標示缺失值的方案有許多種，一般來說，會圍繞在兩種策略執行:



**兩種策略**

+ 全局的遮罩 (Mask): 於遮罩方案中，遮罩層可以是一整個獨立的布林數組，或是佔數據中的一位(bit)來標示
+ 哨兵值 (Sentinel value): 於哨兵的方案中，哨兵值可以是某些特定數據的約定值，像是用-9999或是其它罕見的數值，又或是使用更通用的方式來標記，像是標記一個缺失的浮點數值為NaN (非數字)，NaN為IEEE浮點數標準的一部分


**取捨**

+ 全局的遮罩 (Mask): 獨立的遮蓋數組會需要額外的內存空間來儲存布林數組，這樣會造成容量和計算上的負荷
+ 哨兵值 (Sentinel value): 一般的哨兵值會減少有效數據的取值範圍，並且可能需要在CPU和GPU運算上使用額外的邏輯(通常還未優化)，像是NaN這種常見的特殊值，並不適用於所有的數據類型



**結論**

由於在大部分的情況下沒有通用的優選策略，所以不同的語言和系統會使用不同的約定，像是語言的用戶在每個數據類型中保留一個位(bit)作為哨兵值，用來標示缺失值，而SciDB系統使用一個額外的字節(byte)綁定在每個元素上，用來標示不可用的狀況(NA state)







### 2. Pandas中的缺失值 - Missing Data In Pandas



**筆記:**

Pandas中用來處理缺失值的方式依賴於它的NumPy套件，因此對於非浮點數類型並沒有內建的缺失值表示





#### 重要觀念: Pandas不採用第一種全局的遮罩(Mask)方案原因



**Pandas為什麼不適合採用與R語言一樣的標記缺失值方式?**

+ Pandas可以採用和R語言一樣的方式，就是在數據值中指定一位(bit)作為缺失值的標記，但是這種方式會顯得笨重，因為R中只有四種的基本數據類型，然而NumPy所支援的類型遠遠超過這個數，像是在R中只有一種整數類型，而NumPy卻支援14種不同精度、是否具有符號、大小尾編碼的整數類型
+ 保留一位(bit)作為缺失值的標記，會影響到NumPy所有類型的多種操作，基本上等於需要一套新的NumPy套件來支援這項新的操作，而且當數據類型比較小的狀況下(像是8bits的整數)，犧牲一位(bit)的作法會明顯地縮小數值範圍



**Pandas為什麼不採用遮罩方式**

+ NumPy支援遮罩，也就是一個數組中包含著分散的布林值，用來標示對應數據是"好的"還是"壞的"
+ Pandas當然也繼承了這一項特性，但是存儲、計算和維護程式上額外的需求，也使這個方案不那樣吸引人



#### 重要觀念: Pandas採用第二種策略 - 使用哨兵值標示缺失值


Pandas 選擇了第二種策略，使用哨兵值來標示缺失值，也就是現在存在的Python空值: 用來表示特殊的浮點數值NaN和Python的None對像，這種作法當然也會有缺點，後面會提到，但是這已經證明為在大部分情況下比較好的折中方法





### 3. None: Python的缺失值 - None: Pythonic missing data

+ 筆記: 第一個被Pandas使用的哨兵值(sentinel value)是None，它為Python的一個單例對象，大部分的情況下它都為Python程式碼中的缺失值標誌
+ 由於這是一個Python對象，None不可以任意地在NumPy或Pandas數組中使用，它只能在數據類型為object的數組中使用(像是Python對象所組成的數組)
```Python
## 導入所需的套件
import numpy as np
import pandas as pd
```

```Python
## 構建一個包含None的數組
x = np.array([1, None, 2 ,4])
x
```

**執行結果**



```
array([1, None, 2, 4], dtype=object)
```





+ 結果中的 dtype = object 代表NumPy數組的元素類型為Python對象，雖然這種類型的對象在某些狀況下很有用，任何的數據操作都會在Python層面進行處理，但這樣的方式會比NumPy其它的基礎類型(像是int)進行的快速操作中消耗更多的執行時間


```Python

## 比較object和int類型在數據操作上的速度
for dtype in ['object', 'int']:
    print("dtype = ", dtype)
    ## 1E6: 1乘10的6次方
    %timeit np.arange(1E6, dtype = dtype).sum()
    print()
    
```

**執行結果**

```
dtype =  object
177 ms ± 19.8 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

dtype =  int
7.26 ms ± 245 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```



+ 而且使用Python對象作為數組的數據類型，當使用聚合操作(像是sum()、min()、max()等等)時，如果遇到了None值，就會報錯

```Python
x.sum()
```

**執行結果: **會報錯



+ 結果: 報錯的原因是因為整數和None之間的加法運算是未被定義的





### 4. NaN: 缺失的數據類型 - NaN: Missing numerical data






+ NaN: 非數字的縮寫，另一種表示缺失值的方式，能被所有支援IEEE浮點數標準的系統識別


**重要觀念**

+ NumPy使用原始的浮點數類型('float64')來存儲這個數組，這代表不像上述的對象(object)類型數組
+ 作者形容NaN就像數據病毒，它會傳染給任何觸碰到它的數據，無論是哪種運算類型，NaN參與的算數計算結果都會是另一個NaN

```Python
y = np.array([2, np.nan, 6, 10])
y.dtype
```

**執行結果**

```
dtype('float64')
```





```Python
print(1 + np.nan)
print(2 + y)
```

**執行結果**

```
nan
[ 4. nan  8. 12.]
```





```Python
print(0 * np.nan)
prnit(1 * y)
```

**執行結果**

```
nan
[ 2. nan  6. 10.]
```






+ 對於數組的聚合操作也是被良好定義的，也就是不會報錯，但結果都是NaN
```Python
y.sum(), y.min(), y.max()
```

**執行結果**

```
(nan, nan, nan)
```




+ NumPy提供了一些特殊的聚合函數來忽略掉這些缺失值


```Python
np.nansum(y), np.nanmin(y), np.nanmax(y)
```

**執行結果**

```
(18.0, 2.0, 10.0)
```





**重要觀念:** NaN為一個特殊的浮點數值，對於整數、字符串和其它類型來說沒有對應的值







### 5. Pandas中的NaN和None - NaN and None in Pandas





**重要觀念: 在Pandas中的NaN和None都可以被使用，而且Pandas基本上將兩者進行一樣的處理，並可以在合適的情況下進行轉換**

```Python
pd.Series([2, np.nan, 6, None])
```

**執行結果**

```
0    2.0
1    NaN
2    6.0
3    NaN
dtype: float64
```





+ 對於那些沒有可用哨兵值的數據類型，當Pandas發現出現NA值的情況下會自動對它們進行類型轉換，像是如果我們在已存在的整數類型數組中修改其中的元素變成np.nan值，那整個整數數組就會自動向上擴展為浮點類型

```Python
x = pd.Series(range(6), dtype = 'int64')
x
```

**執行結果**

```
0    0
1    1
2    2
3    3
4    4
5    5
dtype: int64
```



```Python
x[1] = None
x
```

**執行結果**

```
0    0.0
1    NaN
2    2.0
3    3.0
4    4.0
5    5.0
dtype: float64
```



+ 結果中除了將整數類型的數組向上擴展為浮點數類型，還自動將None值改為NaN值
+ 相較於R語言那樣使用統一的NA值來標示的方法，Pandas的這種自動轉換顯得很魔術，但是依據作者的經驗這樣Pandas哨兵值+類型轉換的方式，運行很好很少造成問題
+ 圖表為Pandas對於出現NA值後向上擴展類型的規則

|類型|當NA值被存入後的類型轉換|NA 哨兵值|
|---|---|---|
|floating|No change|np.nan|
|object|No change|None or np.nan|
|integer|Cast to float64|np.nan|
|boolean|Cast to object|None or np.nan|


+ 在Pandas裡，字符串數據都是使用object類型儲存的









### 6. 操作空值 - Operating on Null Values





#### 操作空值的方法

Pandas將None和NaN當成是可以互相轉換的缺失值或空值，當然還提供了一些用來在數據集中偵測、移除和替換空值的方法:

+ isnull(): 產生一個布林遮罩數組來指示這些缺失值
+ notnull(): 與isnull()用法相反
+ dropna(): 傳回一個過濾掉缺失值版本的數據
+ fillna(): 傳回一個數據集的副本，其中的缺失值會使用另外的值替換





#### 檢測空值 - Detecting null values


+ 使用isnull和notnull來檢測，它將返回一個布林遮罩數組

```Python
data = pd.Series([2, None, 6, np.nan])
print(data)
## 檢測Null值
data.isnull()
```

**執行結果**

```
0    2.0
1    NaN
2    6.0
3    NaN
dtype: float64
```

```
0    False
1     True
2    False
3     True
dtype: bool
```




+ 我們可以透過這個方式快速地過濾出不是空值的元素，可以利用返回的布林遮罩數組當成DataFrame或Series的索引來獲得

```Python
## 找出不為null值的數據
data[data.notnull()]
```

**執行結果**

```
0    2.0
2    6.0
dtype: float64
```







+ 同樣地在DataFrame中的isnull()和notnull也會產生類似的布林遮罩數組





#### 移除掉空值 - Dropping null values

+ 使用dropna()移除掉NA值和fillna()填充NA值

+ Series
```Python
## 移除掉null值
data.dropna()
```

**執行結果**

```
0    2.0
2    6.0
dtype: float64
```



+ 對於DataFrame而言，提供了更多的選項

```Python
## 構建一個含有null值的DataFrame
df = pd.DataFrame([[2, np.nan, 6],
                  [3, 5, 8],
                  [None, 6, 8]])                                  
df
```

**執行結果**

![image2](images\image2.PNG)




+ dropna: 會移除掉出現空值的整行

```Python
## 移除空值 - 預設情況會依據行
df.dropna()
```

**執行結果**

![image3](images\image3.PNG)




+ 可以透過設定axis參數(ex. axis = 1)來依據不同維度移除空值
+ 範例: 移除掉含有空值的列

```Python
## 移除空值 - 依據列
df.dropna(axis = 'columns')
```

**執行結果**

![image4](images\image4.PNG)




+ 上述整行或整列移除掉的方法，可能會移除掉一些好的數據，我們可能需要移除掉的是那些全部都是NA值或是大部分數據為NA值的行或列，這時就可以透過設定how或thresh參數來達成，它們可以更精細地掌控移除掉的行和列要包含幾個空值

```Python
## 增加一列全為NaN
df[3] = np.nan
df
```

**執行結果**

![image5](images\image5.PNG)

**how**

+ 預設的情況下: how = 'any'，也就是有任何的空值就會被移除掉，將它改設定為: how = 'all'，就會只有那些全部都為空值的行或列會被移除掉

```Python
## 移除全部都為空值的列
df.dropna(axis = 'columns', how = 'all')
```

**執行結果**

![image6](images\image6.PNG)



**thresh**

+ 更精細的控制: thresh，它可以讓使用者指定行或列需要擁有幾個非空值數據才會被保留，其它會被移除掉

```Python
## 移除掉非空值數量少於3的行
df.dropna(axis = 'rows', thresh = 3)
```

**執行結果**

![image7](images\image7.PNG)





#### 填充空值 - Filling null values



有些情況下我們不一定想移除掉NA值，而是希望使用正確的值來替換它們，替換後的值也許是一個單一數據(ex. 0)，又或是從其它歸併或插補的正確數值，當然也可以使用前面提到的isnull遮罩來實現，但是這個需求是很常見的，所以Pandas提供了fillna()的方法，用來傳回一個替代空值後的數據集副本




+ Series
```Python
data = pd.Series([2, None, 4, np.nan, 6], index = list("ABCDE"))

data
```

**執行結果**

```
A    2.0
B    NaN
C    4.0
D    NaN
E    6.0
dtype: float64
```



```Python
## 用0替換空值
data.fillna(0)
```

**執行結果**

```
A    2.0
B    0.0
C    4.0
D    0.0
E    6.0
dtype: float64
```



+ 夠過method參數(ex. method = 'ffill')，實現向前填充的方法: 將前一個值傳到下一個值
```Python
## 向前填充
data.fillna(method = 'ffill')
```

**執行結果**

```
A    2.0
B    2.0
C    4.0
D    4.0
E    6.0
dtype: float64
```




+ method = 'bfill': 向後填充
```Python
## 向後填充
data.fillna(method = 'bfill')

```

**執行結果**

```
A    2.0
B    4.0
C    4.0
D    6.0
E    6.0
dtype: float64
```

+ DataFrame
+ DataFrame和Series類似，但是多提供了axis參數可以指定填充沿著的維度
```Python
df
```

**執行結果**

![image8](images\image8.PNG)





```Python
df.fillna(method = 'ffill', axis = 1)
```

**執行結果**

![image9](images\image9.PNG)



結果: 由於最後一行的第一個元素(df.iloc[2, 0])前面並沒有數據，所以無法進行填充







# Pandas的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - 多層次結構 - 多重索引 MultiIndex - 筆記#11


## 3.5 章 層次化索引 - Hierarchical Indexing


### 前言


從一開始到現在，我們關注在一維和二維的數據，分別存儲於Pandas的Series和DataFrame中，但很多時候我們需要超過二維來存儲更高維度的數據，也代表用來索引的關鍵字會超過1個或2個


雖然Pandas提供了Panel和Panel4D來存儲高維度的數據，但是在實務上更常被使用的方式是層次化索引(或稱多重索引) Hierarchical Indexing 來將多個索引層次的索引關鍵字結合起來成為一個索引，這種方式讓高維度的數據可以用更緊湊的方式呈現我們熟悉的一維Series和二維DataFrame


+ 導入所需的套件

```Python
## 導入所需的套件
import numpy as np
import pandas as pd


```

### 1. Series中的多重索引 - A Multiply Indexed Series

+ 問題: 使用一維Series如何是好～表示二維數據，實例上我們考慮使用一個序列的數據，每個數據元素點都有一個對應的字符串和數字關鍵字


**不優的作法 - The bad way**


+ 範例: 假設我們要瞭解城市房屋數在兩個不同時間點的數據，利用我們學過的Pandas工具，可能會想使用簡單的Python元祖(tuple)來當key

```Python
## 構建索引
index = [
    ('Hsinchu', 2020), ('Hsinchu', 2021),
    ('Taipei', 2020), ('Taipei', 2021),
    ('Taichung', 2020), ('Taichung', 2021)
]


## 數據
house = [
    52457, 57686,
    267496, 326717,
    256486, 239766
]

## 構建Series
city_house = pd.Series(house, index = index)

city_house
```

+ 這種方式可以直接於Series中對多個索引進行索引(index)或是切片(slice)
```Python
city_house[('Hsinchu', 2021):('Taichung', 2020)]
```

+ 遇到的問題: 雖然上述的方式看起來是很方便，但是如果遇到更複雜的問題可能就不好處理了，像是如果我們需要2021年全部的數據，就需要寫一段沒那麼好讀(性能也較低)的程式碼

```Python
city_house[[i for i in city_house.index if i[1] == 2021]]
```

+ 結果: 結果是正確的，但是相較於我們喜愛用的Pandas切片語句，程式碼很不易讀(可能在處理大數據上效能也不好)


**更好的方法: Pandas的多重索引 - The Better Way: Pandas MultiIndex**


+ 上述的元祖索引方式為一個初級的多重索引，Pandas MultiIndex類型提供了我們多重索引的功能，下面我們來透過元祖創建一個多重索引

```Python
## 使用tuple來構建一個多重索引
index = pd.MultiIndex.from_tuples(index)

index

```
+ 注意: MultiIndex包含多重層級的索引，像是我們例子中的多重層級索引就是城市名稱和年份，也具有多個標籤對應每個數據點


+ 使用這個多重索引 MulitiIndex 來對我們的Series對象進行重新索引，就可以看到多個層級的索引 
```Python
## 使用這個多重索引來重新索引
city_house = city_house.reindex(index)

city_house

```

+ 結果: 結果中Series的前兩列為多重索引的值，最後一列為數據值，第一列有一些數據消失了，是因為在多重索引呈現中，缺失的索引值與它前面的索引值相同


+ 跟上面的方式相比，同樣要獲取2021年的數據，只要簡單的使用Pandas的切片語法就能達成，而且性能也優化很多


```Python
## 檢視2021年的數據
print(city_house:, 2021[)

print()

## 檢視HsinChu底下的所有數據
print(city_house['Hsinchu', :])


```

+ 結果: 執行後變成了一個單一索引的數組，而且是只帶我們需要的索引


### 2. 多重索引當成額外的維度 - MultiIndex as extra dimention

上例中大家可能會注意到我們可以簡單地將數據存成一個DataFrame，城市名稱為行索引，時間(年)為列索引，而Pandas當然也有內建的機制來達到等同的效果 - unstack()


+ unstack(): 快速地將多重索引的Series轉換成普通索引的DataFrame
```Python
## Series
print(city_house)

## 轉換成DataFrame
house_df = city_house.unstack()
house_df
```


+ stack(): 提供了unstack的反向操作
```Python
## 轉換回Series
house_df.stack()

```

**疑惑: 到底為什麼我們需要使用這種層次化索引?**

+ 如我們使用多重索引來將一維Series表示成二維數據一樣，我們可以使用Series或DataFrame來表示三維或更多維度的數據
+ 在多重索引中的額外層都代表著數據集中額外的維度，因為這點我們可以靈活並詳細地呈現我們的數據


+ 範例: 我們希望多增加一列為空屋數，使用MultiIndex就能夠很簡單的添加一列
```Python
## 增加一列
house_df = pd.DataFrame({
    'house_total': city_house,
    'house_empty': [
        28796, 23768,
        82239, 97983,
        53899, 68589
    ]
})

house_df

```

+ Pandas的ufuncs功能當然也可以使用，這邊我們計算空屋的比例

```Python
## 計算兩個年份的空屋比例
house_empty_rate = house_df['house_empty'] / house_df['house_total']

## 轉換成DataFrame
house_empty_rate.unstack()
```


### 3. 創建多重索引的方法  - Methods of MultiIndex Creation

+ 第一種方式: 在Series或DataFrame的index參數中傳入一個多重列表

```Python
## DataFrame: 隨機產生一個4 X 2的正態分佈數值，並指定索引和列名
df = pd.DataFrame(np.random.rand(4, 2),
        index = [['x', 'x', 'y', 'y'], [1, 2, 1, 2]],
        columns = ['A', 'B']
        )
df

```

+ 這樣構建MultiIndex的工作會在背後自動完成


+ 第二種方式: 使用元祖做為關鍵字的字典構建出Series，Pandas也會自動識別並在預設的情況下使用MultiIndex

```Python
## 使用元祖tuple來創建Series
data = {
    ('Hsinchu', 2020): 52437,
    ('Hsinchu', 2021): 57668,
    ('Taipei', 2020): 284327,
    ('Taipei', 2021): 346517,
    ('Taichung', 2020): 52897,
    ('Taichung', 2021): 297982
}

pd.Series(data)

```




#### 顯式的MultiIndex構造器 - Explicit MultiIndex Constructors

+ 第三種方式: 使用pd.MultiIndex的構造器，像是可以使用多重列表來創建和前面一樣的MultiIndex

```Python
## array - 構建多重索引
pd.MultiIndex.from_arrays([['x', 'x', 'y', 'y'], [1, 2, 1, 2])

```


+ 第四種方式: 使用pd.MultiIndex，並使用元祖來創建一個多重索引

```Python
## tuple - 構建多重索引
pd.MultiIndex.from_tuples([('x', 1), ('x', 2), ('y', 1), ('y', 2)])

```


+ 第五種方式: 使用pd.MultiIndex，並使用笛卡爾乘積方式來創建

```Python
## Cartesian product - 構建多重索引
pd.MultiIndex.from_product([['x', 'y'], [1, 2, 3]])

```

+ 第六種方式: 直接使用MultiIndex來構建，需要傳入levels(多重列表每個層次中的索引值)參數和 codes (多重列表數據點的標籤值)
```Python
## MultiIndex - levels和codes構建多重索引
pd.MultiIndex(levels = [['x', 'y', 'z'], [1, 2]],
    codes = [[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])

```

創建Series或DataFrame構造器時，上述構建的這些對象都能當成index參數傳遞，或是使用reindex的方法提供給Series或DataFrame進行重新索引

#### 多重索引的層次名稱 - MultiIndex Level Names

+ 有時候我們需要對不同層次進行命名，就可以透過MultiIndex裡面的names參數，或是已經創建好後設置names屬性來達成

```Python
## 多層次命名
city_house.index.names = ['City', 'Year']

city_house

```

+ 筆記: 這樣的方式可以在複雜的數據集中，讓不同的索引值保有它原本的意義


#### 列的多重索引 - MultiIndex For Columns


+ 在DataFrame中行和列是完全對稱的，如前面看到的行可以有多層次的索引，列當然也可以有多層次的索引

```Python
## 構建行和列的多重索引
index = pd.MultiIndex.from_product([[2020, 2021], [1, 2]],
                              names = ['year', 'visit')
                              
columns = pd.MultiIndex.fro_product([['Ken', 'Jen', 'Cathy']], 
                           names = ['subject', 'type']
         )
         
         
## 隨機產生一個4 X 6 的數據
data = np.round(np.random.randn(4, 6), 2)

data[:, ::2] *=10
data+=40

## 構建DataFrame
hospital_data = pd.DataFrame(data, inedx = index, columns = columns)

hospital_data
```


+ 處理多維度的數據集時，MultiIndex對行和列來說都是非常方便的，上面為一個四維度的數據集，四個維度分別為目標(受試者)、量測類型、年份和訪問編號，有了這樣多重索引的DataFrame後，可以使用目標的名稱來方便地獲取此受試者的所有量測數據

```Python
## 獲取Ken的數據
hospital_data['Ken']

```

### 4. 在MultiIndex上索引和切片 - Indexing And Slicing A MultiIndex


#### Series多重索引 - Multiply Indexed Series


+ 上面的例子中房屋的多重索引Series

```Python
## 索引
index = [
    ('Hsinchu', 2020), ('Hsinchu', 2021),
    ('Taipei', 2020), ('Taipei', 2021),
    ('Taichung', 2020), ('Taichung', 2021)
]


## 數據
house = [
    52457, 57686,
    267496, 326717,
    256486, 239766
]

## 構建Series
city_house = pd.Series(house, index = index)

## 構建多重索引
index = pd.MultiIndex.from_tuples(index)

## 重新索引
city_house = city_house.reindex(index)

city_house



```


+ 使用多重索引值獲取單個元素值

```Python
## 檢索Taipei在2020的房屋數
city_house['Taipei', 2020]

```


+ MultiIndex也支援部分索引，就是只索引其中一層，結果會是另一個Series但會比原本少掉一層

```Python
## 檢索Taichung的數據
city_house['Taichung']

```

+ 只要MultiIndex是排序好的，就可以使用部分切片

```Python
## 檢索Hsinchu到Taipei的數據
city_house.loc['Hsinchu':'Taipei']

```

**重要筆記:** 由於我們範例中的多重索引並沒有排好序，Taipei跟Taichung比字母順序，前三個一樣而第四個c應該要在p前面，所以會報錯喔!!


**解決方法:** 重新排序一下即可

```Python
## 索引
index = [
    ('Hsinchu', 2020), ('Hsinchu', 2021),
    ('Taichung', 2020), ('Taichung',
    ('Taipei', 2020), ('Taipei', 2021),
]


## 數據
house = [
    52457, 57686,
    256486, 239766,
    267496, 326717,
]

## 構建Series
city_house = pd.Series(house, index = index)

## 構建多重索引
index = pd.MultiIndex.from_tuples(index)

## 重新索引
city_house = city_house.reindex(index)


## 檢索Taichung到Taipei的數據
city_house['Taichung':'Taipei']



```

+ 在有排好序的索引情況下，部分索引也能夠用在比較低層次的索引上，只要在第一個索引上傳入一個空的切片就可以了

```Python
## 查看2020年的資料
city_house[:, 2020]

```


+ 也支援其它類型的索引和選擇，像是使用布林遮罩(Mask)進行檢索

```Python
## 檢索房屋數大於26萬的數據
city_house[city_house > 260000]

```

+ 使用高級索引(Fancy Indexing)進行檢索工作

```Python
## 檢索Hsinchu和Taipei的數據
city_house[['Hsinchu', Taipei]]

```


#### DataFrame多重索引 - Multiply Indexed DataFrame

+ 前面的醫院DataFrame數據集

```Python
hospital_data
```

+ **重要觀念:** DataFrame中主要的索引是列，可以透過和上面多重索引Series一樣的方法應用到DataFrame的列上，像是透過簡單的操作獲取Ken的心律數據

```Python
## 查看Ken的心律指數
hospital_data['Ken', 'HR']

```

+ 如單一索引的方式，我們一樣能使用loc、iloc索引符
```Python
## 行和列各呈現前兩筆數據
hospital_data.iloc[:2, :2]

```

+ loc、iloc索引符號提供了一個底層二維數據的數組視圖，而且在loc或iloc中每個獨立的索引都能傳入一個多重索引的元祖來指定哪一層，像是:

```Python
## 獲取Jen的心律數據
hospital_data.loc[:, ('Jen', 'HR')]

```

+ 使用這樣的索引符號並沒有很方便，像是如果在元祖中使用切片會報一個語法錯誤

```Python
hospital_data.loc[(:, 1), (:, 'HR')]
```

**解決方法**

+ 顯式地使用Python內建的slice()函數
+ Pandas提供的更好方法 - IndexSlice對象

```Python
idx = pd.IndexSlice
## 檢索每個人每一年的第一筆心律數據
hospital_data.iloc[idx[:, 1], idx[:, 'HR']]


```

### 5. 重新排列多重索引 - Rearranging Multi-Indices

+ 使用多重索引數據的關鍵在瞭解如何有效地轉換數據
+ Pandas提供了一些操作去保留這些數據中的資訊，並根據不同目的運算操作來重新排列數據，像是前面有介紹到的stack和unstack，當然還有更多接下來會探討



#### 有序和無序的索引 - Sorted And Unsorted Indices


**重要筆記:** 索引分成有序和無序索引，無序索引會讓許多MultiIndex的切片操作報錯


+ 創建一個多重索引，但是索引並沒有自然排序

```Python
## 構建多重索引
index = pd.MultiIndex.from_product()
[['a', 'c', 'b', 'd'], [1, 2]]
## 構建多重索引的Series
data = pd.Series(np.random.rand(8), index = index)
## 添加索引標籤名稱
data.index.names = ['char', 'float']
```


+ 對Series進行切片，將會報錯

```Python
## 切片操作
try:
    data['a':'d']
except KeyError as e:
    pritn(type(e))
    print('Error Message: ', e)
    


```

+ 錯誤訊息: 這條錯誤訊息就是因為MultiIndex沒有排序導致的結果，在很多理由下，當對MultiIndex進行部分切片和其它類似的操作時，都會需要索引是有順序的(或稱自然排序)


**解決方法**

Pandas提供了對索引進行排序的方法，像是:

+ sort_index()
+ sortlevel()

+ 這邊使用sort_index來實現
```Python
## 索引排序
data = data.sort_index()

data

```

+ 索引排序好後，切片(slice)就可以正確完成了

```Python
## 切片操作
data['a':'d']

```

#### 索引的堆疊和拆分 - Stacking And Unstacking Indices

+ unstack(): 將一個堆疊的多重索引數據集拆分成一個二維形式，並且使用level參數指定使用哪一層進行拆分

```Python
print(city_house)

## 根據城市名稱轉換成二維形式
city_house.unstack(level = 0)

```

```Python
## 根據年份轉換成二維形式
city_house.unstack(level = 1)

```

+ stack(): 堆疊數據集

```Python
## 堆疊數據
city_house.unstack().stack()

```

#### 設置和重新設置索引 - Index Setting And Reseting

+ 說明: 將索引標籤轉為列，透過reset_index方法完成


+ 在房屋數據上使用reset_index這個方法，就會在結果Dataframe中將城市名稱和年份這兩個索引標籤變成列，並且使用name參數來對原本的數據定義一個列名

```Python
## 增加索引標籤
city_houe.index.names = ['city', 'year']

## 將索引標籤轉為列數據
city_house_flat = city_house.reset_index(name = 'house')

city_house_flat


```

+ 在處理真實世界的數據時，通常會看到的數據形式像上面那樣，因此在列當中構建一個MultiIndex很有用，可以透過於Datframe中使用set_index來達成，結果就會返回一個多重索引的DataFrame

```Python
## 構建MultiIndex的DataFrame
city_house_flat.se_index(['city', 'year'])

```


+ **重要性: 作者在實務上的經驗覺得這樣重新索引的方式是很有用的**




### 6. 多重索引的數據聚合 - Data Aggregations On Multi-Inndices

+ Pandas內建的數據聚合方法，像是mean()、max()、mn()和sum()，用在層次化索引的數據上。可以透過設定level參數來控制數據根據哪個層次進行運算


+ 醫院數據集

```Python
hosipital_data
```

+ 我們希望瞭解不同年份的平均測量值，就可以透過設置level參數來指定需要進行聚合的標籤

```Python
## 依照年份計算測量平均
data_mean = hospital_data.mean(level = 'year')

data_mean

```


+ axis參數: 透過設定此參數，可以指定在列或行上沿著指定的層次level進行聚合

```Python
## 根據測量種類沿著列計算平均
data_mean.mean(axis = 1, level = 'type')

```

很少程式碼，就已經能夠運算獲得所有受試者每年多次進行測試取樣的平均心律和溫度，此語法實際上是GroupBy函數的簡寫，會在之後的章節進行探討


### 補充: Panel數據 - Aside: Panel Data

還有一些數據結構這章節沒有探討到，像是pd.Panel和pd,Panel4D對象(object)，這兩者是對應於一維Series和二維的DataFrame相應的三維和四維的通用數據結構，熟悉Series和DataFrame的操作，Panel和Panel4D使用起來就會很直觀，而loc和iloc索引符號操作也可以直接在高維結構中使用


**作者不特別介紹Panel的原因**

+ 因為作者認為在大部分的下多重索引會更有用，在高維度的數據概念上也顯得比較簡單
+ Panel 數據從基本上來看為密集數據，而多重索引則為稀疏矩陣，隨著維度增加使用密集數據方式表示數據是非常低效的，但對於一些特殊的應用狀況，這樣的結構是很有用的































































































































































































































































































































































































































































































































































































































































































