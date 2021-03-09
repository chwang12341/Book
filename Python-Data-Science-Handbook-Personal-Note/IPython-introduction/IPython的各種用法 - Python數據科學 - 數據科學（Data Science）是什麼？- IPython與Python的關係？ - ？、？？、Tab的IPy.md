# IPython的各種用法-讀書筆記- Python Data Science Handbook - Python數據科學 - 數據科學（Data Science）是什麼？- IPython與Python的關係？ - ？、？？、Tab的IPython幫助資訊快捷用法-筆記#1 





##  序言 重點整理 



### 1.什麼是數據科學？What is Data Science? 



作者拿很多人心中的疑問：什麼是數據科學（What is Data Science）當破題，他認為數據科學（Data Science）是一門跨領域的技術學科，並由三個領域相交而成： 



+ 統計學：對數據集進行統計分析與建模 
+ 電腦科學：對使用的演算法有效地儲存、處理和展示這些數據 
+ 領域知識：對相關專業領域進行整理，提出正確的問題與相對應的解決方法 由三種不同領域的專家組合而成，統稱為數據科學（Data Science）





### 2. 使用的套件 



+ IPython 和 Jupyter: 提供了Python的數據科學家，一個計算環境來完成工作 
+ Numpy: 提供了ndarray，幫助在Python中高效率地儲存和操作密集的數據數組 
+ Pandas: 提供了DataFrame，幫助在Python中高效率地存儲和處理帶標籤/列的數據資料 
+ Matplotlib: 提供數據可視化的套件 
+ Scikit-Learn: 提供最重要且建立好的機器學習演算法，於Python中高效與乾淨俐落的實現





## 第一章 重點整理 



### 1.0～1.1章 



#### 1. IPython 是什麼？ 



+ 2001年由Fernando Perez創建的一個增強Python解釋器（Interpreter）的項目 

+ Fernando Perez創建IPython的目標："Tools for the entire life cycle of research computing" - 研究計算領域完整生命週期的工具 

+ 作者認為如果將Python當成是我們的數據科學引擎的話，IPython可以認為是一個交互式的控制面板





#### 2. IPython 可以幫助我們快速查詢程式的相關資訊？ 



當我們遇到任何不了解的問題，第一件事就是上網查資料，當然程式工程師也不例外，於是IPython幫我們了一個大忙，只要透過一些符號（？、？？）或函式（help()）就能幫助我們瞭解以下資訊： 



+ 如何使用這個函式（function），有什麼樣的參數和選項？ 

+ 這個Python對象（object）的原始碼是如何寫的？ 

+ 導入的套件（Packages）裡面有哪些內容，有哪些屬性或方法可以使用？







#### 3. IPython啟動幫助文檔的方法



+ help(): 獲取文檔資訊，屬於Python的內建方法 

+ ？：探索文檔，屬於IPython的方法，用來簡化help()的操作 

+ ？？：查看原始碼，屬於IPython的方法 

+ Tab: 按下Tab鍵來進行自動補全，像是我們創建了一個串列（list）為L，那我們想知道串列（list）可以有哪些屬性操作，就打上L.，接著後面按下Tab鍵，就會出現所有可以使用的方法了







#### 4. help的方法舉例 



```Python
help(len) 
```



**執行結果**  

```
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```







#### 5. ？方法舉例 



+ IPython用來簡化help()的方法 

+ 適用對象：任何對象，包括對象的屬性方法與對象本身 

+ **重要觀念**：可以自己創建函數，並自行定義函數資訊，再透過？來查看函數資訊，所以作者希望大家養成寫文檔(docstring)的好習慣 



範例一：對list進行查找資訊



```Python
list?
```

**執行結果**

```
Init signature: list(iterable=(), /)
Docstring:     
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
Type:           type
Subclasses:     _HashedSeq, StackSummary, SList, _ImmutableLineList, FormattedText, NodeList, _ExplodedList, Stack, _Accumulator, _ymd, ...
```





 範例二：自定義一個串列（list），並對對象本身進行查詢資訊 



```Python
new_list = [1,2,3,4,5,6]
new_list?
```



**執行結果**

```
Type:        list
String form: [1, 2, 3, 4, 5, 6]
Length:      6
Docstring:  
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
```





範例三：查詢對象方法的資訊 



```Python
new_list =[1,2,3,4,5,6] 

new_list.insert?
```

**執行結果** 

```
Signature: new_list.insert(index, object, /)
Docstring: Insert object before index.
Type:      builtin_function_or_method
```







範例四：自行定義一個函數，並寫下docstring來供查詢函數資訊 



+ 使用方法：兩邊加上三個"，來將docstring圍住即可 執行結果

```Python
def multiply(a,b):
    """a multiply b"""
    
    return a * b

multiply?
```

**執行結果**

```
Signature: multiply(a, b)
Docstring: a multiply b
File:      c:\users\user\desktop\book\python-data-science-handbook-personal-note\ipython-introduction\<ipython-input-10-dca4930b912a>
Type:      function
```







#### 6. ？？方法舉例 



．使用??來獲取原始碼 

．提醒：因為有些函數方法不是用Python寫的，而是用C寫的，所以獲取不了原始碼，此時??就會變得跟?一樣，像是len、list 



範例一：獲取原始碼 

```Python
def multiply(a,b):
    """a multiply b"""
    
    return a * b

multiply??
```

**執行結果** 

