# NumPy的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - 花式索引(高級索引) Fancy Indexing 根據索引條件一次性地找到所有對應元素值- 非常重要的排序算法 - 格式化數組 NumPy's Structured Arrays 存儲不同類型的數據和運用-NumPy紀錄數組獲取數據效能更高? -筆記#8







## 2.7章 花式索引(高級索引) Fancy Indexing





+ 在前面我們介紹過如何獲取和修改數組的元素或部分元素，就是透過簡單的索引(ex. arr[0])、切片(ex. arr[:5])和布林遮蓋(ex. arr[arr > 0])的方法來實現目的





### 1. 高級索引 是什麼? What is Fancy Indexing



+ 高級索引的用法和我們之前的簡單索引很像，但是差別在它不是傳遞標量(scalars)參數作為索引值，而是傳遞數組參數作為索引值

+ 它能讓使用者很迅速地獲取和修改複雜數組或子數組的元素值



### 2. 探索高級索引 Exploring Fancy Indexing



+ 重要觀念: 高級索引在概念上非常簡單，傳遞一個數組作為索引值參數，讓使用者可以一次性的獲取或修改多個數組的元素值



+ 舉例: 創建一個數組

```Python
import numpy as np
rand = np.random.RandomState(2)

## 創建數組
x = rand.randint(100, size = 10)
print(x)
```

**執行結果**

```
[40 15 72 22 43 82 75  7 34 49]
```







+ 簡單索引方式: 我們想獲取數組內的三個元素

```Python
## 獲取索引位置為2,6,7的三個元素
[x[2], x[6], x[7]]
```

**執行結果**

```
[72, 75, 7]
```



+ 高級索引方式: 用一個數組的方式來將這些元素的數組一次傳給原數組

```Python
ind = [2, 6, 7]
x[ind]
```

**執行結果**

```
array([72, 75,  7])
```



+ 使用高級索引的時候，結果的數組形狀會取決於索引數組的形狀，而不是原數組(被索引數組)的形狀

+ 重要: 高級數組支援多維數組

```Python
## 創建一個二維數組
d2 = np.arange(49).reshape((7, 7))
d2
```

**執行結果**

```
array([[ 0,  1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12, 13],
       [14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27],
       [28, 29, 30, 31, 32, 33, 34],
       [35, 36, 37, 38, 39, 40, 41],
       [42, 43, 44, 45, 46, 47, 48]])
```





+ 就如普通索引，第一個參數行，第二個參數為列

```Python
row = np.array([0, 2, 6])
col = np.array([2, 6, 6])
d2[row, col]
```

**執行結果**

```
array([ 2, 20, 48])
```

+ 結果: 第一個值就是x[0, 2]，第二個是x[2, 6]，第三個是x[6, 6]



+ 重要概念: 高級索引的多個維度組合，也需要遵守廣播(Broadcasting)的規則，所以如果我們在行索引數組的地方增加一個維度，結果就會變成一個二維數組喔



+ 這邊每個行索引會匹配每個列的向量，如同之間我們在廣播的算術運算

```Python
## 將行改成垂直，然後乘以列
print(row[:, np.newaxis])
print(col)
print(row[:, np.newaxis] * col)
```

**執行結果**

```
[[0]
 [2]
 [6]]
[2 6 6]
[[ 0  0  0]
 [ 4 12 12]
 [12 36 36]]
```





**結論**

高級索引結果的形狀是索引數組廣播後的形狀，並不是被索引數組的形狀，非常重要要記住





### 3. 組合索引 Combined Indexing



+ 創建一個二維數組

```Python
## 創建一個二維數組
d2 = np.arange(49).reshape((7, 7))
d2
```

**執行結果**

```
array([[ 0,  1,  2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11, 12, 13],
       [14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27],
       [28, 29, 30, 31, 32, 33, 34],
       [35, 36, 37, 38, 39, 40, 41],
       [42, 43, 44, 45, 46, 47, 48]])
```





+ 高級索引 + 簡單索引: 將高級索引和簡單索引進行組合，原理其實就是廣播，將標量(Scaler)廣播成一個向量

```Python
## 高級索引 + 簡單索引: 將高級索引和簡單索引進行組合，原理其實就是廣播，將標量(Scaler)廣播成一個向量
## 獲取第三行的第3、第4、第六的元素值
d2[2, [2, 3, 5]]
```

**執行結果**

```
array([16, 17, 19])
```





+ 高級索引 + 切片

```Python
## 高級索引 + 切片
## 獲取第二行以後的第3、第4、第六的元素值
d2[1:, [2, 3, 5]]
```

**執行結果**

