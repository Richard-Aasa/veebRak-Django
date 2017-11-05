import urllib.request
from . import models

dok_meta_dict = {}

def read_from_file(url):
    # url = "http://www.tlu.ee/~jaagup/andmed/keel/korpus/dokmeta.txt"
    file = urllib.request.urlopen(url)
    data_bytes = file.read()
    data_string = data_bytes.decode("utf8")
    file.close()
    return data_string


def save_dok_meta_objects(data_string):
    dok_meta_list = []
    data = data_string.splitlines()

    for i in range(1, len(data)):
        attribute = data[i].split(',')
        dok_meta = models.Dok_Meta()
        dok_meta.kood = attribute[0]
        dok_meta.korpus = attribute[1]
        dok_meta.tekstikeel = attribute[2]
        dok_meta.tekstityyp = attribute[3]
        dok_meta.elukoht = attribute[4]
        dok_meta.taust = attribute[5]
        dok_meta.vanus = attribute[6]
        dok_meta.sugu = attribute[7]
        dok_meta.emakeel = attribute[8]
        dok_meta.kodukeel = attribute[9]
        dok_meta.keeletase = attribute[10]
        dok_meta.haridus = attribute[11]
        dok_meta.abivahendid = attribute[12]
        #dok_meta_list.append(dok_meta)

        dok_meta_dict[dok_meta.kood] = dok_meta

        #if (dok_meta_dict.get('test'))
        #dok_meta.save();
        #print(dok_meta)

    return dok_meta_list