```
Signature: multiply(a, b)
Source:   
def multiply(a,b):
    """a multiply b"""
    
    return a * b
File:      c:\users\user\desktop\book\python-data-science-handbook-personal-note\ipython-introduction\<ipython-input-11-410a07b52bea>
Type:      function
```



範例二：由於不是Python寫的函數功能方法，所以獲取不了原始碼 



```Python
len??
```

**執行結果**

```
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method
```







#### 7. Tab鍵的使用 - 自動補全功能



+ 說明：按下Tab鍵來進行自動補全，像是我們創建了一個串列（list）為L，那我們想知道串列（list）可以有哪些屬性操作，就輸入L.，接著按下Tab鍵，就會自動列出所有可以使用的屬性方法了
+ 小提醒：雖然Python沒有明確的私有與公有屬性的差別，但是慣例上私有屬性都會加上"\__"，而預設的情況下Tab不會出現私有屬性的選項，如果要使用，就要在按下Tab前面多加一個或兩個"\_"，像是L.__<Tab>
+ 更多用法1：導入套件也可以使用Tab來查詢喔
+ 更多用法2：查詢通配字符也可以使用喔，像是我想查詢某個名稱，但是我只記得名稱後面是Warning，就可以使用*Warning?來查詢喔





範例一：查詢我創建的新串列（list）中有哪些方法可以操作



+ 小提醒：後面的<Tab>不是要大家直接打在程式裡喔，是要按Tab鍵



```Python
new_list = [1,2,3,4,5,6]
new_list.<Tab>
```

**執行結果**



![image1](images\image1.PNG)







**這樣IPython就會自動出現我們可以操作的方法選項喔**





**補充範例：Python內建的方法dir** 



```Python
new_list = [1,2,3,4,5,6]
dir(new_list)  
```

**執行結果**

```
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
```







範例二：關鍵字縮小選項的範圍，假設我們想找i開頭的屬性功能方法 



```Python
new_list = [1,2,3,4,5,6] 

new_list.i<Tab> 
```

執行結果 

![image2](images\image2.png)





這樣IPython就會自動找尋以i為開頭的方法喔 





範例三：如果方法選項只剩一個的時候，就會自動補全喔，就不會再列出選項 



```Python
new_list = [1,2,3,4,5,6] 

new_list.ins<Tab>
```

**執行結果**

會自動補成insert

```Python
new_list = [1,2,3,4,5,6] 

new_list.insert
```







範例四：查詢私有屬性 



```Python
new_list = [1,2,3,4,5,6]
new_list._<Tab> 
```

**執行結果**  



![image3](images\image3.png)









範例五：從math套件中找尋以a為開頭的內容 



```Python
from math import a<Tab>  
```

**執行結果**



![image4](images\image4.png)





範例六：查詢所有我們自己的第三方套件 

+ 會根據我們下載的第三方套件顯示，所以每個人可能不太一樣 

  

```Python
import <Tab>
```

**執行結果**

![image5](images\image5.png)



+ 查詢以a為開頭的套件名稱 

```Python
import a<Tab>  
```

**執行結果**

![image6](images\image6.png)





範例七：透過通配符，找尋關鍵字的所有名稱



+ 我想找尋所有以Error結尾的名稱

+ *: 用於匹配任何的字符 

```Python
*Error?
```

**執行結果**

  

```
ArithmeticError
AssertionError
AttributeError
BlockingIOError
BrokenPipeError
BufferError
ChildProcessError
ConnectionAbortedError
ConnectionError
ConnectionRefusedError
ConnectionResetError
EOFError
EnvironmentError
FileExistsError
FileNotFoundError
FloatingPointError
IOError
ImportError
IndentationError
IndexError
InterruptedError
IsADirectoryError
KeyError
LookupError
MemoryError
ModuleNotFoundError
NameError
NotADirectoryError
NotImplementedError
OSError
OverflowError
PermissionError
ProcessLookupError
RecursionError
ReferenceError
RuntimeError
SyntaxError
SystemError
TabError
TimeoutError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
ValueError
WindowsError
ZeroDivisionError
```





+ 我想查詢所有str操作裡，有sub在裡面的名稱 str.*sub*?

```Python
str.*sub*?
```

**執行結果**

```
str.__init_subclass__
str.__subclasscheck__
str.__subclasses__
str.__subclasshook__
```





# IPython各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - IPython的快捷鍵與神奇的魔術指令 - 原來In[] 和 Out[] 可以這樣用 - IPython中執行Shell指令 - Errors and Debugging 重要的除錯功能 - 筆記#2 







## 1.2章IPython快捷鍵 







### 1. 如何打開IPython shell? 



打開Anaconda Prompt，並輸入ipython，按下Enter鍵





### 2. IPython shell中的快捷鍵 



#### 領航快捷鍵（Navigation shortcuts） 



| 按鍵                         | 動作                 |
| ---------------------------- | -------------------- |
| Ctrl-a                       | 移動光標到開頭的位置 |
| Ctrl-e                       | 移動光標到結束的位置 |
| Ctrl-b or the left arrow key | 光標向左移動一個字符 |
| Ctrl-r                       | 光標向右移動一個字符 |







#### 文字輸入快捷鍵（Text Entry Shortcuts） 



