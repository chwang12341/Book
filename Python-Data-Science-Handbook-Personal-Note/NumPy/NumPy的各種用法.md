# NumPy的各種用法 - 讀書筆記 - Python Data Science Handbook - 數據科學 - NumPy是什麼 - 理解Python中的數據類型運作原理 - 其實Python中的（整數/列表）不僅僅是個（整數/列表）- NumPy快速創建各種數組與指定類型種類 - 筆記#4







## 2.0章 NumPy介紹



重要觀念：無論哪種數據類型，要使它變成可分析，第一步就是將他們轉換為數值 



### 1.如何使各類型的數據轉換成可分析的數據集？數據處理的第一步是什麼？ 



+ 背景：數據集的來源可能非常不同，而不同的來源，可能擁有非常不同的格式，像是文檔、圖像、聲音片段、數值測量等等，這些數據的異質性相當高 

+ 方法：將所有的數據抽象成為數值組成的數組，就能對數據集進行分析 

+　舉例:

1.數字圖片，可以被轉為簡單的二維數組 

2.聲音片段，可以被轉為一維數組，包括著時間範圍內聲音強度的數值 

3.文本，可以使用二進制數字來代表某個單詞或短語的出現頻率







### 2. NumPy是什麼？ 



+ **說明**：Numerical Python(數值Python)的縮寫，它提供了強大的接口，讓我們存儲和操作密集的數據緩衝區（dense data buffers） 
+ Python關聯：NumPy的數組像是Python內建的列表（list）型態，但是NumPy數組在儲存和操作大量數據時，提供了比Python本身更好的效能 
+ **重要性**：NumPy數組接近是整個Python數據科學領域工具鏈的核心，許多我們所使用的數據分析與處理套件都是以它為基礎構建的





### 3. 查看已安裝的NumPy版本



```Python
import numpy as np
np.__version__ 
```

**執行結果**

```
'1.18.1'
```





### 4. 提醒 - 內建幫助文檔 



+ 使用?: 查看所有文檔 

```Python
np? 
```





+ 使用<Tab>鍵：查看所有的屬性方法 

```Python
np.<Tab>
```





## 2.1章 理解Python中的數據類型與運作原理





### 1. 程式語言的動態與靜態類型



+ 靜態類型的語言：每個變數都要明確的宣告，如C、Java 
+ 動態類型的語言：沒有[每個變數都要明確宣告]的規定，變數類型可以進行動態轉換（ex. Int <-> Str），如Python，這也是為什麼Python具有易用性的重要原因 



舉例：在C中，我們會將for迴圈宣告成如下：  

```C
int total = 0
for(int i = 0; i < 100; i++){
    total +=i
}
```







而在Python中，我們如果寫一樣的程式 

```Python
total = 0
for i in range(1000):
    total += i
```







**重要觀察與觀念釐清**：從Python和C上面的範例可以看出差別，在C中每個變數都要明確宣告類型（ex. int），而在Python中的類型卻是動態去推斷的，這代表著在Python中我們可以給任何變數賦予任何數據類型的值，像是：

```Python
## Python
x = 6
x = "七"
x = "seven"
```



**重要觀念：** 



在Python的例子中，我們先將變數X賦予整數值，然後又再賦予字串類型的值，變數X會自動從整數轉換成字串類型，但這在C中，可能會導致報出一個編譯錯誤或其他無法預料的錯誤資訊（取決於哪種編譯器的使用）

```
/*C */
int x = 7
x = "seven" //會報錯
```









### 2. 動態類型語言 - Python - 易用性背後需要付出的代價





Python擁有數據類型自動轉換的靈活性，但也因為這個特性，Python必須得付出額外的儲存空間代價，Python中的變數不僅僅存儲數據本身，還需要存儲其變數相應的數據類型 





### 3. Python中的整數不僅僅是個整數 - 整數的架構



**重要觀念：** 



+ 標準的Python實現是由C語言撰寫的 

+ 每個Python當中的對象（object）都是一個偽裝良好的C結構，架構中不僅僅包含變數的值，還有其他的資訊 



實際整數中的架構



```
struct _longobject {
    long ob_refcnt;
    PyTypeObject *ob_type;
    size_t ob_size;
    long ob_digit[1];
};
```







#### 一個Python的整數中包含了這四個部分 





．ob_refcnt: 一個參考的計數器，幫助Python默默地來進行內存分配與釋放 

+ ob_type: 編碼變數的類型 

+ ob_size: 指定數據成員的大小 

+ ob_digit: 存儲真正的整數數值  







重點：這樣的架構代表著，在Python中存放一個整數比像C這樣的程式語言中存放一個整數要來得有損耗，像是如下圖 



![2.1.1](images\2.1.1.PNG)



**圖片來源：引用書中的示意圖**







**圖示說明：** 



+ 圖中的PyObjext_HEAD是架構中的一部分，它包含著參考計數（reference count）、程式碼類型和其他上面提到過的內容資訊 



+　C與Python中的整數區別： 

1. C的整數本質上就是內存中某個位置的標籤，其內存位置會編碼一個整數值 
2. Python的整數是指向內存中包含所有Python對象（object）資訊的指標，包括包含整數值的字節（bytes）







### 4. 結論：為什麼Python可以如此自由地撰寫程式？



 這些額外的資訊使Python能夠如此自由地且動態的編碼，但是這是需要付出代價的，像是結構中需要多出很多額外的資訊內容





### 5. Python中的列表不僅僅只是個列表



+ Python中的列表：標準的可變多元素的容器集合 
+ 重點：Python是動態類型的語言，所以可以創建一個具有不同類型元素的列表（list） 



範例一：創建一個整數的列表 

```Python
x = list(range(10))
print(x)
print(type(x[0]))
```

