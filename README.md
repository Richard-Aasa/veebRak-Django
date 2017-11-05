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

## Mudelid
Mudelid asuvad ./app/models.py kaustas
Peale mudeli loomist tuleb see migreerida andmebaasi
Alguses loome n.ö juhendi migreerimiseks
```
python manage.py makemigrations app
```
Vastus peaks tulema kujul
```
app/migrations/0001_initial.py
```
Seejärel teostame migratsiooni eelmise juhendi alusel
```
python manage.py sqlmigrate app 0001
python manage.py migrate
```