| 按鍵          | 動作                                 |
| ------------- | ------------------------------------ |
| Backspace key | 刪除光標前一個字符                   |
| Ctrl-d        | 刪除光標所在的字符                   |
| Ctrl-k        | 剪掉光標所在位置到最後一個位置的字符 |
| Ctrl-u        | 剪掉光標所在位置到第一個位置的字符   |
| Ctrl-y        | 貼上剪掉的字符                       |
| Ctrl-t        | 交換光標前一個與當下所在的字符位置   |





#### 指定歷史的快捷鍵（Command History Shortcuts） 



| 按鍵                           | 動作             |
| ------------------------------ | ---------------- |
| Ctrl-p (or the up arrow key)   | 獲取前一條命令   |
| Ctrl-n (or the down arrow key) | 獲取後一條指令   |
| Ctrl-r                         | 反向搜尋命令歷史 |



#### 雜項快捷鍵（Miscellaneous Shortcuts）



| 按鍵   | 動作                     |
| ------ | ------------------------ |
| Ctrl-l | 清除終端窗口             |
| Ctrl-c | 終止目前執行的Python命令 |
| Ctrl-d | 關掉IPython              |







## 1.3章 IPython的魔術指令（IPython Magic Commands）



### 1. %paste & %cpaste - 張貼程式碼 



大家應該都有遇到過這個問題，就是複製了網路上的程式碼，直接貼上到我們的編譯器上時，竟然報錯了，這可能是因為編譯器被額外的提示符搞亂了，就可以使用%paste和%cpaste來解決  



情況舉例：



原本想複製網路上的程式碼 



```Python
>>> def add(a,b):
... 	return a+b 
```



然後直接複製貼上到IPython會報錯 



這時候就可以使用%paste，它專門處理編譯器被一些額外的提示符搞亂了的情況 



**自己嘗試的結果:但我自己嘗試了書本上的範例發現要很特定的情況下用%paste，才不會報錯，要不然就是原本就不會有錯，感覺基本上它還是張貼的作用**



#### 使用說明 



+ %paste: 一打上去，就會將我們當前複製的程式碼貼上
+ %cpaste: 在IPython中輸入後，會出現一個交互式的多行提示符，使我們可以貼上多個程式碼塊，然後批量執行它們



示範一:



```Python
In [1]: %paste
>>> def add(a,b):
...     return a+b

## -- End pasted text --

In [2]: add(2,6)
Out[2]: 8

In [3]: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:>>> def add(a,b):
:... return a+b
:>>> def add(a,b):
:... return 2a+2b
:>>> def add(a,b):
:... return 3a+3b
:--
```



示範二: 在%cpaste中使用%paste

```Python
In [1]: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:%paste
:--
>>> def add(a,b):
...     return a+b

## -- End pasted text --
```







### 2. %run - 在IPython中，執行外部的Python檔 



+ 格式：%run (執行的Python檔名稱) 



+ 舉例：我們有一個Python檔  

```Python
## python_script.py

def multiply(a,b):
    '''a multiply of b'''
    
    return a*b


if __name__ == '__main__':
    
    for i in range(10):
        print(str(i) + ' multiply of ' + str(i+1) + ' : ' , multiply(i,i+1))
   
```





+ 在IPython中執行這個Python檔，如果沒有給目錄位置，就要到Python檔的目錄位置底下執行喔 



```Python
%run python_script_demo.py 
```





**執行結果**

```Python
In [1]: %run python_script.py
0 multiply of 1 :  0
1 multiply of 2 :  2
2 multiply of 3 :  6
3 multiply of 4 :  12
4 multiply of 5 :  20
5 multiply of 6 :  30
6 multiply of 7 :  42
7 multiply of 8 :  56
8 multiply of 9 :  72
9 multiply of 10 :  90
```



執行完後，還能在IPython使用這些在Python檔中定義好的函數 



```Python
In [2]: multiply(2,8)
Out[2]: 16
```



### 3. %timeit - 程式碼執行時間計時，瞭解哪個用法更快 



．格式：%timeit (要執行計時的程式碼) 



範例一： 



```Python
In [3]: %timeit new_list = [x**2 for x in range(1000)]
282 µs ± 10.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```



範例二：換個方式寫程式碼，但目的一樣  



```Python
In [4]: %%timeit
   ...: new_list = []
   ...: for x in range(1000):
   ...:     new_list.append(x**2)
   ...:
317 µs ± 15 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```





可以看出雖然目的是一樣的，但兩個不同的程式碼寫法，執行時間是不同的喔 





**補充：如果想在IPython中使用多行就要兩個%，像是%%timeit**





### 4. 如何查詢魔術指令的資訊與列出所有的魔術指令 - ?、%magic、%lsmagic 



+ ?: 如果想查詢某個魔術指令的資訊，像是%run? 

+ %magic: 獲得魔術指令的通用敘述與舉例 

+ %lsmagic: 列出所有可用的魔術指令



我這邊列出一些魔術指令喔



![magic_function1](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\IPython-introduction\images\magic_function1.png)



![magic_function2](C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\IPython-introduction\images\magic_function2.png)





## 1.4章 Input 和 Output 的歷史 - 使用In 和 Out 來獲取歷史記錄 





### 1. In 和 Out 的用法 



大家一定都有看到IPython中的提示符 - In[] 和 Out[]，但大部分的人以為只是為了美觀所採用的修飾符，但其實它有很厲害的功用的，它能夠讓我們簡單獲得以前的輸入和輸出內容 





範例：我們先照著以下的程式執行 - 我們導入math套件，並計算開根號、sin、cos和tan