**執行結果**

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
<class 'int'>
```



範例二：創建一個字串的列表 

```Python
y = [str(c) for c in x]
print(y)
type(y)
```

**執行結果**

```
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list
```





範例三：創建不同數據類型的列表

```Python
z = ["Hello", True, 6, 5.8]
[type(item) for item in z]
```

**執行結果**

```
[str, bool, int, float]
```



#### 為什麼Python列表（list）可以裝有不同類型的數據元素？



+ **提醒：**這種靈活性是要付出代價的
+ **原因：**為了要讓列表能夠容納不同的類型，每個列表中的元素都須具有自己的類型資訊、引用計數（reference count）和其他資訊，也就是說列表裡面的每個元素都是一個完整的Python物件(object) 
+ **推論與解決方法：** 1.如果在所有的元素都是同種類型的情況下，就表示列表裡面絕大部分的資訊都是多餘的 2.所以如果我們將數據存儲在一個固定類型的數組中，顯然會更加高效 - NumPy就是固定類型的數組 
+ **圖片：**比較了動態類型的列表（Python List）與固定類型的列表（NumPy Array）![2.1.2](images\2.1.2.PNG)

**圖片來源：引用書本**





+ **圖片說明：**



1. NumPy Array: 從實作層（implementation level）來看，數組僅僅包含了一個指針指向一個連續的內存空間

2. Python List: 含有一個指針指向一塊都是指針的內存空間，裡面的指針再指向對應的完整Python物件（object），像是我們前面看到的整數  

   

#### Python List 與 NumPy Array 比較 - 動態列表與固定列表間的比較



| 列表種類    | 優點                                                         | 缺點                 |
| ----------- | ------------------------------------------------------------ | -------------------- |
| Pythin List | 靈活性，可以裝載不同的數據類型（原因：每個元素都具有完整的結構，數據本身與類型資訊 | 存儲和操作數據效率差 |
| NumPy Array | 高效地存儲和操作數據                                         | 缺少靈活性           |





### 6. Python的固定類型數組 - Fixed-Type Arrays 



Python中提供了相當多樣的選項，讓我們可以高效地存儲數據 -  固定類型數組



#### Python中內建的array套件 - 用來創建全部元素都為同一類型的數組



```Python
import array
x = list(range(10))
## i 代表整數類型
a = array.array('i', x)
print(a)
## f 代表浮點數類型
b = array.array('f', x)
print(b)
```

**執行結果**



```
array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array('f', [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
```





+ 程式碼中的"i"代表著指定數據類型為整數，而"f"代表指定為浮點數類型的數據  





#### NumPy Array - ndarray套件 



導入NumPy套件 

```Python
import numpy as np
```



範例一：使用np.array將Python列表轉變成數組

```Python
import numpy as np
np.array([1,4,66,58])
```

**執行結果**

```
array([ 1,  4, 66, 58])
```





**重要提醒：NumPy數組與Python列表不同，它只能包含一種數據類型喔** 



範例二：如果列表中其中一筆數據元素為浮點數類型，NumPy會試著向上擴展類型（下面的程式碼中將會將整數向上擴展為浮點數）

```Python
import numpy as np
np.array([6.68,7,9,9])
```

**執行結果**

```
array([6.68, 7.  , 9.  , 9.  ])
```



範例三：如果需要明確指定數據的類型，就需要使用drype參數 

```Python
import numpy as np
np.array([1,2,3,4,5,6], dtype = "float32")
```

**執行結果**

```
array([1., 2., 3., 4., 5., 6.], dtype=float32)
```





範例四：與Python列表不同，NumPy數組可以明確表示為多維度，使用列表中的列表來創建二維數組  

```Python
import numpy as np
np.array([range(i, i+6) for i in [2,6,8]])
```

**執行結果**

```
array([[ 2,  3,  4,  5,  6,  7],
       [ 6,  7,  8,  9, 10, 11],
       [ 8,  9, 10, 11, 12, 13]])
```







#### Python中內建的array套件與NumPy中的ndarray差別？ 



Python中的array套件提供了數組的高效儲存，但NumPy除了高效儲存，還更加提供了數組的高效運算



### 7. NumPy - ndarray 從頭開始創建數組 - 更有效率



+ 特別是大型的數組，使用NumPy重頭開始創建數組，會更加有效率 



範例一：zeros用法 - 指定長度後，將數組都填為0 

```Python
## 10為數組的長度
np.zeros(10, dtype = float)
```

**執行結果**

```
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```



範例二：ones用法 - 指定數組維度後，將數組都填為1 

```Python
## (3, 7): 二維3行7列
np.ones((3, 7), dtype = int)
```

**執行結果**

```
array([[1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1]])
```



範例三：full用法 - 設定維度後，再自行設定要填充的值 

```Python
np.full((3, 7), 3.14159)
```

**執行結果**

```
array([[3.14159, 3.14159, 3.14159, 3.14159, 3.14159, 3.14159, 3.14159],
       [3.14159, 3.14159, 3.14159, 3.14159, 3.14159, 3.14159, 3.14159],
       [3.14159, 3.14159, 3.14159, 3.14159, 3.14159, 3.14159, 3.14159]])
```



範例四：arange用法 - 創建一段序列值 - arange(起始值,結束值,步長) 

```Python
np.arange(0 , 60, 6)
```

**執行結果**

```
array([ 0,  6, 12, 18, 24, 30, 36, 42, 48, 54])
```



範例五：linspace用法 - 創建一段序列值，裡面的元素依據區域進行線性（平均）劃分 - linspace(起始值,結束值,幾個元素) 

```Python
np.linspace(0, 60, 4)
```

**執行結果**

```
array([ 0., 20., 40., 60.])
```



範例六：random.random用法 - 隨機分佈創建數組，隨機值的範圍會介於0～1之間，可以指定維度

```Python
np.random.random((3,3))
```

**執行結果**

```
array([[0.56615325, 0.38970791, 0.00862775],
       [0.11195201, 0.33505215, 0.82399896],
       [0.26902014, 0.421862  , 0.95621584]])
```





範例七：random.normal用法 - 正態分佈創建數組 - random.normal(均值,標準差,維度) 

```Python
np.random.normal(0, 1, (3,4))
```

**執行結果**

```
array([[ 0.67851712,  2.44478299,  0.32435313, -0.48474236],
       [-1.11346858, -0.73389409,  0.41083328,  1.50962971],
       [ 0.17242345,  0.87941494, -2.13275581, -0.52307737]])
```



範例八：random.randint用法 - 隨機整數創建數組，指定隨機數範圍與維度 

```Python
np.random.randint(0, 100, (6, 6))
```

**執行結果**

```
array([[55, 24, 67,  3, 33, 28],
       [70, 45, 33, 62, 91, 37],
       [37, 88, 12,  1, 50, 33],
       [62, 35, 51, 23, 43, 66],
       [53, 72, 61, 23,  9, 61],
       [18, 86, 14, 26, 43, 95]])
```



範例九：eye用法 - 創建一個為初始化的數組，數組元素的值保留為原有的內存空間值

```Python
np.eye(6)
```

**執行結果**

```
array([[1., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 1.]])
```



範例十: empty用法 - 創建一個為初始化的數組，數組元素的值，數組元素的值保留為原有的內存空間數值

```Python
np.empty(6)
```

**執行結果**

```
array([1., 1., 1., 1., 1., 1.])
```



### 8.NumPy中可以指定的標準數據類型



+ 由於NumPy數組只能包含一種數據類型，所以他的類型系統和Python並不同，因為對於每一種NumPy類型，它都需要包含著更詳細的類型資訊和限制 

+ NumPy是由C建構的，所以它的類型系統與C、Fortran一樣 



+ **指定數據類型的兩種寫法** 



使用'(類型)' 

```Python
np.zeros(10, dtype = 'int32')
```

**執行結果**

```
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```





或是np.(類型

```Python
np.zeros(10, dtype = np.int32)
```

**執行結果**

```
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
```



+ **類型圖表**

| 數據類型     | 說明                                                         |
| :----------- | :----------------------------------------------------------- |
| `bool_`      | Boolean (True or False) stored as a byte                     |
| `int_`       | Default integer type (same as C `long`; normally either `int64` or `int32`) |
| `intc`       | Identical to C `int` (normally `int32` or `int64`)           |
| `intp`       | Integer used for indexing (same as C `ssize_t`; normally either `int32` or `int64`) |
| `int8`       | Byte (-128 to 127)                                           |
| `int16`      | Integer (-32768 to 32767)                                    |
| `int32`      | Integer (-2147483648 to 2147483647)                          |
| `int64`      | Integer (-9223372036854775808 to 9223372036854775807)        |
| `uint8`      | Unsigned integer (0 to 255)                                  |
| `uint16`     | Unsigned integer (0 to 65535)                                |
| `uint32`     | Unsigned integer (0 to 4294967295)                           |
| `uint64`     | Unsigned integer (0 to 18446744073709551615)                 |
| `float_`     | Shorthand for `float64`.                                     |
| `float16`    | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa |
| `float32`    | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa |
| `float64`    | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa |
| `complex_`   | Shorthand for `complex128`.                                  |
| `complex64`  | Complex number, represented by two 32-bit floats             |
| `complex128` | Complex number, represented by two 64-bit floats             |











# NumPy的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - NumPy聚合操作 Aggregation - NumPy 廣播運算 Broadcasting - 如何操作布林數組，快速找到我們要的元素值Comparisons、Masks、Boolean Logic -筆記#6









## **2.4章 聚合: 最小值、最大值和其它 Aggregations: Min, Max, and Everything In Between**



一般來說，當我們處理大數據集時，第一步就是計算數據集的概要統計結果，而其中也許大家會覺得最重要的就是平均值和標準差，因為他們能歸納出數據集典型的數值，但其它的聚合函數也是相當有用的(像是求總和、乘積、中位值、最大與最小值、分位數等等)



而NumPy擁有非常快速的內建函數來幫助我們計算統計值



### 1. 數組的總和 Summing the Values in an Array



```Python
import numpy as np
```



+　Python內建方法 - sum



```Python
l = np.random.random(1000)
sum(l)
```

**執行結果**

```
491.5934377509918
```





+ NumPy內建方法 - np.sum

```Python
np.sum(l)
```

**執行結果**

```
491.5934377509914
```





+ Python - sum 和 NumPy - np.sum 效能上的比較

 

```Python
big_data_array = np.random.rand(100000000)
print("big data array = ", big_data_array)

%timeit sum(big_data_array)
%timeit np.sum(big_data_array)
```

**執行結果**

```
big data array =  [0.28905104 0.92034195 0.89446633 ... 0.79747072 0.86061536 0.4342236 ]
12.8 s ± 530 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
109 ms ± 729 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```





**結果: 從結果可以看出，由於NumPy函數是用編譯好的程式碼執行，所以它的計算性能遠遠比Python的sum快**



**提醒:** sum和np.sum並不完全相同，兩個函數的可選參數有不同的意義，而且np.sum函數可以處理多維數組的運算，接下來會提到





### 2. 最小值和最大值 Minimum & Maximum





+ Python內建方法 - min、max

```Python
min(big_data_array), max(big_data_array)
```

**執行結果**

```
(5.978993855570991e-09, 0.9999999987580884)
```



+　NumPy的內建方法 - np.min、np.max

```Python
np.min(big_data_array), np.max(big_data_array)
```

**執行結果**

```
(5.978993855570991e-09, 0.9999999987580884)
```



+　效能上的比較

```Python
%timeit max(big_data_array)
%timeit np.max(big_data_array)
```

**執行結果**

```
8.45 s ± 122 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
40.6 ms ± 658 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
```





+ min、max、sum和數種其它的NumPy聚合函數，可以有個更簡短的語法，就是使用自己ndarray物件來調用相應的方法

```Python
print(big_data_array.min(), big_data_array.max(), big_data_array.min())
```

**執行結果**

```
5.978993855570991e-09 0.9999999987580884 5.978993855570991e-09
```





### 3. 多維聚合 Multi Dimensional Aggregates



+ 一種常用的的聚合操作就是我們要沿著行(row)或列(column)來聚合，像是二維數組



```Python
d2 = np.random.random((4,4))
d2
```

**執行結果**

```
array([[0.59011653, 0.89146144, 0.98199896, 0.5765601 ],
       [0.01103124, 0.08254294, 0.62760219, 0.12193807],
       [0.00599072, 0.42766868, 0.19876466, 0.14475601],
       [0.63611429, 0.86594299, 0.67570599, 0.15769323]])
```





+　預設情況下，NumPy聚合函數會返回整個數組的聚合結果

```Python
d2.sum()
```

**執行結果**

```
6.995888060468155
```





+ 可以多加一個axis參數來指定一個軸，來讓函數沿著這個方向進行聚合運算，像是我們沿著行(row)的方向來計算每列的最小值，透過axis = 0



```Python
## 以行的方向，取每個列中的最小值
d2.min(axis = 0)
```

**執行結果**

```
array([0.00599072, 0.08254294, 0.19876466, 0.12193807])
```



+ 計算每一行(row)的最大值



```Python
## 以列的方向，取每個行中的最大值
d2.max(axis = 1)
```

**執行結果**

```
array([0.98199896, 0.62760219, 0.42766868, 0.86594299])
```



**重要觀念:**

上面這種指定axis參數的方式，會讓使用其它程式語言的使用者感到混淆，這邊的axis參數指定的是讓數組沿著這個方向進行壓縮，而不是指定它就是返回值的方向，因此指定axis=0代表第一個維度(行row)將會被壓縮，就是數組會沿著列column的方向進行聚合運算操作喔





### 4. 其他聚合函數 Other Aggregation Functions



+　**重要:** 很多的聚合函數都有一個NaN安全的版本，也就是它可以忽略缺失值(missing value)並計算出結果，NaN也定義為特殊IEEE浮點數非數值，而目前這個功能是在NumPy 1.8後加入的，所以比較就的版本是無法使用的喔



| 聚合函數名稱    | NaN-safe 版本      | 說明                                      |
| :-------------- | :----------------- | :---------------------------------------- |
| `np.sum`        | `np.nansum`        | 計算總和                                  |
| `np.prod`       | `np.nanprod`       | 計算乘積                                  |
| `np.mean`       | `np.nanmean`       | 計算平均值                                |
| `np.std`        | `np.nanstd`        | 計算標準差                                |
| `np.var`        | `np.nanvar`        | Compute variance                          |
| `np.min`        | `np.nanmin`        | Find minimum value                        |
| `np.max`        | `np.nanmax`        | Find maximum value                        |
| `np.argmin`     | `np.nanargmin`     | Find index of minimum value               |
| `np.argmax`     | `np.nanargmax`     | Find index of maximum value               |
| `np.median`     | `np.nanmedian`     | Compute median of elements                |
| `np.percentile` | `np.nanpercentile` | Compute rank-based statistics of elements |
| `np.any`        | N/A                | Evaluate whether any elements are true    |
| `np.all`        | N/A                | Evaluate whether all elements are true    |





## 2.5章 廣播 Broadcasting - 數組上的運算





### 1. 廣播 Broadcasting是什麼?



+ NumPy數組進行向量化操作的另一種方式

+ 廣播就是一整套用於不同大小或形狀的數組之間進行二元ufuncs運算(像是加法、減法、乘法等)的規則





### 2. 廣播介紹 Introducing Broadcasting



```Python
import numpy as np
```





+ 相同尺寸的數組進行運算: 會按每個元素進行計算

```Python
x = np.array([0, 1, 2, 3])
y = np.array([6, 6, 6, 6])
x + y
```

**執行結果**

```
array([6, 7, 8, 9])
```





+ 不同尺寸的數組進行運算: 像是我們可以把一個數組與一個標量相加(如下)，標量可以視為一個零為數組

```Python
x + 6
```

**執行結果**

```
array([6, 7, 8, 9])
```



**筆記:** 上面的結果，我們可以想像成運算首先會將標量擴展為一個一維數組[6,6,6,6]，然後再與x數組進行了加法運算，但其實NumPy的廣播方式並不是真的需要將源入複製然後擴展喔，這只是方便我們理解廣播是如何運作的





+ 不同尺寸的數組運算: 我們拿一個二維數組和一個一為數組來進行運算

```Python
d2 = np.ones((4,4))
d2
```

**執行結果**

```
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
```





```Python
x + d2
```

**執行結果**

```
array([[1., 2., 3., 4.],
       [1., 2., 3., 4.],
       [1., 2., 3., 4.],
       [1., 2., 3., 4.]])
```





結果: 一維數組x在第二個為肚上進行擴展，這樣才能與d2的形狀吻合





+ 不同尺寸的數組運算: 當兩個數組都需要進行廣播，才能符合彼此時



```Python
a = np.arange(6)
b = np.arange(4)[:, np.newaxis]

print(a)
print(b)
```

**執行結果**

```
[0 1 2 3 4 5]
[[0]
 [1]
 [2]
 [3]]
```







```Python
a + b
```

**執行結果**

```
array([[0, 1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5, 6],
       [2, 3, 4, 5, 6, 7],
       [3, 4, 5, 6, 7, 8]])
```





+　下圖是廣播運作的原理圖



![Broadcasting Visual](https://jakevdp.github.io/PythonDataScienceHandbook/figures/02.05-broadcasting.png)

圖片來源: 書本



圖片補充說明: 淺色的格子是廣播後的值，這邊要強調廣播的值不會真的佔用內存，會在圖中出現只是方便我們能夠了解運作原理



### 3. 廣播的規則 Rules Of Broadcasting



NumPy使用廣播是需要嚴格遵守一套規則的



+　規則1: 如果兩個數組有著不同的維度，則維度較低的數組會沿著最前(左)的維度進行填充，使兩個數組的維度一樣

+　規則2: 如果兩個數組的形狀在任何維度上都存在不相同，那麼兩個數組中形狀(shape)為1的維度都會廣播到另一個數組對應的尺寸大小，最後兩個數組就會具有相同的維度

+　規則3: 如果兩個數組在同一個為肚上有不為1的不同長度，將會產生報錯





#### 廣播規則 範例一: 只有一個數組需要廣播的狀況



+ 有一個二維數組和一個一維數組相加

```Python
d2 = np.ones((2, 3))
x = np.arange(3)

print(d2)
print(x)
```

**執行結果**

```
[[1. 1. 1.]
 [1. 1. 1.]]
[0 1 2]
```





+ 檢視一下兩個數組的形狀

```
print(d2.shape)
print(x.shape)
```

**執行結果**

```
(2, 3)
(3,)
```





+ **依據規則1 :** 數組x的維度較低，所以要對其進行為杜的擴增，在它的最前(左)邊增加一個維度，兩個數組的形狀變為

```
d2.shape -> (2, 3)

x.shape -> (1,3)
```





+ **依據規則2 :** 可以看出兩個數組在第一維度上不相同，因為我們將具有長度1的x數組，x數組的第一維度擴展為2，讓雙方的形狀變成:

```
d2.shape -> (2,3)
x.shape -> (2,3)
```



經過一連串的轉換後，兩個數組的形狀一致，就可以進行加法運算囉

```Python
d2 + x
```

**執行結果**

```
array([[1., 2., 3.],
       [1., 2., 3.]])
```





#### 廣播的規則 範例二: 兩個數組都需要廣播的狀況



+ 兩個數組

```Python
x = np.arange(3).reshape((3,1))
y = np.arange(3)

print(x)
print(y)
```

**執行結果**

```
[[0]
 [1]
 [2]]
[0 1 2]
```





+ 兩個數組的形狀

```Python
print(x.shape)
print(y.shape)
```

**執行結果**

```
(3, 1)
(3,)
```





+ **規則1 :** 將數組y擴增一個維度， 長度為1

```
x.shape -> (3, 1)
y.shape -> (1, 3)
```





+ **規則2 :** 除了將數組x的第二維度擴展為3，還需要數組y的第一維度擴展為3

```
x.shape -> (3, 3)
y.shape -> (3, 3)
```





+ 兩個數組形狀相同後，開始進行加法計算

  

```Python
x + y
```

**執行結果**

```
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])
```



#### 廣播的規則 範例三: 不適用廣播的例子



+　兩個數組

```Python
d2 = np.ones((3,2))
x = np.arange(3)


