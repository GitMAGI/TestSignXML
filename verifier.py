from lxml import etree
from base64 import b64decode
from signxml import XMLVerifier

def VerifyXML(input_file_fullname):
    fh = open(input_file_fullname, 'rb')
    xmlDoc = etree.parse(fh)
    fh.close()

    namespaces = {'ds': 'http://www.w3.org/2000/09/xmldsig#'}
    cert_node = xmlDoc.find("//ds:X509Certificate", namespaces)
    cert = cert_node.text

    #print(cert)
    verified = False
    verified_data = None
    verified_xml = None
    verified_signature_xml = None
    try:
        verified_result = XMLVerifier().verify(xmlDoc, x509_cert = cert)
        verified = True
    except Exception as ex:
        print(str(ex))
        verified = False

     # What are Whole Data have been signed
    verified_data = verified_result.signed_data

    # Whole Signed Data as XML
    verified_xml = verified_result.signed_xml

    # Signed Signature Only XML Element as XML
    verified_signature_xml = verified_result.signature_xml

    return (verified, verified_data, verified_xml, verified_signature_xml)