```
array([[ 9, 10, 12],
       [16, 17, 19],
       [23, 24, 26],
       [30, 31, 33],
       [37, 38, 40],
       [44, 45, 47]])
```





+ 高級索引 + 遮蓋(Masking)

```Python
## 高級索引 + 遮蓋(Masking)

## 創建遮蓋Mask
mask = np.array([1, 0, 1,0])

## 構建行的索引
row = np.array([0, 2, 6])

## 獲取第1、3、七行的第1跟第2個位置
d2[row[:, np.newaxis], mask]
```

**執行結果**

```
array([[ 1,  0,  1,  0],
       [15, 14, 15, 14],
       [43, 42, 43, 42]])
```









### 4. 實作 -  選擇隨機點 Example: Selecting Random Points



+　使用時機: 高級索引有一個很常被使用到的場景，就是從一個矩陣的行(rows)中選取子數據集



+ 舉例: 我們有一個N x D的矩陣，表示在D的維度上有N個點，像是下面的二維正態分布的點結合

```Python
## 設定平均值和共變異數
mean = [0, 0]
cov = [[1, 2],
       [2, 5]]


## 創建二維正態分布
x = rand.multivariate_normal(mean, cov, 100)
# print(x)
x.shape
```

**執行結果**

```
(100, 2)
```

+ 視覺化這個數據集

```Python
## 視覺化
%matplotlib inline
import matplotlib.pyplot as plt
## 設定圖表風格
import seaborn; seaborn.set()


plt.scatter(x[:, 0], x[:, 1])
```

**執行結果**

![2.7.1](images\2.7.1.PNG)



+ 高級索引應用: 使用高級索引來選擇20個隨機點，方法是先構建一個索引數組，裡面的索引值不重復，接下來使用這個數組來選擇點

```Python
## 高級索引應用: 使用高級索引來選擇20個隨機點，方法是先構建一個索引數組，裡面的索引值不重復，接下來使用這個數組來選擇點

## 隨機選擇20個數據點
indices = np.random.choice(x.shape[0], 20, replace = False)
print('Index:', indices)

## 根據隨機出來的20個索引，找到對應數據集的元素值
## 高級索引方式 Fancy Indexing
selection = x[indices]
print('Selected Data', selection)
print('Shape: ', selection.shape)
```

**執行結果**

```
Index: [84  0  8 45 82 60 62 77 99  6 92 83 78 76 39 85 61 88 29 91]
Selected Data [[-1.16225052 -2.33247155]
 [ 1.02261758  1.75690791]
 [ 1.53083517  3.36239952]
 [-0.07401261  0.07680661]
 [ 0.3063489  -0.09203542]
 [-0.8872499  -4.36769674]
 [ 0.44588565  0.00868721]
 [-0.55026016 -0.88792517]
 [ 2.34939722  2.94925459]
 [ 1.0922079   2.38687983]
 [ 0.20102031  0.75537747]
 [-0.19354986 -0.68086017]
 [ 0.99427298  1.7944424 ]
 [ 0.43917459 -0.91210767]
 [ 1.07145196  2.98009196]
 [ 0.03419971  0.22937178]
 [-0.29712269 -1.34734648]
 [ 0.09655075 -0.34780985]
 [-1.53513181 -4.33433811]
 [ 0.73541291  1.78156777]]
Shape:  (20, 2)
```



+ 視覺化那些被選中的點和原本數據點的分布

```Python
## 視覺化

## 原數聚集
plt.scatter(x[:, 0], x[:, 1], alpha = 0.3)

## 隨機選擇的20個元素值
plt.scatter(selection[:, 0], selection[:, 1], facecolor = 'none', s = 200)
```

**執行結果**

![2.7.2](images\2.7.2.PNG)



**結論**

這個策略方法經常用來劃分數據集，像是用來驗證統計模型精準性的訓練集與測試集，還有回答統計問題時進行的取樣抽象







### 5. 使用高級索引來修改數據 Modifying Values with Fancy Indexing



+ 舉例: 我們有一個索引數組，我們想根據這個索引來修改對應的元素值

```Python
## 創建一個數組
x = np.arange(10)
print('Original: ', x)

## 將第3,4,7,8位置修改成66
i = np.array([2,3,6,7])
x[i] = 66
print('Modify', x)
```

**執行結果**

```
Original:  [0 1 2 3 4 5 6 7 8 9]
Modify [ 0  1 66 66  4  5 66 66  8  9]
```





+ 可以使用任何賦值類型的操作

```Python
## 將第3,4,7,8位置減10
x[i] -= 10
print(x)
```

**執行結果**

```
[ 0  1 56 56  4  5 56 56  8  9]
```



