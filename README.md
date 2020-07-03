**GET:**

curl --location --request GET 'http://127.0.0.1:8000/api/groups/'

curl --location --request GET 'http://127.0.0.1:8000/api/contacts/' | python -mjson.tool

curl -s http://127.0.0.1:8000/api/contacts/ | python -mjson.tool

ANSWER:
[
    {
        "name": "Walter Simpson",
        "phone": 67573,
        "email": "walt@mail.com",
        "id_db_contact": 1,
        "comment": "Clara's husband",
        "group_id": 1
    },
    {
        "name": "Ashley Braun",
        "phone": 568372873,
        "email": "ashley@mail.com",
        "id_db_contact": 2,
        "comment": "friend of Paul",
        "group_id": 1
    }
]
 

-------------------

**POST:**

curl --location --request POST 'http://127.0.0.1:8000/api/contacts/' \
--header 'Content-Type: application/json' \
--data-raw 
'
{
        "name": "Frank Sinatra",
        "phone": 9677563,
        "email": "sina@mail.com",
        "comment": "man from TV show",
        "group_id": 1
}
'


ANSWER:

200 - success
404 - error


-------------------

**PUT:**

curl --location --request PUT 'http://127.0.0.1:8000/api/groups/2' \
--header 'Content-Type: application/json' \
--data-raw 
'
{
    "name": "Party buddies",
    "category": 4
}
'

ANSWER:

200 - success
404 - error

-------------------

**DELETE:**


curl --location --request DELETE 'http://127.0.0.1:8000/api/contacts/2' 


ANSWER:

200 - success
404 - error

*run tests hint:*
cd api_contacts 
$ python django_contacts/manage.py test api