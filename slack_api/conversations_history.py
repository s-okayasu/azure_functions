from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import config
from datetime import date, datetime, timedelta

# コンフィグ取得
CONFIG = config.get_config()
SLACK_API_TOKEN = CONFIG['SLACK_API_TOKEN']
SLACK_CHANNEL_ID = CONFIG['SLACK_CHANNEL_ID']

SLACK_CHANNEL_ID = CONFIG['SLACK_CHANNEL_ID']
#USERS = CONFIG['USERS']
# クライアントの作成
client = WebClient(token=SLACK_API_TOKEN)

def filter_1(response, current_month):

    pass

def filter_2(start_month, end_month, response):

    pass

def aggregate_weekly_report(response, week):
    # 現在の年と月を取得
    today = date.today()
    year = today.year
    month = today.month

    # 現在の月のすべての水曜日を取得
    wednesdays = get_wednesdays_in_month(year, month)

    # 結果を表示
    print(f"{year}年{month}月の水曜日の日付:")
    for wednesday in wednesdays:
        print(wednesday)


def aggregate_weekly_report_comment(response):

    pass

def conversations_history():
    print("開始:conversations_history")
    response = client.conversations_history(channel=SLACK_CHANNEL_ID)
    for message in response["messages"]:
        if "Hello" in message["text"]:
            print(message["ts"])
    print("終了:conversations_history")


def conversations_replies():
    try:
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
                    _date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                    print(f"メッセージ: {message.get('text')}")
                    print(f"日付: {_date}")
    except SlackApiError as e:
        print(f"エラーが発生しました: {e.response['error']}")

def get_wednesdays_in_month(year, month):
    # 月初めの日付を設定
    first_day = date(year, month, 1)
    # 月の最後の日付を計算
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    last_day = next_month - timedelta(days=1)

    # 水曜日の日付を格納するリスト
    wednesdays = []

    # 月初から月末までの日付を反復
    current_day = first_day
    while current_day <= last_day:
        if current_day.weekday() == 2:  # 0:月曜日, ..., 2:水曜日
            wednesdays.append(current_day)
        current_day += timedelta(days=1)

    return wednesdays


# スクリプトを直接実行した場合にのみ main を呼び出す
if __name__ == "__main__":
    conversations_history()
