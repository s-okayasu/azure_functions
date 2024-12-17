from boxsdk import JWTAuth, Client

# 設定ファイルのパスを指定
config_file = r'784521776_z329yir3_config.json'

# JWTAuth を作成
try:
    auth = JWTAuth.from_settings_file(config_file)
    print("JWTAuth が正しく設定されました。")
except FileNotFoundError:
    print("設定ファイルが見つかりません。")
except Exception as e:
    print(f"エラー: {e}")

# Box クライアントを作成
try:
    client = Client(auth)
    print("Box クライアントが作成されました。")

    # テスト: ルートフォルダのアイテムを取得
    items = client.folder('0').get_items(limit=100)
    for item in items:
        print(f"名前: {item.name}, ID: {item.id}")
except Exception as e:
    print(f"クライアント作成中にエラーが発生しました: {e}")
