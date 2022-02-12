import base64
import json

defdata = {"showpassword":"no","bgcolor":"#ffffff"}
#defdata = {"showpassword":"yes","bgcolor":"#ffffff"}
keydata = base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=").decode("UTF-8")
#keydata = "qw8J"
textdata = json.dumps(defdata)
outtext = ""

for i in range(len(textdata)):
    ti = textdata[i]
    ki = keydata[i%len(keydata)]
    outtext += chr(ord(ti)^ord(ki))
print(outtext)
#print(base64.b64encode(outtext.encode('ascii')))