# Python_study_group

※ わからないときは相談するようにしましょう  
※ 何箇所か真似する場合はコピペではなく書き写しましょう  
※ 情報をどんどん付け足してもらえると助かります


※ あくまで補助的に理解するために作ったので、伊藤と安田のgitをメインに使いましょう
本家URL  


<https://github.com/double-y/data_analisis_tutorial>

##1:論文ID、タイトル、アブストラクトデータの確認
※ 各データの説明（伊藤作）  
>mission.facet.2.tsv：俯瞰システム内で分析を行ったクラスタ２（ニューラルネットワーク関連のクラスタ）の論文データ  
>（ID:"\_N"列，タイトル:"TI"列，アブストラクト:"AB"列）  

>mission.pairs.tsv：論文IDによる引用関係を示したデータ（引用した論文¥t引用された論文）

>selected\_pairs.tsv：mission.pairs.tsvのうち，クラスタ２に含まれている論文の引用関係を示したもの

>NLPパートでは, mission.facet.2.tsvを用いてください  
>networkxパートでは, mission.pairs.tsvを用いてください  
>分析パートでは, networkxパートで作成した隣接行列を作る関数の入力をselected\_pairs.tsvに置き換え, クラスタ2の引用ネットワークを作成する点に注意をしてください  


####TODO  
・"git clone"する  
・管理者などからtsvデータをもらう  
・中身を確認するプログラムを作成  


####github について
必要に応じて適宜参照  

・gitをコマンドで使えるようにする  
~gitインストールを1分で済ませる【Mac編】~  
<http://www.tettori.net/post/1491/>

・gitのことを学ぶ（ドットインストール）  
<http://dotinstall.com/lessons/basic_git>


##2:NLP（自然言語処理）パート
※ 本格的にデータ解析が始まります多々くじけるとは思いますが頑張りましょう  
※ このパートからは各人が練習を含め_説明を追加していくことを想定して_作ります  

















