import os
import test01
import time

path_asset = "asset"
path_input = "Input"
path_output = "Output"
path_cap_certificate = "CAPCertificate"
path_personal_certificate = ""
certificate_filename = "cert.pem"
private_key_filename = "key.pem"

file_to_analize = "esempio_2019_05_04.cap"
#file_to_analize = "esempio_2019_05_04_edit.cap"

#file_to_analize_fullname = os.path.join(path_asset, path_output, file_to_analize)
file_to_analize_fullname = os.path.join("/", "Workspace", "TFS", "GenericPurposesSolution", "CA_Crypto", "asset", "Output", file_to_analize)

certificate_full_filename = os.path.join(path_asset, path_cap_certificate, certificate_filename)
private_key_full_filename = os.path.join(path_asset, path_cap_certificate, private_key_filename)

file_to_sign = "esempio_2019_05_04_unsigned.cap"
#file_to_sign_fullname = os.path.join(path_asset, path_input, file_to_sign)
file_to_sign_fullname = os.path.join("/", "Workspace", "TFS", "GenericPurposesSolution", "CA_Crypto", "asset", "Input", file_to_sign)

file_signed = os.path.splitext(file_to_sign)[0] + "_" + "signed" + "_" + time.strftime("%Y%m%d_%H%M%S") + os.path.splitext(file_to_sign)[1]
file_signed_fullname = os.path.join(path_asset, path_output, file_signed)

test01.TestSign(file_to_sign_fullname, certificate_full_filename, private_key_full_filename, file_signed_fullname)

test01.TestVerify(file_signed_fullname)

#test01.TestVerify(file_to_analize_fullname)