```
In [1]: import math

In [2]: math.sqrt(2)
Out[2]: 1.4142135623730951

In [3]: math.sin(6)
Out[3]: -0.27941549819892586

In [4]: math.cos(6)
Out[4]: 0.960170286650366

In [5]: math.tan(6)
Out[5]: -0.29100619138474915
```



接下來，利用In和Out列印出我們執行過的輸入與輸出內容



```
In [6]: In
Out[6]:
['',
 'import math',
 'math.sqrt(2)',
 'math.sin(6)',
 'math.cos(6)',
 'math.tan(6)',
 'In']

In [7]: Out
Out[7]:
{2: 1.4142135623730951,
 3: -0.27941549819892586,
 4: 0.960170286650366,
 5: -0.29100619138474915,
 6: ['',
  'import math',
  'math.sqrt(2)',
  'math.sin(6)',
  'math.cos(6)',
  'math.tan(6)',
  'In',
  'Out']}
```





+ In: 返回輸入過的內容，會以串列（list）的形式傳回 

+ Out: 返回輸出過的內容，會以字典的形式回傳 



指定我們要看第幾個輸出或輸入

```
In [8]: print(In[1])
import math

In [9]: print(Out[4])
0.960170286650366
```



**提醒：**並不是所有輸入都會有輸出，像是import和print的語句就不會影響輸出（Output）內容，簡單來說就是import和print的結果，會返回None，而任何指令返回None都不會加入到Out中，所以print(Out)會看不到他們的結果 



這個方法，對於拿過去的計算結果做運算，是非常方便的

```
In [1]: import math

In [2]: math.sin(6)
Out[2]: -0.27941549819892586

In [3]: math.cos(6)
Out[3]: 0.960170286650366

In [4]: Out[2]**2 + Out[3]**2
Out[4]: 0.9999999999999999
```





### 2. `_`下滑線用法 - 回到過去的輸出（Output） 



想回到上一個輸出結果，就輸入一個"*"下滑線，前兩個輸出結果就兩個下滑線"*"，前三個輸出結果就三個下滑線`_`，但注意沒有以此類推囉XD，IPython最多只支援三個下滑線，而且它會自動跳過沒有輸出結果的命令喔  

```
In [5]: print(_)
0.9999999999999999

In [6]: print(__)
0.960170286650366

In [7]: print(___)
-0.27941549819892586
```







也可以使用 格式：_ (第幾個輸出結果)來直接印出之前的輸出結果，像是我們會寫Out[4]來引出第四個輸出結果，而這邊有個更簡潔的寫法_4



```
In [8]: Out[4]
Out[8]: 0.9999999999999999

In [9]: _4
Out[9]: 0.9999999999999999
```



### 3. ";" - 不要將執行結果，加入道輸出結果的歷史中

+ 只要在指令後面加上";"，就不會將這次的執行結果加入到Out裡



```
In [16]: math.sin(6)**2 + math.cos(6)**2;

In [17]: Out[16]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-17-7ca36f6eddac> in <module>
----> 1 Out[16]

KeyError: 16

In [18]: 16 in Out
Out[18]: False
```



### 4. %history 批量查看歷史記錄（Input） 



可以查看過去第幾個的輸入（Input） 



+ 範例：我想查看過去第一到第四個輸入（Input）與第一到第五個輸入（Input）



```
In [1]: import math

In [2]: math.sin(6)
Out[2]: -0.27941549819892586

In [3]: math.cos(6)
Out[3]: 0.960170286650366

In [4]: math.tan(6)
Out[4]: -0.29100619138474915

In [5]: print(Out)
{2: -0.27941549819892586, 3: 0.960170286650366, 4: -0.29100619138474915}

In [6]: %history -n 1-4
   1: import math
   2: math.sin(6)
   3: math.cos(6)
   4: math.tan(6)

In [7]: %history -n 1-5
   1: import math
   2: math.sin(6)
   3: math.cos(6)
   4: math.tan(6)
   5: print(Out)
```



## 1.5章 IPython 和 Shell 指令 - 如何在IPython中下達Shell指令 - ls、cd、mkdir等等



+ 在Python環境中，當我們想要一邊下達對操作系統的Shell指令，一邊撰寫Python，我們只能再開一個終端窗口，或是退出Python環境，然後下達完指令，再切回Python，但是IPython可以讓我們同時在它的環境下，做到這兩種事 



### 1. "!" - 輕鬆幫我們在IPython Shell中，執行Shell指令



 ```
In [2]: ls
 磁碟區 C 中的磁碟是 Windows
 磁碟區序號:  1C71-9B46

 C:\Users\user\Desktop\Book\Python-Data-Science-Handbook-Personal-Note\IPython-introduction\images 的目錄

2021/02/10  下午 12:10    <DIR>          .
2021/02/10  下午 12:10    <DIR>          ..
2020/11/28  下午 12:26            21,909 Command History Shortcuts.png
2020/11/24  下午 08:27             6,225 image1.PNG
2020/11/24  下午 08:30            55,914 image2.png
2020/11/24  下午 08:35           110,153 image3.png
2020/11/24  下午 08:37           138,940 image4.png
2020/11/24  下午 08:40           159,651 image5.png
2020/11/24  下午 08:41           239,450 image6.png
2021/02/10  下午 12:09           104,667 magic_function1.png
2021/02/10  下午 12:10           105,858 magic_function2.png
2020/11/28  下午 12:29            15,005 Miscellaneous Shortcuts.png
2020/11/28  下午 12:19            27,758 Navigation shortcuts.png
2020/11/28  下午 12:23            35,943 Text Entry Shortcuts.png
              12 個檔案       1,021,473 位元組
               2 個目錄  35,393,601,536 位元組可用

In [3]: pwd
Out[3]: 'C:\\Users\\user\\Desktop\\Book\\Python-Data-Science-Handbook-Personal-Note\\IPython-introduction\\images'

In [4]: !echo "Shell command - Printing"
"Shell command - Printing""
 ```