print(d2)
print(x)
```

**執行結果**

```
[[1. 1.]
 [1. 1.]
 [1. 1.]]
[0 1 2]
```



+ **規則1:** 將數組x的第一維度進行擴增，長度為1

```
d2.shape -> (3, 2)
x.shape -> (1, 3)
```

**印出大小**

```Python
print(d2.shape)
print(x.shape)
```

**執行結果**

```
(3, 2)
(3,)
```





+ **規則2:** 將數組x的第一維度擴增為3，來讓第一維度與d2一樣，但是第二維度卻不能擴充，因為要長度為1才能進行擴增

```
d2.shape -> (3, 2)
x.shape -> (1, 3)
```





+ 規則3: 因為兩個數組在兩個維度是的長度有所不同，而且也都不為1(只有1能擴增)，都不能擴增的情況下系統會報錯

```Python
d2 + x
```

**執行結果**

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-107-1cd3226c483f> in <module>
----> 1 d2 + x

ValueError: operands could not be broadcast together with shapes (3,2) (3,) 
```





+ 疑問: 如果不按照規則1，也就是廣播的時候不是在最前(左邊)面進行擴增的話，不就可以解決很多數組的運算問題?



也就是說如果舉上面的例子，我們在數組x的第二維度擴增的話，就不會有這個錯誤問題了，但是廣播(Broadcasting)不支援這種處理方式，雖然在某些狀況下會更加彈性，但是會帶來不確定性





