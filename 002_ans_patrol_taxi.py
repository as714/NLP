# coding: utf-8

str1=u'パトカー'
str2=u'タクシー'

print(''.join([a + b for a, b in zip(str1, str2)]))

#ループ時に毎回毎回末尾に追加していく方式は実行速度的に問題アリとのこと．
#print(''.join([a + b for a, b in zip(str1, str2)])) として，あとで文字列をまとめて結合させてしまうのがベストらしい．
#''.join() は引数内の要素を '' 内の区切り文字で区切った上で結合するというもの
