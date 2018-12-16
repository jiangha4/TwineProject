# TwineProject

This project is a simple python3 Flask application with a RESTful API built by Flask RESTplus
and Swagger UI.

Note: Please use python3 to run and install. This app uses the math library functions that
are present in python3 but not python2.

### Install requirements with:
```
sudo pip3 install -r requirements.txt
```
### To run:
```
python3 app.py
```
### To navigate to the front end:
```
localhost:8000/
```
You can also use the command line to send a get request for data.

For example, to get the compensation base for Equinetworks:
```
requests.get('http://localhost:8000/benchmarks/?company=Equinetworks&metric=compensation_base')
```
