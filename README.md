# TwineProject

This project is a simple Flask application with a RESTful API built by Flask RESTplus
and Swagger UI.

### Install requirements with:

sudo pip install -r requirements.txt

### To run:

python app.py

### To navigate to the front end:

localhost:8000/

You can also use the command to send a get request for data.

For example, to get the compensation base for Equinetworks:
```
requests.get('http://localhost:8000/benchmarks/?company=Equinetworks&metric=compensation_base')
```