+ 如果硬要進行右邊擴增的話: 可以使用np.newaxis來處理



```Python
x[:, np.newaxis].shape
```

**執行結果**

```
(3, 1)
```



```Python
d2 + x[:, np.newaxis]
```

**執行結果**

```
array([[1., 1.],
       [2., 2.],
       [3., 3.]])
```





#### 更多的廣播應用

上面的例子都使用加法來運算，但實際上廣播(Broadcasting)可以應用在任何的二元ufunc上



+ 範例: logaddexp函數運算，也就是計算log(exp(a) + exp(b))，使用這個函數比使用原本的exp和log函數進行運算的時候來的更加精確



```Python
np.logaddexp(d2, x[:, np.newaxis])
```

**執行結果**

```
array([[1.31326169, 1.31326169],
       [1.69314718, 1.69314718],
       [2.31326169, 2.31326169]])
```





# NumPy的各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - NumPy聚合操作 Aggregation - NumPy 廣播運算 Broadcasting - 如何操作布林數組，快速找到我們要的元素值Comparisons、Masks、Boolean Logic -筆記#7





這篇是延續上一篇2.5章後面的內容喔，因為太'長了，所以我把它切成兩部分來說明喔



## 2.5章 廣播 Broadcasting - 數組上的運算





### 4. 廣播 實作 - 中心化方法



+ 我們已經知道ufuncs提供了可以避免使用Python循環低效的方式，然而廣播大大地擴展了這個能力

+ 舉例: 數據中心化(Centering an array)



+ 例子: 假設我們進行10次採樣，每次都會得到3個數據值

```Python
import numpy as np

X = np.random.random((10,3))
X
```

**執行結果**

```
array([[0.61395157, 0.63672235, 0.2819929 ],
       [0.01319829, 0.76408163, 0.3923268 ],
       [0.49654391, 0.48526054, 0.80337583],
       [0.52355967, 0.65514011, 0.77710867],
       [0.38722043, 0.45083486, 0.33298208],
       [0.31160497, 0.17435645, 0.32452177],
       [0.58727465, 0.97500597, 0.42886587],
       [0.99165537, 0.43683679, 0.51030536],
       [0.80680708, 0.52657516, 0.38738793],
       [0.81282071, 0.7912729 , 0.127596  ]])
```







+ mean: 使用mean函數來沿著第一個維度求出美個特徵的平均值

```Python
## 根據列來取平均值，也就是每個特徵的平均值
Xmean = X.mean(axis = 0)
Xmean
```

**執行結果**

```
array([0.55446366, 0.58960868, 0.43664632])
```



+ 中心化: 將原本數據的個元素減掉平均值，就可以將數據集中心化(這邊就是一個廣播操作的例子)

```Python
## 中心化
X_centered = X - Xmean
X_centered
```

**執行結果**

```
array([[ 0.05948791,  0.04711367, -0.15465342],
       [-0.54126537,  0.17447295, -0.04431952],
       [-0.05791976, -0.10434814,  0.36672951],
       [-0.030904  ,  0.06553143,  0.34046235],
       [-0.16724324, -0.13877381, -0.10366424],
       [-0.24285869, -0.41525222, -0.11212455],
       [ 0.03281098,  0.3853973 , -0.00778045],
       [ 0.4371917 , -0.15277188,  0.07365904],
       [ 0.25234341, -0.06303352, -0.04925839],
       [ 0.25835705,  0.20166423, -0.30905032]])
```





+ 檢查結果的正確性: 透過查看進行中心化後的數組在各特徵上的平均值是否夠接近於0

```Python
## 根據列來取平均值
X_centered.mean(0)
```

**執行結果**

```
array([ 4.44089210e-17,  5.55111512e-17, -8.88178420e-17])
```





+ 結果: 根據機器準確度(machine precision)的情況，平均值已經是等於0了





### 5. 視覺化 - 廣播應用於二維函數來顯示圖像



+ 廣播有一個非常有用的地方，就是根據二維函數來顯示圖像

+ 舉例: 如果我們要定義一個函數z = f(x, y) ，就可以使用廣播(Broadcasting)來計算整個網路中的函數



```Python
## 創建x和y數據資料 從0到5，總共有50步
x = np.linspace(0, 5, 50)
## [:, np.newaxis]改變形狀: 垂直
y = np.linspace(0, 5, 50)[:, np.newaxis]

## z 值公式
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
```



**視覺化**

