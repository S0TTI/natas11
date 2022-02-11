import base64
import json

#defdata = {"showpassword":"no","bgcolor":"#ffffff"}
defdata = {"showpassword":"yes","bgcolor":"#ffffff"}
#keydata = base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=").decode("UTF-8")
keydata = "qw8J"
textdata = json.dumps(defdata)
outtext = ""
d = []

for i in range(len(textdata)):
    m = [(ord(a)^ord(b)) for a,b in zip(textdata[i],keydata[i%len(keydata)])]
    outtext += (chr(m[0]))
#print(outtext)
print(base64.b64encode(outtext.encode('ascii')))
