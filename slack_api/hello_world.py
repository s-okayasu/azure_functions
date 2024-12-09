from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import config

CONFIG = config.get_config()

# ボットトークン
SLACK_API_TOKEN = CONFIG['SLACK_API_TOKEN']

# チャンネルID（例: "C01234567"）
SLACK_CHANNEL_ID = CONFIG['SLACK_CHANNEL_ID']

# クライアントの作成
client = WebClient(token=SLACK_API_TOKEN)

try:
    # メッセージ送信
    response = client.chat_postMessage(
        channel=SLACK_CHANNEL_ID,
        text="Hello, world! :tada:"  # メッセージ内容
    )
    print(f"メッセージが送信されました: {response['ts']}")
except SlackApiError as e:
    print(f"エラーが発生しました: {e.response['error']}")
