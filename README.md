# Django veebiraamistik

## Nõuded
* SQLite3
* Python3 + pip

## Seadistamine

./ kaustas
```
pip install -r requirements.txt
```

Käivitada .*/ kaustas veebiserver käsuga
```
python manage.py runserver
```

Mudelid ja vaated kaustas ./app
Projekti seadistamine (kuhu mingi URL viitab) tehakse läbi ./projekt/urls.py faili

## Andmebaas
Kasutusel SQLite. DB modeleerimiseks alustada ./ kaustas käsuga
```
sqlite3 db.sqlite3
```

Väljumiseks SQLite seest
```
.exit
```
