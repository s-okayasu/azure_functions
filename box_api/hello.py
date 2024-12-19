from boxsdk import Client, OAuth2

# アクセストークンを使用してBoxクライアントを作成
oauth2 = OAuth2(
    client_id='',
    client_secret='',
    access_token='',
)
client = Client(oauth2)

folder_id = '297827171827'
root_folder = client.folder(folder_id=folder_id)

try:
    # フォルダ内のアイテムを取得
    items = root_folder.get_items()
    print("フォルダ内のアイテム一覧:")
    for item in items:
        print(f"名前: {item.name}, タイプ: {item.type}, ID: {item.id}")

except Exception as e:
    print(f"エラーが発生しました: {e}")
