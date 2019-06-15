from lxml import etree
from base64 import b64decode
import signxml
from signxml import XMLVerifier, XMLSigner

def SignXML(input_file_fullname, cert_file_fullname, key_file_fullname, output_file_fullname):
    fh = open(input_file_fullname, 'rb')
    xmlDoc = etree.parse(fh)
    fh.close()

    #cert = open(cert_file_fullname).read()   
    #key = open(key_file_fullname).read()

    with open(cert_file_fullname, 'rb') as cert_file:    
        cert = cert_file.read()    
         
    with open(key_file_fullname, 'rb') as key_file:
        key = key_file.read()

    root = xmlDoc.getroot()

    signed_root_restricted = XMLSigner(
        method = signxml.methods.enveloped, 
        signature_algorithm=u'rsa-sha256', 
        digest_algorithm=u'sha256', 
        c14n_algorithm=u'http://www.w3.org/2006/12/xml-c14n11'
    ).sign(root, key = key, cert = cert)
    
    xmlDocSigned = etree.ElementTree(signed_root_restricted)    
    
    #print("xmlDoc Type %s " % type(xmlDoc))
    #print("root Type %s " % type(root))
    #print("signed_root_restricted Type %s " % type(signed_root_restricted))
    #print("xmlDoc Type %s " % type(xmlDocSigned))    
    #print(etree.tostring(xmlDocSigned))

    fw = open(output_file_fullname, 'wb+')
    xmlDocSigned.write(fw, xml_declaration=True, encoding='UTF-8')
    fw.close()
        
    return xmlDocSigned