```Python
## 視覺化
## 導入視覺化套件
%matplotlib inline
import matplotlib.pyplot as plt

## 顯示圖像
plt.imshow(z, origin = 'lower',
           extent = [0, 5, 0, 5],
           cmap = 'viridis_r')

## 顯示顏色對應數值條
plt.colorbar()
```

**執行結果**

![2.5.1](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\NumPy\images\2.5.1.PNG)





## 2.6章 比較、遮蓋和布林邏輯 Comparison, Masks, and Boolean Logic





### 1. 布林遮蓋(掩碼) Boolean Masks 是什麼?



+ 當想透過一些表準條件來對數組中的元素值進行提取、修改、技術或著其他操作時，我們就需要用到遮蓋(Masks)



+ 舉例: 當我們希望計算大於某個特定值的元素個數，或著刪除高於某個閾值的異常值(離群值)，在NumPy當中，就會使用布林遮蓋Boolean Masks來達成



### 2. 實作 - 計算下雨的天數 - 上半部



**這邊使用的是書本中，作者所提供的2014西雅圖的每天將與統計數據**



+ 載入數據集

```Python
## 導入所需套件
import numpy as np
import pandas as pd

## 載入數據集
dataset = pd.read_csv('dataset/Seattle2014.csv')

## 顯示數據集
dataset

```



![2.6.1](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\NumPy\images\2.6.1.PNG)





+ 取出降雨量欄位的所有元素值，並准換單位為英寸

```Python
## 取出降雨量的元素值，並組成NumPy Array
rainfall = dataset['PRCP'].values
# print(rainfall)

## 將單位轉換成英寸 inches: 1/10mm -> inches
inches = rainfall / 254.0
# print(inches)

## 查看大小
print(inches.shape)
```

**執行結果**

```
(365,)
```





這個數組共有365個值，代表西雅圖一年365天的降雨(單位為英寸: inches)





**視覺化: 使用直方圖來視覺化出降玉天數的分布情況**



```Python
## 導入視覺化套件
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


## 畫出直方圖 後面的60是bins參數:表示總共有幾條直方 
plt.hist(inches, 60)
```

**執行結果**





![2.6.4](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\NumPy\images\2.6.4.PNG)





+ 上面的視覺化幫助我們概略的了解了這個數據集，但是這張圖並沒有幫助我們得到更多的資訊，像是一年中有多少天在下雨?下雨的日子中降水量的平均值是多少?一年中有多少降雨量超過半英寸?





### 3. UFuncs 比較運算符 - NumPy中用來遮蓋(Masks)的通用工具



+ 之前介紹UFuncs的章節，只介紹了算數運算符(+、-、*、/等等)，來對數組進行逐個元素的計算操作
+ NumPy也可以實現比較運算符(>大於、<小於)的ufuncs，這些比較運算符的結果一定是布林值(True or False)數組



```Python
a = np.array([1,2,3,4,5,6])
```

```Python
a < 3.5
## array([ True,  True,  True, False, False, False])
```

```Python
a > 3.5
## array([False, False, False,  True,  True,  True])
```

```Python
a >= 3.5
## array([False, False, False,  True,  True,  True])
```

```Python
a <= 3.5
## array([ True,  True,  True, False, False, False])
```

```Python
a != 3
## array([ True,  True, False,  True,  True,  True])
```

```Python
a == 3
## array([False, False,  True, False, False, False])
```









+ 更多應用: 也可以將兩個數組的元素逐個進行比較，支援運算的組合操作比較



```Python
4 * a == a ** 2
## array([False, False, False,  True, False, False])
```







+ 圖表為比較運算符的簡潔寫法和其對應的ufuncs寫法



| 比較符 | 相對應的UFuncs |      | 比較符 | 相對應的UFuncs     |
| :----- | :------------- | :--- | :----- | :----------------- |
| `==`   | `np.equal`     |      | `!=`   | `np.not_equal`     |
| `<`    | `np.less`      |      | `<=`   | `np.less_equal`    |
| `>`    | `np.greater`   |      | `>=`   | `np.greater_equal` |







+ 比較運算符也可以應用在任何形狀(shape)的數組上喔



```Python
## RandomState: 控制隨機的方式
## 如果跟我一樣設2 就會生成一樣的二為數組喔
rng = np.random.RandomState(2)
x = rng.randint(10, size = (3, 5))
x
```

```
## 執行結果
array([[8, 8, 6, 2, 8],
       [7, 2, 1, 5, 4],
       [4, 5, 7, 3, 6]])
```





```Python
x >= 5
```

```
## 執行結果
array([[ True,  True,  True, False,  True],
       [ True, False, False,  True, False],
       [False,  True,  True, False,  True]])
```









**重要觀念: 比較運算符的結果都為布林型的數組，而NumPy提供了眾多可以操作這類型數組的函數**



 



### 4. 操作布林數組 Working with Boolean Arrays - <、>、==、<=、>=、!=



當我們透過UFuncs比較符號計算出一個布林數組時，接下來我們需要對這個布林數組進行一些運算操作，來得到更多數據的資訊





+ 創建一個二維數組



```Python
## RandomState: 控制隨機的方式
## 如果跟我一樣設2 就會生成一樣的二為數組喔
rng = np.random.RandomState(2)
a = rng.randint(10, size = (3, 5))
a
```

**執行結果**

```
array([[8, 8, 6, 2, 8],
       [7, 2, 1, 5, 4],
       [4, 5, 7, 3, 6]])
```



#### np.count_nonzero - 計算為數組中True的數量 

```Python
## 計算多少值低於7
np.count_nonzero(a < 7) # 10
```







結果: 從結果可以看出小於7的元素共有十個，另一種用來獲取這種資訊的方式是np.sum







#### np.sum - 計算為數組中指定條件的元素數量



+ 操作原理: 把符合與不符合條件的元素標記為True或False，False會被當成是0，而True會被當成是1，然後相加就會得到True的數量

```Python
## 計算多少值低於7
np.sum(a < 7) # 10
```



+ 優點: 使用np.sum的好處在也可以根據行或列來進行計算



+ 根據行來找尋小於7的元素數量



```Python
## 每一行中小於7的元素數量
np.sum(a < 7, axis = 1)
```

**執行結果**

```
array([2, 4, 4])
```





#### np.any & np.all - 用來檢查當我們有任何一個或全部都為True(符合條件)的值



 ```Python
## RandomState: 控制隨機的方式
## 如果跟我一樣設2 就會生成一樣的二為數組喔
rng = np.random.RandomState(2)
a = rng.randint(10, size = (3, 5))
a
 ```

**執行結果**

```
array([[8, 8, 6, 2, 8],
       [7, 2, 1, 5, 4],
       [4, 5, 7, 3, 6]])
```



+ np.any & np.all用法

```Python
## 有模有任何一個值大於9
np.any(a > 9)  # False
```



```Python
## 有沒有任何一個值小於2
np.any(a < 2) # True
```



```Python
## 是不是所有的元素都小於9
np.all(a < 10) # True
```



```Python
## 是不是所有值都不等於7
np.all(a != 7) # False
```





+ np.any 和 np.all 也可以根據特定的軸進行運算喔



```Python
## 是不是每一行都所有元素值都大於6
np.all(x > 2, axis = 1)
```

**執行結果**

```
array([False, False,  True])
```



前兩行都不是全部元素都大於2，只有第三行的元素都大於2





#### 重點提醒

Python也有內建的sum()、any()、all()函數，但他們與NumPy相對應的函數有著不同的語法，尤其是計算多維數組的時候，可能報錯或無法預料的結果





### 實作 - 計算下雨的天數 - 下半部

接下來的實作都會使用這個數據集當例子喔





### 5. 布林操作符 - Boolean Operators - 按位邏輯運算符 Bitwise Logic Operators、& 、|、^、~ 





我們能夠透過前面教的計算操作知道，有多少天雨量少於4 inches，或是多少天雨量大於2inches，但是我們接下來想知道的是多少天雨量少於6 inches且大於2inches?



