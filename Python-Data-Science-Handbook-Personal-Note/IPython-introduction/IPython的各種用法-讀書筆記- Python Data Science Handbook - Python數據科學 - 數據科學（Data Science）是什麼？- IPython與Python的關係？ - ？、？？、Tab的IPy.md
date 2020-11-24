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