./totolot/analayze

( データ分析を行うフォルダです )

セットアップ

wget https://raw.githubusercontent.com/takkii/totolot/master/analyze/install.py

python ./install.py

( 2020/03/11 作成 )

python ./ruby-dic3_ana.py

[ 出力結果 ]

                   0
0          nesting\n
1     used_modules\n
2        constants\n
3              new\n
4         allocate\n
...              ...
2622   reiwa_print\n
2623       version\n
2624      himekuri\n
2625         count\n
2626           reiwa

[2627 rows x 1 columns]

※ 読み込む辞書の行数とカウントする文字列を表示しています。

python ./sklearn_dic.py

[ 出力結果 ]

      __callee__  __dir__  __end__  __id__  __method__  __name__  ...  yielder  zero  zerodivisionerror  zip  zone  zoom
0            0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
1            0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
2            0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
3            0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
4            0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
...          ...      ...      ...     ...         ...       ...  ...      ...   ...                ...  ...   ...   ...
2622         0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
2623         0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
2624         0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
2625         0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0
2626         0.0      0.0      0.0     0.0         0.0       0.0  ...      0.0   0.0                0.0  0.0   0.0   0.0

[2627 rows x 2019 columns]

※ 重複していないことが数字でわかります。