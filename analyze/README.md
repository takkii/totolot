### ./totolot/analyze

```markdown
( データ分析を行うフォルダです )
```

#### ~~ 初期設定 ~~

```markdown
wget https://raw.githubusercontent.com/takkii/totolot/master/analyze/install.py

python ./install.py
```

#### 作成日 2020/04/09

```markdown
Requirement already satisfied: scikit-learn in d:\python37\lib\site-packages (0.22.2.post1)
Requirement already satisfied: scipy>=0.17.0 in d:\python37\lib\site-packages (from scikit-learn) (1.4.1)
Requirement already satisfied: joblib>=0.11 in d:\python37\lib\site-packages (from scikit-learn) (0.14.1)
Requirement already satisfied: numpy>=1.11.0 in d:\python37\lib\site-packages (from scikit-learn) (1.18.2)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'scikit-learn'], returncode=0, stderr='')
Requirement already satisfied: numpy in d:\python37\lib\site-packages (1.18.2)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'numpy'], returncode=0, stderr='')
Requirement already satisfied: pandas in d:\python37\lib\site-packages (1.0.3)
Requirement already satisfied: numpy>=1.13.3 in d:\python37\lib\site-packages (from pandas) (1.18.2)
Requirement already satisfied: pytz>=2017.2 in d:\python37\lib\site-packages (from pandas) (2019.3)
Requirement already satisfied: python-dateutil>=2.6.1 in d:\python37\lib\site-packages (from pandas) (2.8.1)
Requirement already satisfied: six>=1.5 in d:\python37\lib\site-packages (from python-dateutil>=2.6.1->pandas) (1.14.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'pandas'], returncode=0, stderr='')
Requirement already satisfied: requests-html in d:\python37\lib\site-packages (0.10.0)
Requirement already satisfied: pyquery in d:\python37\lib\site-packages (from requests-html) (1.4.1)
Requirement already satisfied: parse in d:\python37\lib\site-packages (from requests-html) (1.15.0)
Requirement already satisfied: bs4 in d:\python37\lib\site-packages (from requests-html) (0.0.1)
Requirement already satisfied: pyppeteer>=0.0.14 in d:\python37\lib\site-packages (from requests-html) (0.0.25)
Requirement already satisfied: fake-useragent in d:\python37\lib\site-packages (from requests-html) (0.1.11)
Requirement already satisfied: w3lib in d:\python37\lib\site-packages (from requests-html) (1.21.0)
Requirement already satisfied: requests in d:\python37\lib\site-packages (from requests-html) (2.23.0)
Requirement already satisfied: lxml>=2.1 in d:\python37\lib\site-packages (from pyquery->requests-html) (4.5.0)
Requirement already satisfied: cssselect>0.7.9 in d:\python37\lib\site-packages (from pyquery->requests-html) (1.1.0)
Requirement already satisfied: beautifulsoup4 in d:\python37\lib\site-packages (from bs4->requests-html) (4.9.0)
Requirement already satisfied: pyee in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (7.0.1)
Requirement already satisfied: websockets in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (8.1)
Requirement already satisfied: appdirs in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (1.4.3)
Requirement already satisfied: urllib3 in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (1.25.8)
Requirement already satisfied: tqdm in d:\python37\lib\site-packages (from pyppeteer>=0.0.14->requests-html) (4.45.0)
Requirement already satisfied: six>=1.4.1 in d:\python37\lib\site-packages (from w3lib->requests-html) (1.14.0)
Requirement already satisfied: chardet<4,>=3.0.2 in d:\python37\lib\site-packages (from requests->requests-html) (3.0.4)
Requirement already satisfied: idna<3,>=2.5 in d:\python37\lib\site-packages (from requests->requests-html) (2.9)
Requirement already satisfied: certifi>=2017.4.17 in d:\python37\lib\site-packages (from requests->requests-html) (2019.11.28)
Requirement already satisfied: soupsieve>1.2 in d:\python37\lib\site-packages (from beautifulsoup4->bs4->requests-html) (2.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'requests-html'], returncode=0, stderr='')
Requirement already satisfied: beautifulsoup4 in d:\python37\lib\site-packages (4.9.0)
Requirement already satisfied: soupsieve>1.2 in d:\python37\lib\site-packages (from beautifulsoup4) (2.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'beautifulsoup4'], returncode=0, stderr='')
```

### ~~ 実行 ~~

```markdown
python ./ruby-dic3_ana.py
```

#### [ 出力結果 ]

```markdown
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
```

#### ※ 読み込む辞書の行数とカウントする文字列を表示しています。

```markdown
python ./sklearn_dic.py
```

### [ 出力結果 ]

```markdown
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
```

#### ※ 重複していないことが数字でわかります。

```markdown
Coronavirus Tracker

╔══════╤════════════╤══════════════╤═════════════╤══════════════╤══════════════╤═══════════╤═══════════╤══════════╤════════════════╗
║ Rank │ Country    │ Total Cases  │ New Cases ▲ │ Total Deaths │ New Deaths ▲ │ Recovered │ Active    │ Critical │ Cases / 1M pop ║
╟──────┼────────────┼──────────────┼─────────────┼──────────────┼──────────────┼───────────┼───────────┼──────────┼────────────────╢
║ 1    │ Japan (JP) │        4,667 │             │           94 │              │       632 │     3,941 │       99 │             37 ║
╟──────┼────────────┼──────────────┼─────────────┼──────────────┼──────────────┼───────────┼───────────┼──────────┼────────────────╢
║      │ World      │    1,518,773 │       813 ▲ │       88,505 │         50 ▲ │   330,589 │ 1,099,679 │   48,079 │         194.86 ║
╚══════╧════════════╧══════════════╧═════════════╧══════════════╧══════════════╧═══════════╧═══════════╧══════════╧════════════════╝

Stay safe. Stay inside.
Code: https://github.com/sagarkarira/coronavirus-tracker-cli
Twitter: https://twitter.com/ekrysis

Last Updated on: 09-Apr-2020 06:04 UTC

US STATES API: https://corona-stats.online/states/us
HELP: https://corona-stats.online/help
SPONSORED BY: ZEIT NOW
```

#### ※ CSSを非表示にしました。

![corona_ja_result_image](https://github.com/takkii/totolot/blob/master/images/corona_ja_result.png)

### PythonでTcl/Tkを使用しコンソール画像を表示しました。

![corona_ja_result_movie](https://github.com/takkii/totolot/blob/master/images/corona_movie.gif)

### Pythonを実行する様子を動画にしました。