我自己試了在Windoes系統中，如果不加!會有作用嗎，發現也會有喔！！但是加了!，看起來更簡潔清楚



### 2. 從Shell中傳回值，並保存成一個看似Python的列表，但多了一些功能的列表 



```
In [8]: file_list = !ls

In [9]: print(file_list)
["'ls' ���O�����Υ~���R�O�B�i���檺�{���Χ妸�ɡC"]

In [10]: directory_list = !pwd

In [11]: type(directory_list)
Out[11]: IPython.utils.text.SList
```







從印出的類型來看，它看起來像是Python的列表（list），但是多了一些額外的功能，像是grep和fields方法，以及s、n和p屬性，使我們能夠用簡單的方式進行搜索、過濾和顯示結果 file_list?



### 3. 從Python中傳值給Shell使用 





+ Python也可以傳變數名稱給Shell使用，只要透過{變數名稱}即可 

```
In [12]: context = "Values from Python"

In [13]: !echo {context}
Values from Python

In [14]: echo {context}
Values from Python
```





### 4. !cd 沒辦法在IPython中移動目錄位置 



+ 原因：因為notebook中的Shell是在一個暫時的子Shell空間中運行的 
+ 解決辦法：將!cd指令改成%cd或cd 
+ 補充：除了%cd，其它相似的Shell指令，像是%cat、%cp、%env、%ls、%rmdir、%mkdir、%more、%rm、%pwd、%man和%mv，這些魔術命令在automagic啟動（打上%automagic來啟動或關閉）時都可以不用有%就能使用，也就是把IPython shell當成我們系統的shell使用





## 1.6章 Errors and Debugging - 非常重要的錯誤與除錯功能 





### 1. %xmode - Controlling Exception - 異常控制 - Plain、Context和Verbose 



+ %xmode - Exception mode的縮寫，用來控制異常發生時，錯誤訊息的數量 

+ 模式：Plain、Context、Verbose，預設為Context 

+ 使用方法：%xmode (一種模式名稱)  

  

  

一般情況下，當程式出現錯誤時，系統會報的錯誤資訊

```Python
def divided(a, b):
    c = b - 1
    return a/c

divided(8,1)
```

**執行結果**

```
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-c36e5fec3a86> in <module>
      3     return a/c
      4 
----> 5 divided(8,1)

<ipython-input-3-c36e5fec3a86> in divided(a, b)
      1 def divided(a, b):
      2     c = b - 1
----> 3     return a/c
      4 
      5 divided(8,1)

ZeroDivisionError: division by zero
```





當編譯器遇到了異常狀況的時候，會將錯誤產生的原因壓縮到眼前程式執行的追溯（Traceback）中，而IPython使我們可以控制異常發生時錯誤訊息的數量 





### 2. Context模式: 預設模式



```Python
%xmode Context 

def divided(a, b):
    c = b - 1
    return a/c

divided(8,1)
```

**執行結果**

```
Exception reporting mode: Context
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-4-b54a250447e3> in <module>
      5     return a/c
      6 
----> 7 divided(8,1)

<ipython-input-4-b54a250447e3> in divided(a, b)
      3 def divided(a, b):
      4     c = b - 1
----> 5     return a/c
      6 
      7 divided(8,1)

ZeroDivisionError: division by zero
```



### 3. Plain模式：更簡短的，較少的錯誤資訊內容

```Python
%xmode Plain

def divided(a, b):
    c = b - 1
    return a/c

divided(8,1)
```

**執行結果**



```
Exception reporting mode: Plain
Traceback (most recent call last):

  File "<ipython-input-8-01362f71b695>", line 7, in <module>
    divided(8,1)

  File "<ipython-input-8-01362f71b695>", line 5, in divided
    return a/c

ZeroDivisionError: division by zero
```







### 4. Verbose模式：更多訊息，包括函數調用時的參數值

```Python
%xmode Verbose

def divided(a, b):
    c = b - 1
    return a/c

divided(8,1)
```

**執行結果**

```
Exception reporting mode: Verbose
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-10-6808dfac2ac2> in <module>
      5     return a/c
      6 
----> 7 divided(8,1)
        global divided = <function divided at 0x000002405C314048>

<ipython-input-10-6808dfac2ac2> in divided(a=8, b=1)
      3 def divided(a, b):
      4     c = b - 1
----> 5     return a/c
        a = 8
        c = 0
      6 
      7 divided(8,1)

ZeroDivisionError: division by zero
```





#### Verbose可以擁有那麼多的錯誤資訊，為什麼不都用它就好？ 

當我們的程式越來越多的時候，太多的訊息很難閱讀，所以要視情況，有時候簡短才能幫助我們快速進行除錯（Debugging）喔 



### 5. %debug 進階用法 - 當Traceback已經不能滿足問題 



+ Python - 標準Python下有一個交互式的除錯工具 - pdb
+ IPython - 有一個增強版的除錯工具 - ipdb





#### ipdbb是什麼？ 

