# Challenge2

[![Build Status](https://travis-ci.org/Rhytah/Challenge2.svg?branch=tests)](https://travis-ci.org/Rhytah/Challenge2)  [![Coverage Status](https://coveralls.io/repos/github/Rhytah/Challenge2/badge.svg?branch=tests)](https://coveralls.io/github/Rhytah/Challenge2)
Maintenance Tracker API

Maintenance Tracker-Api is an interface that comprises of a set of endpoints that use data structures to store data in memory

### Tools

* Text editor where we write our project files. (VScode)
* Flask Python Framework -Server-side framework
* Pytest - a Python Testing Framework
* Pylint - a Python linting library 
* Postman -Application to test and consume endpoints
* PEP8 - Style guide

## Getting Started
clone the github repo to your computer:
* $git clone https://github.com/Rhytah/Challenge2
* Extract the zip file to another file

**Create virtual environment and activate it**
```
$pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
``` 
 **Install all the necessary tools by**
 ```
 $pip insatll -r requirements.txt
 ```
**Start app server in console/terminal/commandprompt**
```
$python app.py
```
**Start app in terminal**
```
$python pytest
```
## Versioning
```
This is version one"v1" of the API
```
## End Points(Required Features)
|           End Point                                 |            Functionality                   |
|   -----------------------------------------------   | -----------------------------------------  |
|     POST  auth/register                             |             Register a user                |
|     POST  auth/login                                |             Login a user                   |
|     GET  api/v1/users/requests                      |             Fetch all requests             |
|     GET  api/v1/users/requests/<requestId>          |             Fetch a request                |
|     POST api/v1/users/requests                      |             Add a request                  |
|     PUT  api/v1/users/requests/<requestId>          |             Modify a request               |

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/e53ed3a54e8253e6229e)

## Author
- [Rhytah] https://github.com/Rhytah