+ Python的方法: 這時候就需要透過Python的按位邏輯運算符(bitwise logic operators)、&、|、^和~來達成

+ NumPy的方法: NumPy將上面的Python方法重載到UFuncs裡面，來對數組(通常是布林數組)中每個元素進行操作





+ 前面轉換成英寸的降雨量數據

```Python
## 每天的降雨量數據
inches
```

**執行結果**

```
array([0.        , 0.16141732, 0.05905512, 0.        , 0.        ,
       0.01181102, 0.48031496, 0.38188976, 0.22834646, 0.16929134,
       0.83858268, 0.05905512, 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.01968504, 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.3503937 , 0.8503937 , 0.        ,
       0.09055118, 0.07874016, 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.2007874 , 0.01968504,
       0.72047244, 0.66929134, 0.18110236, 0.07086614, 0.37007874,
       0.46062992, 1.03937008, 0.57086614, 0.5984252 , 0.03937008,
       0.11811024, 0.11023622, 0.0984252 , 0.24015748, 0.51181102,
       0.01181102, 0.        , 0.        , 0.        , 0.01968504,
       0.7519685 , 0.42125984, 0.6496063 , 1.83858268, 0.11811024,
       0.        , 1.27165354, 0.16929134, 0.74015748, 0.        ,
       0.        , 0.01968504, 0.27165354, 0.31889764, 1.09055118,
       0.01181102, 0.        , 0.01968504, 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.16141732, 0.14173228,
       0.01181102, 0.87007874, 0.5511811 , 0.        , 0.        ,
       0.        , 0.        , 0.0984252 , 0.        , 0.18110236,
       0.        , 0.        , 0.18110236, 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.01968504,
       0.42913386, 0.72834646, 0.        , 0.53937008, 0.        ,
       0.2007874 , 0.55905512, 0.3503937 , 0.48818898, 0.        ,
       0.12992126, 0.27165354, 0.        , 0.        , 0.        ,
       0.        , 0.        , 1.31102362, 0.62992126, 0.2007874 ,
       0.        , 0.        , 0.53937008, 0.07874016, 0.01968504,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.1496063 , 0.        , 0.22047244,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.07086614, 0.2519685 , 0.        ,
       0.01968504, 0.14173228, 0.0511811 , 0.        , 0.03149606,
       0.01181102, 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.07086614, 0.09055118, 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.01181102, 0.75984252, 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.01968504, 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.01968504, 0.5       , 0.8503937 ,
       0.        , 0.03937008, 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.33070866, 0.0511811 , 0.        , 0.11811024,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.01968504,
       0.01181102, 0.        , 0.        , 0.        , 0.01181102,
       0.72047244, 0.7992126 , 0.16929134, 0.3503937 , 0.        ,
       0.        , 0.03149606, 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.01181102, 0.29133858, 0.        ,
       0.2992126 , 0.27952756, 0.33858268, 0.        , 0.12992126,
       0.59055118, 0.        , 0.46062992, 0.03937008, 1.25984252,
       0.37007874, 0.16141732, 0.24015748, 0.05905512, 0.03149606,
       0.5       , 0.01968504, 1.        , 0.66929134, 0.        ,
       0.07086614, 0.42913386, 0.16141732, 0.18897638, 0.16141732,
       0.        , 0.        , 0.2007874 , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.        , 0.        , 0.        , 0.14173228, 0.5984252 ,
       0.01968504, 0.46850394, 0.0511811 , 0.72047244, 0.01181102,
       0.12992126, 1.3503937 , 0.14173228, 0.        , 0.        ,
       0.        , 0.        , 0.03149606, 0.11811024, 0.29133858,
       0.        , 0.35826772, 0.38976378, 0.51181102, 0.27165354,
       0.        , 0.        , 0.        , 0.        , 0.        ,
       0.11023622, 0.51181102, 0.11811024, 0.77165354, 0.        ,
       0.        , 0.81102362, 0.20866142, 0.        , 0.        ,
       0.12992126, 0.16141732, 0.        , 0.        , 0.        ])
```





+ 有多少天降雨量介於0.5 inches到1 inches之間

```Python
## 找出大於0.5且小於1的元素值
##print((inches > 0.5) & (inches < 1))

## 統計True的個數，統計符合大於0.5且小於1的元素值
np.sum((inches > 0.5) & (inches < 1)) # 29
```





+ 統計不符合大於1或是小於等於0.5的元素值的數量



```Python
## 找出大於1或是小於等於0.5的元素值
##print((inches > 1) | (inches <= 0.5))

## 將上面的條件相反過來 - 取not，也就是不符合大於1或是小於等於0.5的元素值
##print(~((inches > 1) | (inches <= 0.5)))

## 計算True的數量，統計不符合大於1或是小於等於0.5的元素值的數量
np.sum(~((inches > 1) | (inches <= 0.5))) # 30
```







+ 圖表: 符號對應UFuncs表

| 符號 | 等同於UFuncs     |      | 符號 | 等同於UFuncs     |
| :--- | :--------------- | :--- | :--- | :--------------- |
| `&`  | `np.bitwise_and` |      | \|   | `np.bitwise_or`  |
| `^`  | `np.bitwise_xor` |      | `~`  | `np.bitwise_not` |







+ 統計各種條件



```Python
print('沒有降雨的天數: ', np.sum(inches == 0))
print('有降雨的天數: ', np.sum(inches != 0))
print('降雨量大於0.6 inches的天數: ', np.sum(inches > 0.6))
print('降雨量介於0.2到0.6之間的天數: ', np.sum((inches > 0.2) & (inches < 0.6)))
```

**執行結果**

```
沒有降雨的天數:  215
有降雨的天數:  150
降雨量大於0.6 inches的天數:  26
降雨量介於0.2到0.6之間的天數:  49
```







### 6. 遮蓋 - 布林數組 Boolean Arrays as Masks - 直接返回符合條件的元素值，而不是返回True或False



#### 舉例 : 我們想知道數組中所有大於5的元素值有哪些?



+ 創建一個二維數組

```Python
## RandomState: 控制隨機的方式
## 如果跟我一樣設2 就會生成一樣的二為數組喔
rng = np.random.RandomState(2)
a = rng.randint(10, size = (3, 5))
a
```

**執行結果**

```
array([[8, 8, 6, 2, 8],
       [7, 2, 1, 5, 4],
       [4, 5, 7, 3, 6]])
```







+ 找出符合條件的有幾個元素

```Python
## 大於5的元素值，返回布林數組
a > 5
```

**執行結果**

```
array([[ True,  True,  True, False,  True],
       [ True, False, False, False, False],
       [False, False,  True, False,  True]])
```







+ 找出符合條件的元素值

```Python
## 大於5的元素值，返回一維數組裝載符合條的的元素值
a[a > 5]
```

**執行結果**

```
array([8, 8, 6, 8, 7, 7, 6])
```





利用剛剛建立好的布林數組當作索引，來對原數組進行搜尋，找到所有對應True的元數值





**結果: 傳回一個一維數組，裡面裝載著滿足設定條件的元素值; 也就是說，掩碼數組(Mask Array)為True的位置中的所有值喔**



+ 利用這個遮蓋(Masks)方法，來對我們的降雨數據進行各種統計操作



```Python
## 建構一個下雨天的遮蓋(Mask)
rainy = (inches > 0)

## 建構一個晴天的遮蓋(Mask) - 6/21號是第172天
days = np.arange(365)
summer = (days > 172) & (days < 262)


print("2014年下雨天的中位(Median Precip)降雨量: ", np.median(inches[rainy]))
print("2014年晴天的中位(Median Precip)降雨量: ", np.median(inches[summer]))
print("2014年晴天的最大(Max Precip)降雨量:　", np.max(inches[summer]))
print('2014年不為晴天的中位(Median Precip)降雨量: ', np.median(inches[rainy & ~summer]))
```

**執行結果**

```
2014年下雨天的中位(Median Precip)降雨量:  0.19488188976377951
2014年晴天的中位(Median Precip)降雨量:  0.0
2014年晴天的最大(Max Precip)降雨量:　 0.8503937007874016
2014年不為晴天的中位(Median Precip)降雨量:  0.20078740157480315
```