ipdbb讓我們可以查看當前的Traceback訊息，還可以顯示變數與它們的值，甚至還能直接執行Python命令 







當執行%debug，就會啟動ipdbb交互式界面，讓我們查詢變數值等等功能 

```Python
%debug 
```







範例：像是我們現在有一個程式執行的時候會報錯

```Python
def divided(a, b):
    c = b - 1
    return a/c

divided(8,1)
```





這時候就執行%debug，來開啟ipdbb 

```Python
%debug
```





使用print來得知變數值  

```Python
> <ipython-input-11-c36e5fec3a86>(3)divided()
      1 def divided(a, b):
      2     c = b - 1
----> 3     return a/c
      4 
      5 divided(8,1)

ipdb> print(a)
8
ipdb> print(b)
1
ipdb> print(c)
0
ipdb> print(a/c)
*** ZeroDivisionError: division by zero
ipdb> quit
```









使用up、down來回溯上一層或下一層，當很多個Function互相調用（call）對方時，幫助我們從眾多Function中找尋哪個Function出問題

```Python
> <ipython-input-11-c36e5fec3a86>(3)divided()
      1 def divided(a, b):
      2     c = b - 1
----> 3     return a/c
      4 
      5 divided(8,1)

ipdb> up
> <ipython-input-11-c36e5fec3a86>(5)<module>()
      1 def divided(a, b):
      2     c = b - 1
      3     return a/c
      4 
----> 5 divided(8,1)

ipdb> down
> <ipython-input-11-c36e5fec3a86>(3)divided()
      1 def divided(a, b):
      2     c = b - 1
----> 3     return a/c
      4 
      5 divided(8,1)
```



#### 如何將除錯工具ipdbb保持啟動的狀態，程式執行報錯就會馬上開啟 



+ 使用%pdb，後面加上on/off 來開啟或關閉除錯工具的自動開啟模式 

+ 使用方法：%pdb (on/off)



```Python
%xmode Verbose
%pdb on


def divided(a, b):
    c = b - 1
    return a/c

divided(8,1)
```



**執行結果**

```
Exception reporting mode: Verbose
Automatic pdb calling has been turned ON
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-16-2425b790b5b2> in <module>
      7     return a/c
      8 
----> 9 divided(8,1)
        global divided = <function divided at 0x000002405C3F70D8>

<ipython-input-16-2425b790b5b2> in divided(a=8, b=1)
      5 def divided(a, b):
      6     c = b - 1
----> 7     return a/c
        a = 8
        c = 0
      8 
      9 divided(8,1)

ZeroDivisionError: division by zero
ipdb> 
> <ipython-input-16-2425b790b5b2>(7)divided()
      5 def divided(a, b):
      6     c = b - 1
----> 7     return a/c
      8 
      9 divided(8,1)
```



#### 外部的Python檔，如何在IPython中交互式的執行，並且同時打開除錯工具 - ipdbb 



+ 使用%run -d來執行Python檔，然後使用next在交互模式下進行一步一步執行Python檔中的程式



```Python
In [1]: %run python_script.py
0 multiply of 1 :  0
1 multiply of 2 :  2
2 multiply of 3 :  6
3 multiply of 4 :  12
4 multiply of 5 :  20
5 multiply of 6 :  30
6 multiply of 7 :  42
7 multiply of 8 :  56
8 multiply of 9 :  72
9 multiply of 10 :  90

In [2]: %run -d  python_script.py
*** Blank or comment
*** Blank or comment
*** Blank or comment
NOTE: Enter 'c' at the ipdb>  prompt to continue execution.
> c:\users\user\desktop\book\python-data-science-handbook-personal-note\ipython-introduction\python_script.py(3)<module>()
      1 ## python_script.py
      2
----> 3 def multiply(a,b):
      4     '''a multiply of b'''
      5

ipdb>  
```





#### 開啟除錯模式ipdbb，可以下達的命令



| 命令       | 說明                                             |
| ---------- | ------------------------------------------------ |
| list       | 顯示目前在檔案中的位置                           |
| h(elp)     | 幫助文檔，可以顯示列表，或檢視某個指令的幫助資訊 |
| q(uit)     | 退出除錯器與當前程序                             |
| c(ontinue) | 退出除錯模式，繼續執行程式                       |
| n(ext)     | 執行下一行程式碼，一步一步執行                   |
| <enter>    | 重複上一個命令                                   |
| p(rint)    | 印出變數 s(tep): 踏進子函數內部中進行除錯        |
| r(eturn)   | 執行到函數返回                                   |





ipdbb 的官方文檔：https//[github.com/gotcha/ipdb](http://github.com/gotcha/ipdb?fbclid=IwAR2kRnEfpYNLc3C0eNp-3_kAo4Z9jOgxsXB9b_wocIPeOp4REMKS_1_eXZk)







# IPython各種用法 - 讀書筆記 - Python Data Science Handbook - Python數據科學 - 寫程式非常重要的性能測算與計時 - IPython的相關網路資源與書籍 - 筆記#3 



## 1.7章 程式性能的測算與計時 



### 1.IPython中的各種計算性能方法 



+ %time: 測量單個語句的執行時間 
+ %timeit: 重複測量單個語句的執行時間，並計算平均時間，來取得更準確的執行時間結果 
+ %prun: 使用性能計算工具與程式碼一起執行 
+ %lprun: 使用單個語句執行的性能計算工具與程式碼一起運行 
+ %memit: 計算單個語句佔用的內存（Memory）空間 
+ %mprun: 使用單個語句執行的內存（Memory）計算工具與程式碼一起執行



