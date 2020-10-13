#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Author：hms5232
Repo：https://github.com/hms5232/get-LAN-IP-telegram-bot
Bug or suggestion：https://github.com/hms5232/get-LAN-IP-telegram-bot/issues
"""


import platform

from telegram.ext import Updater, CommandHandler
import secret
import ifcfg


# 設定一些個人的環境變數
telegram_bot_token = secret.token


'''
尚未執行機器人之前，可傳送訊息給機器人後至下列網址查看：

	https://api.telegram.org/bot{$token}/getUpdates
'''
updater = Updater(token=telegram_bot_token)  # 呼叫 bot 用


def welcome(bot, update):
	""" Show user welcome message. """
	
	chat_id = update.message.from_user.id
	
	about_bot = ''
	about_bot = about_bot + 'Hello! 感謝您的使用\n'
	about_bot = about_bot + '本機器人由 hms5232 開發\n'
	about_bot = about_bot + '可於 [Github](https://github.com/hms5232) 或 [Gitlab](https://gitlab.com/hms5232) 上找到我\n'
	about_bot = about_bot + '聯絡請走[這邊](https://github.com/hms5232/get-LAN-IP-telegram-bot/issues)\n'
	
	bot.send_message(chat_id, about_bot, parse_mode='Markdown')


def show_user_info(bot, update):
	""" 回覆使用者的資訊 """
	
	user_info = '發送人 id：{}\n'.format(update.message.from_user.id)
	
	update.message.reply_text(user_info, disable_notification="True")


def get_ip(updater):
	""" 找 IP 後回給使用者 """

	if platform.system() != 'Linux':
		'''
		https://docs.python.org/3/library/platform.html#platform.system
		'''
		updater.bot.send_message(uid, 'Not supported OS.')

	# 取得裝置區域網路 ip
	result = ''
	for name, interface in ifcfg.interfaces().items():
		'''
		介面卡1
		IPv4: 127.0.0.1
		Netmask: 255.255.0.0

		介面卡2
		IPv4: 192.168.0.1
		Netmask: 255.0.0.0
		'''
		result += interface['device'] + '\nIPv4: ' + interface['inet'] + '\nNetmask: ' + interface['netmask']
		result += '\n\n'

	# 將設定檔中全部的 id 都傳一輪
	for uid in secret.notify_user_id:
		updater.bot.send_message(uid, result)


updater.dispatcher.add_handler(CommandHandler(['start', 'about'], welcome))  # 歡迎訊息 / 機器人資訊
updater.dispatcher.add_handler(CommandHandler('info', show_user_info))  # 顯示使用者資訊


# 機器人起床!!!
updater.start_polling()
# 找 IP
get_ip(updater)
# 功成身退
updater.stop()
updater.is_idle = False