+ 提醒: 如果索引數駔中有重復元素的話，這樣的操作可能會導致一個潛在意料之外的結果

```Python
x = np.zeros(10)
x[[0, 0]] = [4, 6]
print(x)
```

**執行結果**

```
[6. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```





+ 結果: 4跑去哪了? 上面的操作會首先賦值x[0] = 4，然後賦值x[0] = 6，所以最後的x[0]為6



+ 再看一個例子

```Python
print('Before: ', x)
i = [2, 3, 3, 4, 4, 4]
x[i] += 1
print('After: ', x)
```

**執行結果**

```
Before:  [6. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
After:  [6. 0. 1. 1. 1. 0. 0. 0. 0. 0.]
```



+ 結果: 我們希望看到的是x[3]的值是2，而x[4]的值是3，因為這兩個索引值重復出現，所以對兩個元素進行了多次的加法動作



**但結果為什麼不是這樣?**  這是因為x[i] += 1是操作 x[i] = x[i] + 1的簡寫，而 x[i] = x[i] + 1表達是已經算好了，然後才被賦值給x[i]，因此上面的操作不會被擴展為重復運算，而只是一次性的賦值操作，所以才造成了這種難理解的結果





+ 如果我們還是需要這種重復操作的話，可以使用NumPy提供的at()這個ufunc方法來達成需求



```Python
x = np.zeros(10)
print('Before: ', x)
i = [2, 3, 3, 4, 4, 4]
np.add.at(x, i, 1)
print('After: ', x)
```

**執行結果**

```
Before:  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
After:  [0. 0. 1. 2. 3. 0. 0. 0. 0. 0.]
```



**重點 :**

+ at()方法不會預先計算表達式的值，而是根據每次運算及時得到

+ at()函數用法: 第一個參數為數組，第二個參數為索引，第三個參數為要進行的運算

+ 另有一個類似的方法 - reduceat()





### 6. 實作 - 數據裝箱(分組) Example: Binning Data



+ 舉例: 我們有1000個值，想將它們分別放入各個不同的數組分組中，並快速地找到它們在分組數組中的位置，此時就可以使用at()函數

```Python
## 隨機產生一個一維並擁有100個標準正態分布的值
np.random.seed(66)
x = np.random.randn(100)

## 自定義一個數據分組， 區間-5到5平均取20個數據點，每個區間為一個數據分組
bins = np.linspace(-5, 5, 20)

## counts為x數值落入區間的計數
counts = np.zeros_like(bins)

## 使用searchsorted，來獲得x每個算在bins中落入的區間序號
i = np.searchsorted(bins, x)

## 使用at和add，對x元素在每個區間的元素個數進行計算
np.add.at(counts, i, 1)
```



+ counts代表著每個數組分組中元素的個數，換句話說，就是直方圖喔



**提醒: 由於從Matplotlib3.1開始，linestyle這個參數已經不再支援，改成drawstyle或寫ds喔**

```Python
## 視覺化
plt.plot(bins, counts, ds = 'steps')
```

**執行結果**

![2.7.3](images\2.7.3.PNG)



+ 如果每次繪製直方圖時都必須這樣做是很麻煩的，這也就是Matplotlib提供plt.hits()例程的原因，該例程在一行中達到與上面一樣的操作

```Python
## 視覺化 採用np.hist
plt.hist(x, bins, histtype = 'step')
```

**執行結果**

![2.7.4](images\2.7.4.PNG)



+ Matplotlib的plt.hits()為了計算合併，它所使用的是np.histogram函數，這與我們之間做的很相似，比要一下兩者

```Python
print("Numpy routine: ")
%timeit counts, edges = np.histogram(x, bins)

print('Custom routine: ')
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)
```

**執行結果**

```
Numpy routine: 
25.6 µs ± 1.95 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
Custom routine: 
12.9 µs ± 255 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

+ 結果: 我們前面所使用的單行算法np.searchsorted比NumPy中的優化算法快好幾倍!!



**為什麼有這樣的結果?**



如果深入研究np.histogram的源代碼(使用np.histogram??來查看)，會發現它比我們完成的簡單搜索和計數要(simple search-and-count)涉及得多，這是因為NumPy的算法更加有彈性，尤其是當數據點數量變大時，它的設計目的是為了提高表現(性能)



+ 當數據量大時比較兩者運算效能

```Python
## 構建一個大型數據集
x = np.random.randn(100000)
print("Numpy routine: ")
%timeit counts, edges = np.histogram(x, bins)

