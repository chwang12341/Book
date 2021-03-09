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









## 2.4章 聚合: 最小值、最大值和其它 Aggregations: Min, Max, and Everythong In Between



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

