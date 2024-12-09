import configparser
import os

def get_config():
    # ConfigParserのインスタンス作成
    config = configparser.ConfigParser()

    # 設定ファイル読み込み
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)

    # 値の取得
    config = {
        "SLACK_API_TOKEN" : config['SLACK']['SLACK_API_TOKEN'],
        "SLACK_CHANNEL_ID" : config['SLACK']['SLACK_CHANNEL_ID']
    }

    return config