print('Custom routine: ')
%timeit np.add.at(counts, np.searchsorted(bins, x), 1)
```

**執行結果**

```
Numpy routine: 
5.5 ms ± 48.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
Custom routine: 
9.2 ms ± 162 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

### 結論

+ 從上面的結果可以理解，算法效率從來不是一個簡單的問題，對於大型數據集而言，高效的算法並不一定是小型數據集的最佳選擇，反之也是

+ 作者認為自己編寫算法的好處是，在了解了這些基本的方法之後，我們可以使用這些構造塊(Building Blocks)來擴展這些有趣的自定義行為，在數據密集型的應用程式中，能有效地使用Python的關鍵在了解像是np.histogram之類的常規便利例程以及何時適合使用它們，以及當需要更多針對性行為時，能夠了解如何利用底層的功能





## 2.8章 數組排序 Sorting Arrays





### 1. 自行定義的各種排序算法



過去我們學習過的相關排序方法，像是插入排序(Insertion sorts)、選擇排序(selction sorts)、合併排序(Merge Sort)、快速排序(quick sort)、冒泡排序(bubble sort)等等，接下來這邊會介紹的是對NumPy數組進行排序的算法



+　選擇排序(Selection Sort): 一個簡單的選擇排序會重復尋找列表中最小的值，然後和當前的值進行交換，直到列表排序完成



```Python
import numpy as np

## 選擇排序 Selection Sort
def selection_sort(x):
    for i in range(len(x)):
        ## 尋找數組中最小值的索引序號   
        swap = i + np.argmin(x[i:])
        ## 替換當前值和最小值
        (x[i], x[swap]) = (x[swap], x[i])
    return x

x = np.array([2,8,3,5,9,2,1,6,7,9,3,6,6])
selection_sort(x)
```

**執行結果**

```
array([1, 2, 2, 3, 3, 5, 6, 6, 6, 7, 8, 9, 9])
```







+ 結論: 選擇排序很簡單，但是對於應用在大型數組上，運行效率相當慢對於具有N個值得數組，它需要N次循環，每次循環中還需要~N次比較和尋找來執行交換元素，Big-O(時間複雜度)經常用來對算法性能進行定量分析，而選擇排序(Selection Sort)平均需要O[N ** 2]； 如果例表中的元素個數加倍，執行時間會大約變成原本的4倍





+ 選擇排序法遠比bogosort排序算法來的有效多了



```Python
import numpy as np

def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

x = np.array([2,8,3,5,9,2,1,6,7,9,3,6,6])
bogosort(x)
```



**bogosort排序算法:** 

bogosort這個有趣而笨笨的算法完全依賴於機會(機率): 它重復對數組進行隨機的亂序直到結果剛好是正確排序為止，此算法平均需要O[N X N!]，表示N乘N階層，這樣真的太慢了，所以在真實情況，它不應該被用在排序





不用擔心上面的狀況，Python有內建的排序算法，比我們剛剛提到的那些簡單的排序算法都要高效，接下來我們會先討論Python內建的排序算法，接著再討論NumPy中為了優化數組的排序函數



### 2. NumPy中的快速排序: np.sort 和 np.argsort 





+ Python內建的方法: sort和sorted函數

+ NumPy的方法: np.sort 和 np.argsort



這邊不對Python的sort和sorted多做討論，是因為**NumPy的np.sort函數有更優秀的性能**





+ 使用np.sort: 對數組進行排序，傳回排序後的結果，但是不改變原始數組的數據資料

```Python
x = np.array([6,2,4,3,5,9,3,7,5,6,6])
print('Sorted: ', np.sort(x))
print('Original: ', x)
```

**執行結果**

```
Sorted:  [2 3 3 4 5 5 6 6 6 7 9]
Original:  [6 2 4 3 5 9 3 7 5 6 6]
```





+ 使用sort: 直接對原數組進行排序，會改變原始數組的數據資料

```Python
x.sort()
print(x)
```

**執行結果**

```
[2 3 3 4 5 5 6 6 6 7 9]
```





+ 使用argsort: 它將傳回排好序後，元素原始的序號(index)序列:

```Python
x = np.array([6,2,4,3,5,9,3,7,5,6,6])
i = np.argsort(x)
print(i)
```

**執行結果**

```
[ 1  3  6  2  4  8  0  9 10  7  5]
```



+ 結果: 第一個元素為最小元素在原數組的序號(index)，第二個元素為第二小的序號，以此類推





+ 如果想獲得原數組中第二、第三、第四小的元素，可以這樣寫

```Python
## 獲取數組中第二，第三，第四小的元素
x[i[1:4]]
```

**執行結果**

```
array([3, 3, 4])
```





### 3. 按照行或列進行排序 Sorting along rows or columns



