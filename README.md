# weather-bot

- 天気は、インターネットがある人にだけ降るわけではない。
- この小さなPython製botは、空の様子を3時間ごとに聞き出し、そっとテキストメールで届けてくれる。
- 指定した地点の予報を集め、決まった時刻にきちんと配達。
- 余計な機能はなく、派手な画面もない。
- ただ、昔ながらの「定時通信」の流儀で、静かに、確実に働き続ける。

## 機能

- OpenWeather APIから天気予報を取得
- 3時間ごとの予報を抽出
- テキストメールで送信
- cronによる定時実行に対応

## 動作環境

- Python 3.9 以上
- インターネット接続
- SMTPで送信可能なメールアカウント
- 自動実行にはcronが必要

## インストール

### 1. リポジトリを取得

```sh
git clone https://github.com/tamasakian/weather-bot.git
cd weather-bot
```

### 2. 仮想環境の作成（任意）

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 必要なパッケージをインストール

```sh
pip install -r requirements.txt
```

## 設定

`config.py` を作成し、以下の内容を記述する。

```python
API_KEY = "あなたの OpenWeather API 鍵"
LATITUDE = "緯度"
LONGITUDE = "経度"

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

SMTP_USER = "your_email@example.com"
SMTP_PASSWORD = "your_password"

FROM_EMAIL = SMTP_USER
TO_EMAIL = "destination@example.com"
```

> [!CAUTION]
> config.py は秘密情報を含むため、公開しないこと。

## 実行方法

### 手動実行

```sh
python3 main.py
```

成功すると、指定したメールアドレスに天気情報が送信される。

### 自動実行（cron設定例）

毎朝5時55分に実行する例

cron.txtを編集

```
55 5 * * * /path/to/.venv/bin/python /path/to/weather-bot/main.py
```

```sh
crontab cron.txt
```

登録できたか確認。

```sh
crontab -l
```

## 出力

```
件名：weather-bot

06時 晴れ 5.1度
09時 晴れ 7.3度
12時 曇り 8.0度
15時 雨 6.4度
18時 曇り 5.9度
21時 晴れ 4.7度
00時 晴れ 4.2度
03時 曇り 3.8度
```

## 使用API

- OpenWeather（無料枠あり）
- https://openweathermap.org/

## 注意事項

- API鍵やメール認証情報は公開しない
- キャリアメールの場合、迷惑メール設定に注意
- cronはPCが起動している時間のみ実行される