### 2. %time & %timeit 程式執行計時工具



| 魔術指令 | 優點                                                         | 缺點                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| %time    | 1.適合對於執行時間較長的程式 2.不進行重複執行，所以特定狀況下，像是對列表（list）進行排序時，就非常適合使用 | 較不準確，因為只執行一次                                     |
| %timeit  | 1.適合對於執行時間較短的程式2.時間準確（因為重複執行很多次後取平均值） | 有些情況下，重複執行造成時間計算錯誤，像是對列表（list）進行排序 |



#### %timeit 

```Python
%timeit sum(range(600))
```

**執行結果**

```
7.35 µs ± 38.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```



 補充說明：由於上面的例子執行速度相當快，所以%timeit會自動重複運行很多回合，但如果換成一個執行較慢的計算，%timeit會自動減少回合數，如下例子  

```Python
%%timeit

total = 0
for i in range(6000):
    for k in range(6000):
        total += i * k
print(total)
```

**執行結果**

```
323892009000000
323892009000000
323892009000000
323892009000000
323892009000000
323892009000000
323892009000000
323892009000000
2.73 s ± 212 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```



狀況：如果遇到列表進行排序操作時，重複執行的結果會誤導我們，因為對一個已經排好序的列表進行排序是非常快的，所以在第一次執行完成後，後面重複進行測量的數據都是錯誤的，時間會不對（會過快）

```Python
import random
L = [random.random() for i in range(1000000)]
%timeit L.sort()
```

**執行結果**

```
21.9 ms ± 278 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
```





#### %time



 範例一：計算還沒排序的列表 

```Python
import random
L = [random.random() for i in range(1000000)]
print('Sorting an Unsorting list(L)')
%time L.sort()
```

**執行結果**

```
Sorting an Unsorting list(L)
Wall time: 230 ms
```



範例二：接著上面執行計算已經排好序的列表 

```Python
print('Sorting an Alreaddy Sorted list(L)')
%time L.sort()
```

**執行結果**

```
Sorting an Alreaddy Sorted list(L)
Wall time: 22.7 ms
```



可以明顯看出時間差異！！所以非常不適合重複執行！！ 





#### 計時 - %timeit為什麼通常都比%time的執行時間快？

 

%timeit會有一種額外的機制，來防止系統調用（System calls）影響程式執行的時間結果，像是它會防止系統清理掉不再使用的Python物件（又稱垃圾收集），才不會讓這樣的狀況影響執行的時間





#### % 只能執行一行程式碼，%%就可以執行一整段程式碼  

```Python
%%time
total = 0
for i in range(6000):
    for k in range(6000):
        total += i * k
        
print(total)
```

**執行結果**

```
323892009000000
Wall time: 5.01 s
```





### 3. %prun整個Python檔的性能測算



舉例：先自行定義一個函數，然後測算它的性能 

```IPython
In [1]: def sum_list(N):
   ...:     total = 0
   ...:     for i in range(5):
   ...:         L = [j ^ (j >> i) for j in range(N)]
   ...:     return total
```







計算性能%prun

```IPython
In [2]: %prun sum_list(10000000)
         9 function calls in 6.178 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        5    5.708    1.142    5.708    1.142 <ipython-input-1-9b46611eb043>:4(<listcomp>)
        1    0.355    0.355    6.063    6.063 <ipython-input-1-9b46611eb043>:1(sum_list)
        1    0.115    0.115    6.178    6.178 <string>:1(<module>)
        1    0.000    0.000    6.178    6.178 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```





產出的結果表格，顯示每個函數調用的執行時間排序（從大到小），當然從我們的範例中，因為只有執行一個函數，所以耗時最長的就是sum_list 



使用%prun就能看出程式在哪耗時最久，也就能知道要從哪裡著手了





### 4. %lprun 一行一行的執行程式碼去測試性能 



安裝第三方套件到Python中 

```
pip install line_profiler 
```



再從IPython中載入套件 

```
%load_ext line_profiler 
```





執行%lprun來計算函數的逐條程式性能 

```Python
%lprun -f sum_list(5000) 
```







書本說從結果可以看出，%lprun會幫我們一行一行計算程式性能，單位是毫秒，讓我們知道哪一行執行時間最久，就能根據這個資訊優化哪行程式 



這邊我在安裝第三方套件的時候一直報錯，所以沒辦法親自試試，大家可以自行使用看看



### 5. %memit & %mprun 計算內存（Memory）使用量 



安裝第三方套件到Python中 

```
pip install memory_profiler
```



再從IPython載入套件 

```
%load_ext memory_profiler 
```





#### %memit 整個程式的內存空間（Memory Space）使用量 



執行%memit來計算函數的逐條程式性能 

```IPython
In [1]: %load_ext memory_profiler

In [2]: def sum_list(N):
   ...:    ...:     total = 0
   ...:    ...:     for i in range(5):
   ...:    ...:         L = [j ^ (j >> i) for j in range(N)]
   ...:    ...:     return total
   ...:

In [3]: %memit sum_list(6000)
peak memory: 50.06 MiB, increment: 0.51 MiB
```

結果：從peak memory可以看出這個程式用了多少的內存（Memory）空間





#### %mprun - 逐行程式檢視內存（Memory）空間的使用量 



