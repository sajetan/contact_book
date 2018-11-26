A simple Flask contact book app.

Deployed on Heroku - [Demo](https://basic-contact-app.herokuapp.com)

## Install

```bash
pip install -r requirements.txt
python test.py
```
## Run

```bash
python app.py
```

## Details

* This is a simple CRUD app designed using Flask-Restful
* Has APIs for Add/Edit/Search/Delete of contact
* Session tracking 
* Supports pagination

## Limitations

* Uses sqlite currently for database - when hosted on cloud runs in memory, data stores data in a disk file. Will try to update to Postgres in the next version
* Flask sessions are not a secure way to protect the Flask APIs. Token based authentication/OAuth can be added further.
* Need to work on the scalable approach for database growth. 

Note: This serves as a basic introduction to building apps. This design would not be suitable for a production level deployment. 

Suggestions and edits welcome. 
