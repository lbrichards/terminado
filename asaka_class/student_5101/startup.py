import IPython
t1 = u""" \
安積高校の皆様、Python言語基礎知識講座へようこそ。　　"""

print(t1, end="\n")
print(u"""こちらは、ウェブブラウザー埋め込み型IPythonのインタラクティブシェルです。この中に入力されるpythonコマンドは即実行されます。   """, end="")
print("\n\n")
IPython.start_ipython()