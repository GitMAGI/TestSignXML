from lxml import etree
from base64 import b64decode
from signxml import XMLVerifier
import os

path_asset = "asset"
#certificate_filename = "cert.pem"
#private_key_filename = "key.pem"

file_to_analize = "esempio_2019_05_04.cap"
#file_to_analize = "esempio_2019_05_04_edit.cap"

fh = open(os.path.join(path_asset, file_to_analize), 'rb')
xmlDoc = etree.parse(fh)
fh.close()

namespaces = {'ds': 'http://www.w3.org/2000/09/xmldsig#'}
cert_node = xmlDoc.find("//ds:X509Certificate", namespaces)
cert = cert_node.text

#print(cert)
verified = False
try:
    verified_result = XMLVerifier().verify(xmlDoc, x509_cert = cert)
    verified = True
except:
    verified = False

if verified:
    # What are Whole Data have been signed
    verified_data = verified_result.signed_data

    # Whole Signed Data as XML
    verified_xml = verified_result.signed_xml

    # Signed Signature Only XML Element as XML
    verified_signature_xml = verified_result.signature_xml

    print("XML Verified")

    #print(verified_data)
    print(verified_xml)
    print(verified_signature_xml)
else:
    print("XML NOT Verified")