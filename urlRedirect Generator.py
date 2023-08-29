def TextToHex(txt):
    return txt.encode("utf-8").hex()

def ToUrlHex(strHex):
    strHex = str(strHex)
    urlHex = ""
    for i in range(len(strHex)):
        if (i % 2) == 0:
            urlHex+='%'
        urlHex += strHex[i]
    return urlHex


def ToUrl(strHex):
    url = "https://www.google.com/search?btnI&q=//" + strHex
    return url

def CreateURL(txt):
    hex = ToUrlHex(TextToHex(txt))
    return ToUrl(hex)

while True:
    text = input("\n Enter the link: ")
    print(CreateURL(text))



""" 
https://www.youtube.com/watch?v=dQw4w9WgXcQ

https://www.google.com/search?btnI&q=//%68%74%74%70%73%3a%2f%2f%77%77%77%2e%79%6f%75%74%75%62%65%2e%63%6f%6d%2f%77%61%74%63%68%3f%76%3d%64%51%77%34%77%39%57%67%58%63%51 
"""