NumPy中的排序算法可以根據多位數組中的某特定軸axis進行排序，像是行和列



```Python
## 創建一個隨機二維數組
rand = np.random.RandomState(66)
d2 = rand.randint(0, 10, size = (6, 4))
d2
```

**執行結果**

```
array([[4, 7, 3, 5],
       [3, 0, 7, 6],
       [0, 2, 2, 2],
       [6, 0, 8, 8],
       [9, 9, 8, 2],
       [7, 2, 3, 0]])
```





+ axis = 0

```Python
## 根據每列對數據進行排序
np.sort(d2, axis = 0)
```

**執行結果**

```
array([[0, 0, 2, 0],
       [3, 0, 3, 2],
       [4, 2, 3, 2],
       [6, 2, 7, 5],
       [7, 7, 8, 6],
       [9, 9, 8, 8]])
```





+ axis = 1

```Python
## 根據每行對數據進行排序
np.sort(d2, axis = 1)
```

**執行結果**

```
array([[3, 4, 5, 7],
       [0, 3, 6, 7],
       [0, 2, 2, 2],
       [0, 6, 8, 8],
       [2, 8, 9, 9],
       [0, 2, 3, 7]])
```





+ 提醒: 這種排序方式會獨立的對每一行或每一列進行排序，所以結果中原來行或列之間的聯繫都會丟失



**因為篇幅的關係，所以2.8章後面的內容，會放在下一篇喔!!**





# NumPy的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - 花式索引(高級索引) Fancy Indexing 根據索引條件一次性地找到所有對應元素值- 非常重要的排序算法 - 格式化數組 NumPy's Structured Arrays 存儲不同類型的數據和運用-NumPy紀錄數組獲取數據效能更高? -筆記#9



**這篇是延續上一篇2.8章後面的內容繼續往下寫的筆記喔!!**





## 2.8章 數組排序 Sorting Arrays





### 4. np.partition 部分排序: 分區 Partial Sorts: Partitioning



+ 使用情況: 有時候我們並不是需要對整個數組排序，而僅僅需要的是找到數組中K個最小值

+ 解決方法: NumPy提供了np.partition函數來達成這個任務

+ 返回結果: 結果會被分成兩部分，最小的K個值會位於數組的左邊，而其餘的值會位於右邊，**順序則是隨機的**



+ 舉例一: 找到前四個最小值



```Python
## 創建一個數組
x = np.array([6,2,9,8,1,7,3,2,8])
## 找到最小的四個值
np.partition(x, 4)
```





結果: 可以看到結果中最小的四個值位於數組的左邊，其餘的值位於右邊，而元素的順序是隨機的



+ 舉例二: 和排序一樣，可以根據任意軸對一個多維數組進行分區

```Python
## 創建一個隨機二維數組
rand = np.random.RandomState(2)
d2 = rand.randint(0, 10, size = (4, 6))
print(d2)
## 根據行進行分區，找到最小的三個元素
np.partition(d2, 3, axis = 1)
```







+ 結果中每行的前三個元素就是該行的最小的三個值喔



### 5. 實作 K-Nearest Neighbors - 使用np.argsort 和 np.argpartition



np.argpartition: 如同np.argsort函數可以傳回排好序的元素序號一樣，np.argpartition則可以計算分區後的元素序號(Index)





+ 這邊將使用argsort根據多個維度來找尋每個點的近鄰(Nearest Neighbors)

+ **STEP1 : **在一個二維平面上構建10個隨機數據，依照慣例，我們會先排列為一個[Math Processing Error]10X2的數組

```Python
## 創建一個隨機的10X2數組
x = rand.rand(10, 2)
x
```







視覺化

```Python
## 視覺化
%matplotlib inline
import matplotlib.pyplot as plt
## 設定風格
import seaborn; seaborn.set()


## 繪製散點圖
plt.scatter(x[:, 0], x[:, 1], s = 100)
```





+ **STEP2:** 計算每兩個點之間的距離，距離平方的公式是兩點坐標差的平方和

應用廣播(Broaadcasting)和聚合(Aggregation)，我們只需要使用一行程式碼就能完成

```Python
## 計算每兩個點間的距離
dist_sq = np.sum((x[:, np.newaxis, :] - x[np.newaxis, :, :]) ** 2, axis = -1)
dist_sq
```







+ **拆解上面的方法:** 上面那行的程式碼可能很難直接理解，所以這邊將一步一步解釋

```Python
## 計算每兩個點之間的坐標距離
## differences = x[:, np.newaxis] - x[np.newaxis, :] 我自己實驗覺得與書本計算結果一樣
differences = x[:, np.newaxis, :] - x[np.newaxis, :, :]
# print(differences)
differences.shape
```



