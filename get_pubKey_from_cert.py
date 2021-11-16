import OpenSSL

def get_pubkey(file_path):
  """証明書から公開鍵を取得する."""
  # 証明書をopen
  pem_file = open(file_path, 'rb')

  # byteに変換
  buffer = pem_file.read()

  # 証明書を読み込み
  pemCert = OpenSSL.crypto.load_certificate(
        OpenSSL.crypto.FILETYPE_PEM, buffer)

  # 公開鍵を取得
  pubkey = OpenSSL.crypto.dump_publickey(
    OpenSSL.crypto.FILETYPE_PEM, pemCert.get_pubkey())


  f = open('pubkey.pem', 'w')
  f.write(str(pubkey,encoding='utf-8'))
  f.close()

get_pubkey('./sources.pem')