+ 限制：它只能在獨立的模塊（Modules）上使用，不能應用在notebook本身，簡單來說，它要執行整個外部的Python檔 



+ **使用%%file，來創建一個Python檔，如果遇到Permission denied，表示權限不夠喔，可以建議改用Anaconda Powershell Prompt 或是自行用別的編譯器來創建Python檔**  

```IPython
In [3]: %memit sum_list(6000)
peak memory: 50.06 MiB, increment: 0.51 MiB

In [4]: %%file mprun_demo_example.py
   ...: def sum_lists(N):
   ...:     total = 0
   ...:     for i in range(6):
   ...:         L = [j ^ (j >> i) for j in range(N)]
   ...:         total += sum(L)
   ...:         del L
   ...:     return toal
   ...:
Writing mprun_demo_example.py
```





+ 導入模塊，也就是導入外部Python檔（前面所建立的），並使用內存空間（Memory Space）計算工具 - %mprun，來進行逐行程式碼計算 

```IPython
In [5]: from mprun_demo_example import sum_lists

In [6]: %mprun -f sum_lists sum_lists(10000000)
```



**執行結果**

```
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     1     51.3 MiB     51.3 MiB           1   def sum_lists(N):
     2     51.3 MiB      0.0 MiB           1       total = 0
     3     51.3 MiB      0.0 MiB           2       for i in range(6):
     4    359.6 MiB -75619584.5 MiB    17985287           L = [j ^ (j >> i) for j in range(N)]
     5    127.6 MiB      0.0 MiB           1           total += sum(L)
     6     51.3 MiB    -76.3 MiB           1           del L
     7                                             return toal
*** KeyboardInterrupt exception caught in code being profiled.
```



+ Increment 表示內存空間（Memory Space）是如何變化的，創建L串列，與最後刪除L串列，大家可以看出內存的佔用與釋放變化





## 1.8章 IPython網路資源與相關數據推薦 





### 1. 網路資源 



| 網站                                       | 說明                                                         | 連結                                                         |
| ------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| The IPython website                        | 文檔、例子、教學和很多樣的其他資源                           | [https://ipython.org/](https://l.facebook.com/l.php?u=https%3A%2F%2Fipython.org%2F%3Ffbclid%3DIwAR1RivHSM8fnLtY6fpeet8nvMJ6bh4bL3bT0fyzAJ0C4lgihd12PAVZ9glo&h=AT3c3VoHrLCpkv9N8Mn85Y2oqNWdHWhxwA2y7SWufd3-MbO1OKIafCfCh5b7naY-60ijqQYS8umIB0x2P5grCxlSLX0T7iqulZr3Tno-4FQeaPRXCPecDFcfhbJ-Y07xUV4Xew) |
| The nbviewer website                       | 網站上展示了網路上的IPython notebook的資源文件，並在首頁上展示了一些notebooks的例子，這樣我們可以看到其他人是如何使用IPython的 | [https://nbviewer.jupyter.org/](https://l.facebook.com/l.php?u=https%3A%2F%2Fnbviewer.jupyter.org%2F%3Ffbclid%3DIwAR3s1nZgctgaPmGL9sgiFBcqBrt99btgLS_Qqwr1lyStVvUW2m01qq_bEYs&h=AT3c3VoHrLCpkv9N8Mn85Y2oqNWdHWhxwA2y7SWufd3-MbO1OKIafCfCh5b7naY-60ijqQYS8umIB0x2P5grCxlSLX0T7iqulZr3Tno-4FQeaPRXCPecDFcfhbJ-Y07xUV4Xew) |
| A gallery of interesting Jupyter Notebooks | 它是一個不斷增加的notebooks列，由nbviewer進行維護，展示了許多具有深度又有廣度的IPython在數值分析上的應用，它應有盡有，從簡短的例子到教程，再到完整的課程與書籍，並且它都是使用notebook格式 | [https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fjupyter%2Fjupyter%2Fwiki%2FA-gallery-of-interesting-Jupyter-Notebooks%3Ffbclid%3DIwAR2mkIp3Xi-3ZAGo6KE_y55UxJqzW_dw1jX2oAnaQOsslT52elyBSnB0pNk&h=AT3c3VoHrLCpkv9N8Mn85Y2oqNWdHWhxwA2y7SWufd3-MbO1OKIafCfCh5b7naY-60ijqQYS8umIB0x2P5grCxlSLX0T7iqulZr3Tno-4FQeaPRXCPecDFcfhbJ-Y07xUV4Xew) |
| Video Tutorials                            | 可以在網路上找到很多關於IPython的教學影片，作者這邊特別推薦PyCon, SciPy和PyData 學術會議上Fernando Perez 和 Brain Granger 的教程，他們是IPython和Jupyter的主要創始人與維護者 |                                                              |





### 2. 相關書籍 

| 書籍                                                         | 說明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Python for Data Analysis                                     | 作者為Wes Mckinney，其中一章節描述如何使用IPython來當數據科學家，也就是IPython如何應用於數據科學 |
| Learning IPython for interactive Computing and Data Visualization： | 作者為Cyrille Rossant，一本簡短的書籍，提供IPython應用於數據上很好的介紹 |
| IPython Interactive Computing and Visualization Cookbook     | 作者為Cyrille Rossant，一本詳盡的書籍，提供IPython應用於數據分析上進階的用法，雖然名為IPython，但實際上內容涵蓋了既有深度與廣度的數據科學議題 |