```Python
## 計算距離的平方
sq_difference = differences ** 2
# print(sq_difference)
sq_difference.shape
```



```Python
## 按照最後一個維度求和
dist_sq = sq_difference.sum(-1)
dist_sq
```





+ 檢查這個舉的對角線元素，對角線的原數值是點與其自身的距離平方，應該要都為0

```Python
## 檢查對角線元素值
dist_sq.diagonal()
```





+ **STEP3 :** 上面得到了距離平方矩陣，接著就可以使用np.argsort函數來按照每行進行排序，最左邊的列會給出每個數據點的最近鄰(Nearest Neighbor)

```Python
nearest = np.argsort(dist_sq, axis = 1)
print(nearest)
```







+ 結果中的第一列是0到9的數字: 因為每個點最近的的點當然是自己



這邊對數據點位置進行了完整的排序，但其實我們不需要這樣做，如果我們只對最近的K個鄰居有興趣的話，可以使用分區(Partition)來完成





+ **STEP4 :** 我們想知道最近的K個鄰居，為哪些數據點，只要在距離平方矩陣中對每行進行K+1分區即可，使用np.argpartition函數達成

```Python
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis = 1)
nearest_partition
```





+　**STEP5 :** 視覺化最近鄰網路圖，圖中連線每個點和它最近的兩個點之間的距離

```Python
## 畫出每個數據點
plt.scatter(x[:, 0], x[:, 1], s = 100)

## 每個數據點與它最近的兩個點之間連線
K = 2


## x.shape[0]: 表示數據量
## nearest_partition[i, :K+1]: 代表指定數據x[i]最近的K個近鄰
for i in range(x.shape[0]):
    for j in nearest_partition[i, :K+1]:
        ## 從x[i]連線到x[j]
        ## 使用一些zip魔術(Magic Funcion)方法來畫線
        plt.plot(*zip(x[j], x[i]), color = 'black')
```







+ 結果: 圖中看起來有些點的線可能超過兩條，其實是因為如果A是B的兩個近鄰之一，但不代表B必須也是A的兩個近鄰之一





**結論**



+ 雖然使用廣播和逐行排序的方式沒有循環來直觀，但是在Python中這是一種非常有效率的方式

+ 使用循環方式來對每個點計算它相對應的近鄰，會比我們前面使用的向量化操作慢非常多

+ 向量化方法還具備一個優點: 它不在意數據的尺寸，可以使用一樣的程式碼和方法計算100個或1000000個以上的數據點，和任意維度數的數據集的最近鄰點(Nearest Neighbor) 

+ 還有一種方法為KD-Tree，它是一個基於樹或相似的算法能夠將時間複雜度從原本方法的O[N**2]優化到O[NlogN]，適合對一個非常大型的數據集進行最近鄰搜索



### 6. Big-O 表示法



+ 說明: Big-O 表示法次一種描述算法的操作數據如何隨著輸入的大小增加而擴展的方法

+ 其他: 當然也會有small-o表示法、big-[Math Processing Error]θθ表示法、big-[Math Processing Error]Ω和很多其他混合的種類

+ 數據科學世界: 普遍被使用的是較不嚴格的Big-O 表示法，來當算法縮放的一種描述



+ 廣義定義: Big-O 表示法告訴我們，算法在增加數據量時將耗費多少的時間



+ N的定義: N通常會表示為數據集大小的某些面向(數據點數、維數等)，當我們要分析數十億或數萬億的數據時O[N]和O[N平方]之間的差值會顯得非常小



+ 重要觀念: Big-O 表示法不會告訴我們計算的實際時間，而是告訴我們更改N時的縮放比例


## 2.9章 格式化數據: NumPy中的格式化數組 Structured Data: NumPy's Structured Arrays



大部分的情況下我們的數據都能表示成一個同類型的數組，但是總會有例外的狀況，這章節探討了如何使用NumPy的結構化數組(structured arrays)和紀錄數組(record arrays)，它提供了對於複合、不同種類的數組有效率地存儲方式





### 1. 創建格式化數組和基本運用







+ 今天我們有關於人的三種不同類型的數據(ex. Name、Age、Weight)，然後我們想將它們保存於Python程序中，可以採用保存到三個獨立數組的方

```Python
import numpy as np

## 創建三種不同類型的數組: str、int、float
name = ['Jack', 'Victor', 'Henna', 'Jen','Jessy']
age = [34, 40, 23, 36, 28]
weight = [60.0, 90.8, 50.6, 46.2, 52.4]
```