結合了布林操作、遮蓋操作和聚合，我們可以從數據集中得到更多的統計資訊





### 7. 關鍵字 and/or vs &/|



#### 疑問: 使用and/or，和使用&/|的差別?



+ and/or: 測量整個對象(object)的真假

+ &/|: 引用對象中的每個位(bits)





+ 每當使用and或or時，等同於要求Python將物件(object)視為單個布林實體

```Python
bool(66), bool(0) # (True, False)
```

```Python
bool(66 and 0) # False
```

```Python
bool(66 or 0) # True
```





+ 在Python中，所有非零整數都將估計為True





+　當使用&和|在整數上時，表達式會對元素的位(bit)進行運算，簡單來說會對每個位(bits)進行and或or計算 - ex.1and0 會等於0(False)，而1or0會等於1(True)



```Python
bin(68) # '0b1000100'
```

```Python
bin(58) # '0b111010'
```

```Python
bin(55 & 66) # '0b1110111'
```



重要提醒: 比較了二進制表示刑事的相應位，來得出結果





+ 當我們在NumPy中有布林數組，我們可以將它視為一個0和1組成的字符串，1代表True，而0代表False，然後使用&和|來得到結果



```Python
a = np.array([1,0,0,1,1,1,0,0,0,1], dtype = bool)
b = np.array([0,1,0,1,0,0,1,1,1,0], dtype = bool)

a | b
```

**執行結果**

```
array([ True,  True, False,  True,  True,  True,  True,  True,  True,
        True])
```





+ 如果使用or來評估整個物件(object)的真假，但這不是一個明確定義的值

```Python
a or b
```

**執行結果**

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-98-51429399a6cf> in <module>
----> 1 a or b

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```

+ 結果: 在給定數組上執行布林表達式時，應該要使用|或是&，而不是使用and和or



```Python
x = np.arange(10)
(x > 3) & (x < 9)
```

**執行結果**

```
array([False, False, False, False,  True,  True,  True,  True,  True,
       False])
```



+ 使用and來評估整個數組的真實性或是虛假性會給我們帶來與之間結果相同的錯誤- ValueError

```Python
(x > 3) and (x <9)
```

**執行結果**

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-104-0b2c6dfa091b> in <module>
----> 1 (x > 3) and (x <9)

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
```





#### 結論

+ and/or: 測量整個對象(object)的真假

+ &/|: 引用對象中的每個位(bits)

對於NumPy中的布林數組，通常都會使用&和|來進行操作





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

![2.7.1](C:/Users/user/Desktop/Book/Python-Data-Science-Handbook-Personal-Note/NumPy/images/2.7.1.PNG)



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

![2.7.2](C:/Users/user/Desktop/Book/Python-Data-Science-Handbook-Personal-Note/NumPy/images/2.7.2.PNG)



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

![2.7.3](C:/Users/user/Desktop/Book/Python-Data-Science-Handbook-Personal-Note/NumPy/images/2.7.3.PNG)



+ 如果每次繪製直方圖時都必須這樣做是很麻煩的，這也就是Matplotlib提供plt.hits()例程的原因，該例程在一行中達到與上面一樣的操作

```Python
## 視覺化 採用np.hist
plt.hist(x, bins, histtype = 'step')
```

**執行結果**

![2.7.4](C:/Users/user/Desktop/Book/Python-Data-Science-Handbook-Personal-Note/NumPy/images/2.7.4.PNG)



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

**執行結果**

```
array([2, 1, 2, 3, 6, 7, 8, 9, 8])
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

**執行結果**

```
[[8 8 6 2 8 7]
 [2 1 5 4 4 5]
 [7 3 6 4 3 7]
 [6 1 3 5 8 4]]
```

```
array([[2, 6, 7, 8, 8, 8],
       [1, 2, 4, 4, 5, 5],
       [3, 3, 4, 6, 7, 7],
       [1, 3, 4, 5, 6, 8]])
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

**執行結果**

```
array([[0.50952588, 0.21726993],
       [0.99326629, 0.31529748],
       [0.25873317, 0.80917529],
       [0.35367538, 0.46784249],
       [0.27417326, 0.79820039],
       [0.81413841, 0.94809042],
       [0.82288464, 0.51513912],
       [0.22099815, 0.74663141],
       [0.43153777, 0.88830375],
       [0.9411933 , 0.50301225]])
```



**視覺化**

```Python
## 視覺化
%matplotlib inline
import matplotlib.pyplot as plt
## 設定風格
import seaborn; seaborn.set()


## 繪製散點圖
plt.scatter(x[:, 0], x[:, 1], s = 100)
```

**執行結果**

![2.8.1](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\NumPy\images\2.8.1.PNG)









+ **STEP2:** 計算每兩個點之間的距離，距離平方的公式是兩點坐標差的平方和

應用廣播(Broaadcasting)和聚合(Aggregation)，我們只需要使用一行程式碼就能完成

```Python
## 計算每兩個點間的距離
dist_sq = np.sum((x[:, np.newaxis, :] - x[np.newaxis, :, :]) ** 2, axis = -1)
dist_sq
```

**執行結果**

```
array([[0.00000000e+00, 2.43614193e-01, 4.13248936e-01, 8.70759890e-02,
        3.92871055e-01, 6.26887394e-01, 1.86919772e-01, 3.63471825e-01,
        4.56368536e-01, 2.67985446e-01],
       [2.43614193e-01, 0.00000000e+00, 7.83454195e-01, 4.32346520e-01,
        7.50290010e-01, 4.32513704e-01, 6.89665890e-02, 7.82447038e-01,
        6.43875118e-01, 3.79484320e-02],
       [4.13248936e-01, 7.83454195e-01, 0.00000000e+00, 1.25522098e-01,
        3.58844705e-04, 3.27772397e-01, 4.04724146e-01, 5.33566825e-03,
        3.61227431e-02, 5.59487636e-01],
       [8.70759890e-02, 4.32346520e-01, 1.25522098e-01, 0.00000000e+00,
        1.15456925e-01, 4.42664279e-01, 2.22394302e-01, 9.53265051e-02,
        1.82850220e-01, 3.46414225e-01],
       [3.92871055e-01, 7.50290010e-01, 3.58844705e-04, 1.15456925e-01,
        0.00000000e+00, 3.14029390e-01, 3.81207861e-01, 5.48695158e-03,
        3.28822050e-02, 5.32051776e-01],
       [6.26887394e-01, 4.32513704e-01, 3.27772397e-01, 4.42664279e-01,
        3.14029390e-01, 0.00000000e+00, 1.87523326e-01, 3.92401102e-01,
        1.49957698e-01, 2.14237522e-01],
       [1.86919772e-01, 6.89665890e-02, 4.04724146e-01, 2.22394302e-01,
        3.81207861e-01, 1.87523326e-01, 0.00000000e+00, 4.15856022e-01,
        2.92404213e-01, 1.41440010e-02],
       [3.63471825e-01, 7.82447038e-01, 5.33566825e-03, 9.53265051e-02,
        5.48695158e-03, 3.92401102e-01, 4.15856022e-01, 0.00000000e+00,
        6.43979825e-02, 5.78031349e-01],
       [4.56368536e-01, 6.43875118e-01, 3.61227431e-02, 1.82850220e-01,
        3.28822050e-02, 1.49957698e-01, 2.92404213e-01, 6.43979825e-02,
        0.00000000e+00, 4.08198301e-01],
       [2.67985446e-01, 3.79484320e-02, 5.59487636e-01, 3.46414225e-01,
        5.32051776e-01, 2.14237522e-01, 1.41440010e-02, 5.78031349e-01,
        4.08198301e-01, 0.00000000e+00]])
```







+ **拆解上面的方法:** 上面那行的程式碼可能很難直接理解，所以這邊將一步一步解釋

