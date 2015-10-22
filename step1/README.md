# Step1:データの確認

###1:FileManagerの確認
FileManager.py（伊藤作）を確認しましょう  
最初はわからない部分が多いと思うので、さらっと見るだけで大丈夫です  

####step1.py
ファイルの出力を見ます  
このまま出力すると大変な事態が起こるので  
```sh
$ control + C  
```
で実行を止めてください  
その後、
"print f" をコメントアウトし、すでに付いているコメントアウトを外して再度実行してください  


２度目の出力結果
```sh
['_N', '_C', '_D', '_E', 'PT', 'AU', 'BA', 'BE', 'GP', 'AF', 'BF', 'CA', 'TI', 'SO', 'SE', 'BS', 'LA', 'DT',  
'CT', 'CY', 'CL', 'SP', 'HO', 'DE', 'ID', 'AB', 'C1', 'RP', 'EM', 'RI', 'OI', 'FU', 'FX', 'CR', 'NR', 'TC',    
'Z9', 'PU', 'PI', 'PA', 'SN', 'EI', 'BN', 'J9', 'JI', 'PD', 'PY', 'VL', 'IS', 'PN', 'SU', 'SI', 'MA', 'BP',   
'EP', 'AR', 'DI', 'D2', 'PG', 'WC', 'SC', 'GA', 'UT', 'PM']

['138', '2', '4002', '2961', 'J', 'HOPFIELD, JJ', '', '', '', 'HOPFIELD, JJ', '', '', 'NEURAL NETWORKS AND   
PHYSICAL SYSTEMS WITH EMERGENT COLLECTIVE COMPUTATIONAL ABILITIES', 'PROCEEDINGS OF THE NATIONAL ACADEMY OF   
SCIENCES OF THE UNITED STATES OF AMERICA-BIOLOGICAL SCIENCES', ' .............................
```
  


FileManager.pyのreadFile()を理解しておきましょう  
```sh
    def readFile(self, fName, pattern):
        print fName + "の読み込み開始"
        f = open(fName)
        lines = f.readlines()
        f.close()
        store = []
        for line in lines:
            line = line[:-1].split(pattern)
            store.append(line)
        return store
```
ポイント  
・関数の呼び出し方  
・openの使い方  
・for文の使い方  
・リストの指定の仕方（line[:-1]）  
・リストへの追加の仕方（append）  
・splitの使い方  