+ 上面的作法有點不好，因為沒有額外的訊息告訴我們三個數組間的關聯

+ **解決方法 :**  使用一個結構來保存所有的這些數據，就會顯得自然許多，而NumPy可以使用結構化數組來處理這個狀況，因為結構化數組可以儲存複合的數據類型

+ 過去我們創建一個簡單數組的方式

```Python
## 創建一個簡單數組的方法，指定數據類型為整數
np.zeros(5, dtype = int)
```

```
array([0, 0, 0, 0, 0])
```



+ 透過指定對應的dtype數據類型，可以創建一個複合類型的數組

```Python
## 這邊使用複合的dtype(data type)參數來創建結構化的數組
data = np.zeros(5, dtype = {'names': ('name', 'age', 'weight'),
                            'formats':('U10','i4','f8')
                           })

## 數組的類型
print(data.dtype)

```

```
[('name', '<U10'), ('age', '<i4'), ('weight', '<f8')]
```



+ 結果: 

  +　U10: 表示Unicode編碼的字符串，最大長度為10

  + i4: 表示4-byte(i.e., 32 bit)整數

  + f8: 表示8-byte(i.e., 64 bit)浮點數

  



+ 將數據填進我們創建好的空結構化數組

```Python
## 將數據填進我們創建好的空結構化數組
data['name'] = name
data['age'] = age
data['weight'] = weight


print(data)
```

```
[('Jack', 34, 60. ) ('Victor', 40, 90.8) ('Henna', 23, 50.6)
 ('Jen', 36, 46.2) ('Jessy', 28, 52.4)]
```



+ 結果: 三個獨立數組的數據現在被存儲在一整塊的內存空間之中，也就是被存儲在一起







+ 使用結構化數組的好處在可以使用字段的名稱，而不是序號索引來訪問元素值了

```Python
## 獲取所有姓名
print(data['name'])

## 獲取所有年齡
print(data['age'])

## 獲取所有重量
print(data['weight'])
```

```
['Jack' 'Victor' 'Henna' 'Jen' 'Jessy']
[34 40 23 36 28]
[60.  90.8 50.6 46.2 52.4]
```



```Python
## 獲得第一筆數據(獲取第一行)
data[0]
```

```
('Jack', 34, 60.)
```



```Python
## 獲取最後一筆數據的重量(獲取最後一行的重量)
data[-1]['weight']
```

```
52.4
```



+ 布林遮蓋 Boolean Masking - 增加條件來過濾數據，像是體重的過濾

```Python
## 過濾體重，找到體重大於50的姓名
data[data['weight'] > 50]['name']
```

```
array(['Jack', 'Victor', 'Henna', 'Jessy'], dtype='<U10')
```

### 2. 創建結構化數組 Create Structured Arrays



+ 第一種方式: 字典(dict)的方式

```Python
## 字典的方式
np.dtype({
    'names':('name','age','weight'),
    'formats':('U10','i4','f8')
})

```

```
dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f8')])
```



+ 這邊數字類型也可以透過Python類型或是NumPy數據類型來設定

```Python
## Python類型或NumPy類型來指定
np.dtype({
    'names':('name','age','weight'),
    'formats':((np.str_, 10), int, np.float32)
})
```

```
dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])
```

+　第二種方式: 元組(tuple)的方式

```Python
## 元組
np.dtype([('name','S10'), ('age', 'i4'), ('weight', 'f8')])
```

```
dtype([('name', 'S10'), ('age', '<i4'), ('weight', '<f8')])
```





+ 第三種方式: 如果類型的名稱不重要，可以直接省略掉，以一個用逗號分隔的字符串來設定數據類型

```Python
## 省略類型名稱，直接使用逗號隔開的字符串指定
np.dtype('S10, i4, f8')
```

```
dtype([('f0', 'S10'), ('f1', '<i4'), ('f2', '<f8')])
```





+ 符號講解:

縮短的字符串格式碼看起來很難懂，但實際上它是依據一個簡單的規則創立的，第一個(可選的)字符是<或>，代表這類型是小端序(Little Endian)或是大端序(Big Endian)，下一個字符設定的是數據類型: 字符、字節(bytes)、整數、浮點數或其他如下表，最後一個字符則代表類型的長度



如果不清楚小端序(Little Endian)或是大端序(Big Endian)的話，可以參考這篇喔https://blog.gtwang.org/programming/difference-between-big-endian-and-little-endian-implementation-in-c/





