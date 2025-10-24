from OpenSSL import crypto
from socket import gethostname

# Crear certificado autofirmado
key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)

cert = crypto.X509()
cert.get_subject().CN = gethostname()
cert.set_serial_number(1000)
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(31536000)  # 1 año
cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, "sha256")

# Guardar archivos
open("cert.pem", "wt").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
open("key.pem", "wt").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode("utf-8"))

print("✅ Certificado generado correctamente (cert.pem y key.pem).")
