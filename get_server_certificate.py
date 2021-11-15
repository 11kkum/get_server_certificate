import ssl
import OpenSSL # required pyopenssl

cert = ssl.get_server_certificate(('www.google.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

print('cert:{}'.format(cert))
print('x509:{}'.format(x509))
