# Step1:データの確認

###1:FileManagerの確認
FileManager.py（伊藤くん作）を確認しましょう  
最初はわからない部分が多いと思うので、さらっと見るだけで大丈夫です  

####step1\_1.py
ファイルの出力を見ます  
このまま出力すると大変な事態が起こるので  
```sh
$ control + C  
```
で実行を止めてください  


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




