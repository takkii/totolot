[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)[![GitHub release](https://img.shields.io/github/release/takkii/totolot.svg?style=flat)](GitHub)[![GitHub Status](https://img.shields.io/github/last-commit/takkii/totolot.svg?style=flat)](GitHub)

<div align="center"><img src="https://github.com/takkii/Bignyanco/blob/master/images/python_ruby.gif" alt="Python¤ÈRuby" title="logo"></div>

# Totolot created date [ 2019.01.31 ]

*Made [Python3](https://www.python.org/) (Bignyanco Evolutions)*

#### How To Use

--------------------------------------------------------------------

[ Need [deoplete.nvim](https://github.com/Shougo/deoplete.nvim) ]

```markdown
※「 deoplete requires msgpack 1.0.0+ 」

When you don't understand problem Use Installer!

pip install --upgrade pip

or ( Update pip manually )

python -m pip install --upgrade pip

cd .vim (Vim8)

or ( Select The Env Where The Totolot is Used )

cd .config/nvim (Neovim)

wget https://raw.githubusercontent.com/takkii/totolot/master/install.py

python ./install.py

※ install.py is Windows10/MacOS/LinuMint Python Work.
```

> If you get an error, Please run with root or clone the project or check python version and run install.py.

### Example (Windows) OutPut Results After Running The Installer.

```markdown
CompletedProcess(args=['python', '-m', 'pip', 'uninstall', 'msgpack-python'], returncode=0, stderr='WARNING: Skipping msgpack-python as it is not installed.\n')
Requirement already up-to-date: msgpack in d:\python37\lib\site-packages (1.0.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', '-U', 'msgpack'], returncode=0, stderr='')
Requirement already satisfied: numpy in d:\python37\lib\site-packages (1.18.1)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'numpy'], returncode=0, stderr='')
Requirement already satisfied: pynvim in d:\python37\lib\site-packages (0.4.0)
Requirement already satisfied: msgpack>=0.5.0 in d:\python37\lib\site-packages (from pynvim) (1.0.0)
Requirement already satisfied: greenlet in d:\python37\lib\site-packages (from pynvim) (0.4.15)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'pynvim'], returncode=0, stderr='')
Requirement already satisfied: pandas in d:\python37\lib\site-packages (1.0.1)
Requirement already satisfied: numpy>=1.13.3 in d:\python37\lib\site-packages (from pandas) (1.18.1)
Requirement already satisfied: python-dateutil>=2.6.1 in d:\python37\lib\site-packages (from pandas) (2.8.1)
Requirement already satisfied: pytz>=2017.2 in d:\python37\lib\site-packages (from pandas) (2019.3)
Requirement already satisfied: six>=1.5 in d:\python37\lib\site-packages (from python-dateutil>=2.6.1->pandas) (1.14.0)
CompletedProcess(args=['python', '-m', 'pip', 'install', 'pandas'], returncode=0, stderr='')
```

### ※ Please deoplete and totolot Settting.

--------------------------------------------------------------------

### Use Vim8/Neovim for totolot env, dein plugin manager.

other you use, ['takkii/Bignyanco'](https://github.com/takkii/Bignyanco).

--------------------------------------------------------------------

totolot [ruby-dictionary3](https://github.com/takkii/ruby-dictionary3) read path.

Conditional branch Transplant from [MinTab](https://github.com/takkii/MinTab).

--------------------------------------------------------------------

### [ Only Use Neovim ]

[dein](https://github.com/Shougo/dein.vim) plugin manager,
use case.

[ init.vim / .vimrc ]

```markdown
call dein#add('takkii/totolot')
call dein#add('takkii/ruby-dictionary3')
```

or

[ dein.toml ]

```markdown
[[plugins]]
repo = 'takkii/totolot'

[[plugins]]
repo = 'takkii/ruby-dictionary3'
```

--------------------------------------------------------------------

#### It is necessary to load ruby-dictionary3.

```markdown

Totolot is Vim8/Neovim Plugins, Vim8 set path '~/.cache/dein'

```

#### totolot Sample picture to views [Do_your_Best!]

![background](https://github.com/takkii/totolot/blob/master/images/background.gif)

#### totolot images icon

![totolot](https://github.com/takkii/totolot/blob/master/images/totolot.gif)

Author Takayuki Kamiyama.
