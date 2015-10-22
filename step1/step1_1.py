#coding: UTF8

import os
from FileManager import FileManager

#"実行ファイルの場所を指定"
ROOT = os.path.abspath(os.path.dirname(__file__))
#"TSVデータの入っているディレクトリを指定"
TSVDIR = ROOT.replace("/step1", "/tsvdata/")

#"メイン関数"
if __name__ == "__main__":

    #"tsvのファイルの場所を指定します"
    tsvfile = TSVDIR + "mission.facet.2.tsv"

    #"FileManagerを使ってfileを呼び出します"
    fm = FileManager()
    f = fm.readFile(tsvfile, '\t')

    print f





