import ssl
import OpenSSL # required pyopenssl
import settings

SOURCE = settings.SOURCE
cert = ssl.get_server_certificate((SOURCE, 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

# print('cert:{}'.format(cert))
print('x509:{}'.format(x509))

f = open('sources.pem','w')
f.write(cert)
f.close()

# f = open('x509.pem','w')
# f.write(x509)
# f.close()
