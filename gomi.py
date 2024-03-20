import requests
from datetime import datetime

# LINE Notifyのアクセストークンを設定してください
access_token = "d4DssQgrmBdaTS7WG1W3Cb0pGY6FJYm0Vor03MaeJ7x"

# ゴミの日の曜日ごとの通知メッセージを定義します
garbage_days = {
    "月曜日": "燃えるゴミの日です。",
    "火曜日": "資源ごみの日です。",
    "水曜日": "燃えるゴミの日です。",
    "木曜日": "不燃ごみの日です。",
    "金曜日": "資源ごみの日です。",
    "土曜日": "燃えるゴミの日です。",
    "日曜日": "不燃ごみの日です。"
}

# 今日の曜日を取得します
today = datetime.now().strftime("%A")

# 曜日に対応するメッセージを取得します
message = garbage_days.get(today, "今日はゴミの日ではありません。")

# LINE NotifyのAPIエンドポイントを設定します
url = "https://notify-api.line.me/api/notify"

# アクセストークンをヘッダーに設定します
headers = {
    "Authorization": f"Bearer {access_token}"
}

# メッセージをペイロードに設定します
payload = {
    "message": message
}

# 通知を送信します
response = requests.post(url, headers=headers, data=payload)

# 通知が成功したかどうかを確認します
if response.status_code == 200:
    print(f"{today}のゴミの日を通知しました！")
else:
    print(f"通知の送信中にエラーが発生しました。ステータスコード: {response.status_code}")
