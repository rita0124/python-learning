# Learn Python
# Python 學習筆記

## 基本資料型別

* **字串 (String)**
    * 一般字元
    * 特殊字元 與 跳脫字元
* **整數 (Integer)**
    * 有號整數
    * 無號整數
    * 長整數
    * **更多內容**請見... [線上文件](https://www.tutorialspoint.com/python3/python_numbers.htm)
* **浮點數 (Float)**
* **串列 (List)** 與 **元組 (Tuple)**
* **字典 (Dictionary)**
* **布林值 (Boolean)**

## 運算 & 運算子

* 加法 +
* 減法 -
* 乘法 *
* 除法 /
* 取次方 / 開根號 **
* 簡略式的寫法 +=, -=, *=, /=
* 其他... 如取對數

## 邏輯 與 Statement

* if / else / elif
* and
* or
* not

 ## List 填充
 ```
 name = [' momo, alex, lulu']
 ```
 * **根據 index 取值**
     使用位移值取得項目
     * name [0]會取出 'momo'
 * **切片 / 選取 index 的範圍**
     使用 slice 取出項目
     * name[0:2]，會取出 'momo, alex'，不包含2
     * name[::2]，會取出 'momo, lulu'，表示每間隔2取出值
 * **附加**
    使用 append 將項目附加到最後
     * name.append('rita')，會印出 [ 'momo, alex, lulu, rita' ]
 * **合併**
     * ** 合併串列用 extend() 或 += 
     other = ['apple, orange']
     name.append(other)會印出 [ 'momo, alex, lulu, appple, orange' ]
     name += other 會印出 [ 'momo, alex, lulu, appple, orange' ]
 * **插入**
    使用 insert(位移值, 項目名稱)插入項目
    name(0, amy)，會印出 [ 'amy, momo, alex, lulu, appple, orange' ]
 * **刪除**
     使用 del, remove(項目名稱), pop(位移值)移除項目
     * 若要刪除'amy', 分別寫法為 del name[0], remove(amy), pop(0)