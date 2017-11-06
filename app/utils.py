import urllib.request
from . import models
from django.apps import apps
#raamatud_dict = {}
#omanikud_dict = {}

def read_from_file(url):
    file = urllib.request.urlopen(url)
    data_bytes = file.read()
    data_string = data_bytes.decode("utf8")
    file.close()
    return data_string

def save_raamatud(data_string):
    
    data = data_string.splitlines()
    dataLen = len(data)
    
    kasKirjetearvudSamad = (models.raamatud.objects.all().count() >= (dataLen-1))
    
    if(not kasKirjetearvudSamad):    
        for i in range(1, dataLen):
            attribute = data[i].split(',')
            model = models.raamatud()
            omanikeModel = models.omanikud()
            model.raamatu_nr = attribute[0]
            model.raamatu_nimi = attribute[1]
            model.raamatu_lehti = attribute[2]
            
            model.save()
            for item in models.omanikud.objects.all():
                #kui omanikul on see raamat
                if(int(item.omatud_raamatu_nr) == int(attribute[0])):
                    #print(item.omatud_raamatu_nr)
                    model.omanikud.add(item)
            #key_exists = raamatud_dict.get(model.raamatu_nr, 'None')
            #exists_in_db = models.raamatud.objects.get(id = attribute[0])
            #print(exists_in_db)
            #if (key_exists == 'None'):
                #raamatud_dict[model.raamatu_nr] = "exists"
            

def save_omanikud(data_string):
    data = data_string.splitlines()    
    dataLen = len(data)
    
    kasKirjetearvudSamad = (models.raamatud.objects.all().count() >= (dataLen-1))
    
    if(not kasKirjetearvudSamad):
    
        for i in range(1, dataLen):
            attribute = data[i].split(',')
            model = models.omanikud()
            model.id = attribute[0]
            model.omaniku_nr = attribute[1]
            model.omanik_nimi = attribute[2]
            model.omatud_raamatu_nr = attribute[3]        
            model.save()
            #key_exists = omanikud_dict.get(attribute[0], 'None')
            #exists_in_db = models.omanikud.objects.get(id = attribute[0])
            #print(exists_in_db)
            #if (key_exists == 'None'):
                #omanikud_dict[attribute[0]] = "exists"
            #if (exists_in_db == 'Null'):
            