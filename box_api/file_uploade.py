from boxsdk import Client, OAuth2

# アクセストークンを使用してBoxクライアントを作成
oauth2 = OAuth2(
    client_id='08l9yi0hw47ru94ogbe4v1sct4s0e1ig',
    client_secret='a5GVNYDeHKcrTiqYdBh6NuqTX43MrxTT',
    access_token='UrcAl5eFsVi50UgapZ35QBxTmO5BYUAu',
)
client = Client(oauth2)

folder_id = '297827171827'
root_folder = client.folder(folder_id=folder_id)

# アップロードするファイルのパスと名前
file_path = 'local_file.txt'
file_name = 'local_file.txt'

try:
    # フォルダにファイルをアップロード
    with open(file_path, 'rb') as file:
        uploaded_file = client.folder(folder_id).upload_stream(file, file_name)
        print(f"ファイルがアップロードされました: {uploaded_file.id}")
except Exception as e:
    print(f"エラーが発生しました: {e}")
