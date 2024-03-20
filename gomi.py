import requests
import datetime

# LINE Notifyのトークンをここに設定してください
LINE_NOTIFY_TOKEN = "d4DssQgrmBdaTS7WG1W3Cb0pGY6FJYm0Vor03MaeJ7x"

# 沖縄市のゴミ収集スケジュール
garbage_schedule = {
    "Monday": "可燃ゴミ",
    "Tuesday": "プラスチックリサイクルゴミ",
    "Wednesday": "紙リサイクルゴミ",
    "Thursday": "不燃ゴミ",
    "Friday": "ガラスリサイクルゴミ",
    "Saturday": "缶リサイクルゴミ",
    "Sunday": "回収なし"
}

# 現在の曜日を取得
today = datetime.datetime.now().strftime("%A")

# 今日のゴミの種類を取得
garbage_type = garbage_schedule.get(today, "不明")

# 通知メッセージを作成
message = f"今日の沖縄市のゴミ収集は: {garbage_type}"

# LINE Notifyを介してメッセージを送信
headers = {"Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"}
payload = {"message": message}
response = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=payload)

# レスポンスを表示
print(response.text)

