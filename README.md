# get-LAN-IP-telegram-bot
拿到區域網路 IP 並傳給你的 Telegram bot

## ⚠️重要

**此專案已經停止開發，隨時可能停止維護（屆時將會封存），請轉移至使用 Rust 重寫的全新版本：https://github.com/hms5232/get-LAN-IP-telegram-bot-rs**

中文介紹文章及使用說明，請見[〈讓 Telegram bot 告訴你樹莓派的 IP 吧！（Rust version）〉](https://hhming.moe/post/get-lan-ip-through-telegram-bot-rs-version/)

## 介紹
厭煩常常跑掉的樹莓派 IP 讓你遠端失敗了嗎？可是設定 mail 又很麻煩，掃描區域網路又要花不少時間該怎麼辦？別擔心，這個專案就是用在這時候的！準備好使用你的 Telegram bot 來幫你拿 IP 並坐著等訊息吧！

## 需求
* 目前先 Linux 限定
* Python 3.7 或更新的版本
* pip

## 部署
### 系統
1. 安裝 pip3： `sudo apt install python3-pip`
2. 安裝部分相依套件： `sudo apt install libffi-dev libssl-dev`
3. （可選）安裝 [Poetry](https://python-poetry.org/)：https://python-poetry.org/docs/#installation
### 專案
1. Clone this project `git clone https://github.com/hms5232/get-LAN-IP-telegram-bot.git` or [download zip](https://github.com/hms5232/get-LAN-IP-telegram-bot/archive/main.zip)
2. cd into project dir
1. `cp config.py secret.py`
2. edit `secret.py` file for your env
4. 安裝第三方 Python 套件：
	* 直接安裝
		1. 安裝 [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)： `pip3 install python-telegram-bot==12.5`
		2. 安裝 [ifcfg](https://pypi.org/project/ifcfg/)： `pip3 install ifcfg`
	* Poetry
		`poetry install`

## 使用
* 使用一般方法安裝者： `python3 bot.py`
* 使用 Poetry 者： `poetry run python3 bot.py`

## LICENSE
See [LICENSE](LICENSE) file.
