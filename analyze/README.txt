./totolot/analyze

( データ分析を行うフォルダです )

~~ 初期設定 ~~

wget https://raw.githubusercontent.com/takkii/totolot/master/analyze/install.py

python ./install.py

( 2020/03/11 作成 )

```markdown
Requirement already satisfied: scikit-learn in d:\python37\lib\site-packages (0.22.2.post1)
Requirement already satisfied: numpy>=1.11.0 in d:\python37\lib\site-packages (from scikit-learn) (1.18.2)
Requirement already satisfied: scipy>=0.17.0 in d:\python37\lib\site-packages (from scikit-learn) (1.4.1)
Requirement already satisfied: joblib>=0.11 in d:\python37\lib\site-packages (from scikit-learn) (0.14.1)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'scikit-learn'], returncode=0, stderr='')
Requirement already satisfied: numpy in d:\python37\lib\site-packages (1.18.2)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'numpy'], returncode=0, stderr='')
Requirement already satisfied: pandas in d:\python37\lib\site-packages (1.0.3)
Requirement already satisfied: python-dateutil>=2.6.1 in d:\python37\lib\site-packages (from pandas) (2.8.1)
Requirement already satisfied: pytz>=2017.2 in d:\python37\lib\site-packages (from pandas) (2019.3)
Requirement already satisfied: numpy>=1.13.3 in d:\python37\lib\site-packages (from pandas) (1.18.2)
Requirement already satisfied: six>=1.5 in d:\python37\lib\site-packages (from python-dateutil>=2.6.1->pandas) (1.14.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'pandas'], returncode=0, stderr='')
Requirement already satisfied: requests in d:\python37\lib\site-packages (2.23.0)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in d:\python37\lib\site-packages (from requests) (1.25.8)
Requirement already satisfied: chardet<4,>=3.0.2 in d:\python37\lib\site-packages (from requests) (3.0.4)
Requirement already satisfied: idna<3,>=2.5 in d:\python37\lib\site-packages (from requests) (2.9)
Requirement already satisfied: certifi>=2017.4.17 in d:\python37\lib\site-packages (from requests) (2019.11.28)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'requests'], returncode=0, stderr='')
```

~~ 実行 ~~

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

╔══════╤════════════╤══════════════╤═════════════╤══════════════╤══════════════╤═══════════╤═════════╤══════════╤════════════════╗
║ Rank │ Country    │ Total Cases  │ New Cases ▲ │ Total Deaths │ New Deaths ▲ │ Recovered │ Active  │ Critical │ Cases / 1M pop ║
╟──────┼────────────┼──────────────┼─────────────┼──────────────┼──────────────┼───────────┼─────────┼──────────┼────────────────╢
║ 1    │ Japan (JP) │        3,139 │             │           77 │              │       514 │   2,548 │       64 │             25 ║
╟──────┼────────────┼──────────────┼─────────────┼──────────────┼──────────────┼───────────┼─────────┼──────────┼────────────────╢
║      │ World      │    1,202,609 │     1,156 ▲ │       64,732 │         44 ▲ │   246,640 │ 891,237 │   42,376 │         154.30 ║
╚══════╧════════════╧══════════════╧═════════════╧══════════════╧══════════════╧═══════════╧═════════╧══════════╧════════════════╝

Stay safe. Stay inside.
Code: https://github.com/sagarkarira/coronavirus-tracker-cli
Twitter: https://twitter.com/ekrysis

Last Updated on: 05-Apr-2020 05:04 UTC

US STATES API: https://corona-stats.online/states/us
HELP: https://corona-stats.online/help

※ 要らないタグを削除してあります。