| 字符 Character | 描述 Description       | 例子 Example                       |
| :------------- | :--------------------- | :--------------------------------- |
| `'b'`          | Byte                   | `np.dtype('b')`                    |
| `'i'`          | Signed integer         | `np.dtype('i4') == np.int32`       |
| `'u'`          | Unsigned integer       | `np.dtype('u1') == np.uint8`       |
| `'f'`          | Floating point         | `np.dtype('f8') == np.int64`       |
| `'c'`          | Complex floating point | `np.dtype('c16') == np.complex128` |
| `'S'`, `'a'`   | String                 | `np.dtype('S5')`                   |
| `'U'`          | Unicode string         | `np.dtype('U') == np.str_`         |
| `'V'`          | Raw data (void)        | `np.dtype('V') == np.void`         |





### 3. 更多進階的複合類型 More Advanced Compound Types



定義更加複雜的複合類型，像是我們可以創建一個類型，裡面的每個元素裝載一個數組或矩陣值



+ 構建一個數據類型，裡面包含一個mat對象，由一個3 X 3的浮點數矩陣構成

```Python
## 建立類型
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
# print(tp)
## 使用剛剛設定的類型建立數組
x = np.zeros(2, dtype = tp)
# print(x)
print(x[0])
print(x['mat'][0])
```

```
(0, [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```







+ 程式講解: 上面x數組中的每個元素都有一個id和3 X 3矩陣



重要觀念: 上面的方法為什麼不用一個多維數組或是Python的字典呢?

+ 原因: 由於NumPy的dtype數據類型直接對應這一個C語言的結構體定義，因此存儲這個數組的內容可以直接被C語言的程式使用

+ 使用時機: 當我們在寫訪問底層C語言或Fortran語言的Python接口的情況下，這種結構化數組就會很有用

### 3. 更多進階的複合類型 More Advanced Compound Types



定義更加複雜的複合類型，像是我們可以創建一個類型，裡面的每個元素裝載一個數組或矩陣值



+ 構建一個數據類型，裡面包含一個mat對象，由一個3 X 3的浮點數矩陣構成

```Python
## 建立類型
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
# print(tp)
## 使用剛剛設定的類型建立數組
x = np.zeros(2, dtype = tp)
# print(x)
print(x[0])
print(x['mat'][0])
```

```
(0, [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```







+ 程式講解: 上面x數組中的每個元素都有一個id和3 X 3矩陣



重要觀念: 上面的方法為什麼不用一個多維數組或是Python的字典呢?

+ 原因: 由於NumPy的dtype數據類型直接對應這一個C語言的結構體定義，因此存儲這個數組的內容可以直接被C語言的程式使用

+ 使用時機: 當我們在寫訪問底層C語言或Fortran語言的Python接口的情況下，這種結構化數組就會很有用





### 4. 紀錄數組: 具有彎曲方式的結構化數組  RecordArrays: Structured Arrays with a Twist



+ np.recarray: NumPy提供了一個類np.recarray，它幾乎與結構化數組相同，但是它可以使用屬性來獲取數值，而不是使用字典關鍵字來獲取



```Python
import numpy as np

## 創建三種不同類型的數組: str、int、float
name = ['Jack', 'Victor', 'Henna', 'Jen','Jessy']
age = [34, 40, 23, 36, 28]
weight = [60.0, 90.8, 50.6, 46.2, 52.4]


## 這邊使用複合的dtype(data type)參數來創建結構化的數組
data = np.zeros(5, dtype = {'names': ('name', 'age', 'weight'),
                            'formats':('U10','i4','f8')
                           })


## 將數據填進我們創建好的空結構化數組
data['name'] = name
data['age'] = age
data['weight'] = weight
```



+ 前面當我們要獲得name裡面的資料時，我們會使用字典關鍵字來獲得

```Python
## 獲取name的資料
data['name']
```

```
array(['Jack', 'Victor', 'Henna', 'Jen', 'Jessy'], dtype='<U10')
```





+ 如果我們將它轉成紀錄數組，就能減少打字量，也能獲取name的資料

```Python
## 轉成紀錄數組
data_rec = data.view(np.recarray)

## 獲取name資料
data_rec.name
```

```
array(['Jack', 'Victor', 'Henna', 'Jen', 'Jessy'], dtype='<U10')
```





+ 使用屬性獲取雖然方便快速，但是會有額外的性能耗損

```Python
## 結構化數組字典關鍵字的方式
%timeit data['weight']

## 紀錄數組字典關鍵字的方式
%timeit data_rec['weight']

## 紀錄數組屬性獲取的方式
%timeit data_rec.weight
```

```
186 ns ± 4.77 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
3.16 µs ± 108 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
4.18 µs ± 104 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```





結論: 依照個人應用的需求，決定要更簡潔的寫法還是更高效能的寫法

