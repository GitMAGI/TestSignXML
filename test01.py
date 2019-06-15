import verifier
import signer

def TestVerify(file_to_analize_fullname):
    print("Verifying of file %s starting ..." % file_to_analize_fullname)

    (verified, verified_data, verified_xml, verified_signature_xml) = verifier.VerifyXML(file_to_analize_fullname)

    if verified:
        print("XML Verified")

        #print(verified_data)
        print(verified_xml)
        print(verified_signature_xml)
    else:
        print("XML NOT Verified")

def TestSign(input_file_fullname, cert_file_fullname, key_file_fullname, output_file_fullname):
    signer.SignXML(input_file_fullname, cert_file_fullname, key_file_fullname, output_file_fullname)