```Python
## 計算每兩個點之間的坐標距離
## differences = x[:, np.newaxis] - x[np.newaxis, :] 我自己實驗覺得與書本計算結果一樣
differences = x[:, np.newaxis, :] - x[np.newaxis, :, :]
# print(differences)
differences.shape
```

**執行結果**

```
(10, 10, 2)
```





+ 計算距離的平方

```Python
## 計算距離的平方
sq_difference = differences ** 2
# print(sq_difference)
sq_difference.shape
```

**執行結果**

```
(10, 10, 2)
```





+ 按照最後一個維度求和

```Python
## 按照最後一個維度求和
dist_sq = sq_difference.sum(-1)
dist_sq
```

**執行結果**

```
array([[0.00000000e+00, 2.43614193e-01, 4.13248936e-01, 8.70759890e-02,
        3.92871055e-01, 6.26887394e-01, 1.86919772e-01, 3.63471825e-01,
        4.56368536e-01, 2.67985446e-01],
       [2.43614193e-01, 0.00000000e+00, 7.83454195e-01, 4.32346520e-01,
        7.50290010e-01, 4.32513704e-01, 6.89665890e-02, 7.82447038e-01,
        6.43875118e-01, 3.79484320e-02],
       [4.13248936e-01, 7.83454195e-01, 0.00000000e+00, 1.25522098e-01,
        3.58844705e-04, 3.27772397e-01, 4.04724146e-01, 5.33566825e-03,
        3.61227431e-02, 5.59487636e-01],
       [8.70759890e-02, 4.32346520e-01, 1.25522098e-01, 0.00000000e+00,
        1.15456925e-01, 4.42664279e-01, 2.22394302e-01, 9.53265051e-02,
        1.82850220e-01, 3.46414225e-01],
       [3.92871055e-01, 7.50290010e-01, 3.58844705e-04, 1.15456925e-01,
        0.00000000e+00, 3.14029390e-01, 3.81207861e-01, 5.48695158e-03,
        3.28822050e-02, 5.32051776e-01],
       [6.26887394e-01, 4.32513704e-01, 3.27772397e-01, 4.42664279e-01,
        3.14029390e-01, 0.00000000e+00, 1.87523326e-01, 3.92401102e-01,
        1.49957698e-01, 2.14237522e-01],
       [1.86919772e-01, 6.89665890e-02, 4.04724146e-01, 2.22394302e-01,
        3.81207861e-01, 1.87523326e-01, 0.00000000e+00, 4.15856022e-01,
        2.92404213e-01, 1.41440010e-02],
       [3.63471825e-01, 7.82447038e-01, 5.33566825e-03, 9.53265051e-02,
        5.48695158e-03, 3.92401102e-01, 4.15856022e-01, 0.00000000e+00,
        6.43979825e-02, 5.78031349e-01],
       [4.56368536e-01, 6.43875118e-01, 3.61227431e-02, 1.82850220e-01,
        3.28822050e-02, 1.49957698e-01, 2.92404213e-01, 6.43979825e-02,
        0.00000000e+00, 4.08198301e-01],
       [2.67985446e-01, 3.79484320e-02, 5.59487636e-01, 3.46414225e-01,
        5.32051776e-01, 2.14237522e-01, 1.41440010e-02, 5.78031349e-01,
        4.08198301e-01, 0.00000000e+00]])
```





+ 檢查這個舉的對角線元素，對角線的原數值是點與其自身的距離平方，應該要都為0

```Python
## 檢查對角線元素值
dist_sq.diagonal()
```

**執行結果**

```
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```





+ **STEP3 :** 上面得到了距離平方矩陣，接著就可以使用np.argsort函數來按照每行進行排序，最左邊的列會給出每個數據點的最近鄰(Nearest Neighbor)

```Python
nearest = np.argsort(dist_sq, axis = 1)
print(nearest)
```

**執行結果**

```
[[0 3 6 1 9 7 4 2 8 5]
 [1 9 6 0 3 5 8 4 7 2]
 [2 4 7 8 3 5 6 0 9 1]
 [3 0 7 4 2 8 6 9 1 5]
 [4 2 7 8 3 5 6 0 9 1]
 [5 8 6 9 4 2 7 1 3 0]
 [6 9 1 0 5 3 8 4 2 7]
 [7 2 4 8 3 0 5 6 9 1]
 [8 4 2 7 5 3 6 9 0 1]
 [9 6 1 5 0 3 8 4 2 7]]
```



+ 結果中的第一列是0到9的數字: 因為每個點最近的的點當然是自己



這邊對數據點位置進行了完整的排序，但其實我們不需要這樣做，如果我們只對最近的K個鄰居有興趣的話，可以使用分區(Partition)來完成





+ **STEP4 :** 我們想知道最近的K個鄰居，為哪些數據點，只要在距離平方矩陣中對每行進行K+1分區即可，使用np.argpartition函數達成

```Python
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis = 1)
nearest_partition
```

**執行結果**

```
array([[0, 3, 6, 1, 9, 5, 2, 7, 8, 4],
       [1, 9, 6, 0, 3, 5, 2, 7, 8, 4],
       [2, 4, 7, 8, 3, 5, 6, 0, 1, 9],
       [3, 0, 7, 4, 1, 5, 6, 2, 8, 9],
       [2, 4, 7, 8, 3, 5, 6, 0, 1, 9],
       [8, 5, 6, 9, 4, 1, 3, 7, 2, 0],
       [1, 9, 6, 0, 3, 5, 2, 7, 8, 4],
       [7, 2, 4, 8, 3, 0, 6, 5, 1, 9],
       [4, 8, 2, 7, 5, 3, 6, 9, 1, 0],
       [6, 9, 1, 5, 0, 3, 2, 7, 8, 4]], dtype=int64)
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

**執行結果**

![2.8.2](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\NumPy\images\2.8.2.PNG)



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

**執行結果**

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

**執行結果**

```
[('name', '<U10'), ('age', '<i4'), ('weight', '<f8')]
```

+ 結果: 

  +　U10: 表示Unicode編碼的字符串，最大長度為10

  +　i4: 表示4-byte(i.e., 32 bit)整數

  +　f8: 表示8-byte(i.e., 64 bit)浮點數

  



+ 將數據填進我們創建好的空結構化數組

```Python
## 將數據填進我們創建好的空結構化數組
data['name'] = name
data['age'] = age
data['weight'] = weight


print(data)
```

**執行結果**

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

**執行結果**

```
['Jack' 'Victor' 'Henna' 'Jen' 'Jessy']
[34 40 23 36 28]
[60.  90.8 50.6 46.2 52.4]
```



獲得第一筆數據(獲取第一行)

```Python
## 獲得第一筆數據(獲取第一行)
data[0]
```

**執行結果**

```
('Jack', 34, 60.)
```





獲取最後一筆數據的重量(獲取最後一行的重量)

```Python
## 獲取最後一筆數據的重量(獲取最後一行的重量)
data[-1]['weight']
```

**執行結果**

```
52.4
```



+ 布林遮蓋 Boolean Masking - 增加條件來過濾數據，像是體重的過濾

```Python
## 過濾體重，找到體重大於50的姓名
data[data['weight'] > 50]['name']
```

**執行結果**

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

**執行結果**

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

**執行結果**

```
dtype([('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])
```

+　第二種方式: 元組(tuple)的方式

```Python
## 元組
np.dtype([('name','S10'), ('age', 'i4'), ('weight', 'f8')])
```

**執行結果**

```
dtype([('name', 'S10'), ('age', '<i4'), ('weight', '<f8')])
```



+ 第三種方式: 如果類型的名稱不重要，可以直接省略掉，以一個用逗號分隔的字符串來設定數據類型

```Python
## 省略類型名稱，直接使用逗號隔開的字符串指定
np.dtype('S10, i4, f8')
```

**執行結果**

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

**執行結果**

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

**執行結果**

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

**執行結果**

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

**執行結果**

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

**執行結果**

```
144 ns ± 9.74 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
2.39 µs ± 162 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
3.21 µs ± 124 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```



結論: 依照個人應用的需求，決定要更簡潔的寫法還是更高效能的寫法