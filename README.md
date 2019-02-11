# notice_global_ip  

## Overview
グローバルIPの切り替わりをメールで通知するスクリプト。  
外出先からRDPやSSHなどで自宅のPCにアクセスする場合、グローバルIPをメモしておく必要があるが、
いちいち確認するのは面倒なので、一連の処理を自動化してメールで通知するようにした。

## How to use
````
$ git clone https://github.com/casshy/notice_global_ip.git

# 以下のURLを参考にGmail APIを有効化する。
# https://developers.google.com/gmail/api/quickstart/python
# ダウンロードしたcredentials.jsonをクローンしたディレクトリに移動

# 必要なパッケージをインストール
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# emailアドレスを設定
$ vim check_and_send.py
...
# change following email address
sender = 'example@gmail.com'
to = 'example@gmail.com'
...

# run.sh内のpythonへのパスを変更
$ vim run.sh
#!/bin/bash
cd `dirname $0`
path/to/python check_and_send.py

# crontabの設定(毎時0分に実行する場合)
$ vim cron.conf
0 * * * * your/working/directory/run.sh

# crontabに登録
$ crontab cron.conf
````
