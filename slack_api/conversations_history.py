from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import config
from datetime import datetime

# コンフィグ取得
CONFIG = config.get_config()
SLACK_API_TOKEN = CONFIG['SLACK_API_TOKEN']
SLACK_CHANNEL_ID = CONFIG['SLACK_CHANNEL_ID']
USERS = CONFIG['USERS']
# クライアントの作成
client = WebClient(token=SLACK_API_TOKEN)

try:
    print("開始: conversations_history")

    '''
    # メッセージ取得
    response = client.conversations_history(channel=SLACK_CHANNEL_ID)
    for message in response["messages"]:
        if "Hello" in message["text"]:
            response2 = client.conversations_replies(
                channel=SLACK_CHANNEL_ID,
                ts=message["ts"],
                limit=100
            )
            #print(message["ts"])
            #print(response2)
            messages2 = response2.get("messages",[])
            for message2 in response2["messages"]:
                pass
                #print(f"message: {message2}")

            # 日付に変換
            ts = message.get("ts")  # タイムスタンプ
            if ts:
                timestamp = float(ts)
                date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                #print(f"メッセージ: {message.get('text')}")
                #print(f"日付: {date}")
    '''
except SlackApiError as e:
    print(f"エラーが発生しました: {e.response['error']}")

print("終了: conversations_history")
