# Step2:NLPパート

###2:FileManagerの確認

####step2\_1.py
冗長なプログラムになるのを防ぐために自作関数を作ります  
11行目からの merge\_doc を見ていきましょう  

```sh
def merge_doc(input_data):
    sys.stderr.write("文書の作成")
    attr = input_data[0]
    id_num = attr.index('_N')
    title_num = attr.index('TI')
    abst_num = attr.index('AB')
    doc = []
    for line in input_data[1:]:
        tmp = line[id_num] + '\t' + line[title_num] + '\t' + line[abst_num]
        doc.append(tmp)
    return doc
```

step1で確認したファイルの中から必要な情報のみ取り出しましょう  
今回の解析で必要となるのは  
  
ID:"\_N"列，タイトル:"TI"列，アブストラクト:"AB"列  
  
なので、これらの各行におけるインデックスを最初に取得し  
全ての行から内容を抜き出しましょう  


ポイント  
・関数の作り方  
・index() の使い方  
・for文における１行目の飛ばし方  
・文字の結合  


####step2\_2\_1.py

#####参考サイト 
・TF-IDFの理解の参考になりそうなサイト  
TF-IDFで文洋の単語の重み付け  
<http://takuti.me/note/tf-idf/>  




