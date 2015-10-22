#coding: UTF8

import os
import sys
from FileManager import FileManager

ROOT = os.path.abspath(os.path.dirname(__file__))
TSVDIR = ROOT.replace("/step2", "/tsvdata/")


# タイトルとアブストラクトを結合させて、論文ID\tタイトル\tアブストラクトの文書を作る関数
def merge_doc(input_data):
    sys.stderr.write("文書の作成")

    #"要素名を含んでいる１行目のみ取得"
    attr = input_data[0]
    
    #"必要な要素のインデックス取得"
    id_num = attr.index('_N')
    title_num = attr.index('TI')
    abst_num = attr.index('AB')
    doc = []

    #"各行での結合"
    for line in input_data[1:]:
        tmp = line[id_num] + '\t' + line[title_num] + '\t' + line[abst_num]
        doc.append(tmp)
    return doc


#"メイン関数"
if __name__ == "__main__":

    tsvfile = TSVDIR + "mission.facet.2.tsv"
    
    fm = FileManager()
    f = fm.readFile(tsvfile, '\t')

    #"関数の呼び出し、結合した情報の取得"
    texts = merge_doc(f)

    #"作成したtextsの中身確認"
    print texts[0]
    print texts[1]



