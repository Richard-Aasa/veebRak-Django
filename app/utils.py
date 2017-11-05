import urllib.request


def read_from_file(url):
    #url = "http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokmeta.txt"
    file = urllib.request.urlopen(url)
    bytes = file.read()
    string = bytes.decode("utf8")
    file.close()
    return string
