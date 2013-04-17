evidenceupload
==============

Upload your evidence for the Boston Marathon bombings

# Getting started

Create a virtualenv and install the requirements:

```
$ mkvirtualenv evidenceupload
$ cd evidenceupload
$ source bin/activate
(evidenceupload)$ pip install -r requirements.txt
```

Export your Filepicker.io API key:

```
$ export FILEPICKER_API_KEY=XXXXXXXXXXXXXXX
```

Sync the database and start the server:

```
(evidenceupload)$ cd evidenceupload
(evidenceupload)$ python manage.py syncdb
(evidenceupload)$ python manage.py runserver
```

