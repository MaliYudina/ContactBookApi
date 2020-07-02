*GET:*

curl --location --request GET 'http://127.0.0.1:8000/api/groups/'

curl --location --request GET 'http://127.0.0.1:8000/api/contacts/' | python -mjson.tool

curl -s http://127.0.0.1:8000/api/contacts/ | python -mjson.tool

ANSWER:
[
    {
        "name": "Kate Wilson",
        "phone": 898372873,
        "email": "some@email.com",
        "id_db_contact": 1,
        "comment": "secretary",
        "category": 3,
        "group_id": 1
    },
    {
        "name": "Ashley Braun",
        "phone": 568372873,
        "email": "ashley@mail.com",
        "id_db_contact": 2,
        "comment": "friend of Paul",
        "category": 2,
        "group_id": 1
    }
]
 

-------------------

*POST:*

curl --location --request POST 'http://127.0.0.1:8000/api/contacts/' \
--header 'Content-Type: application/json' \
--data-raw 
'
{
        "name": "Ashley Braun",
        "phone": 568372873,
        "email": "ashley@mail.com",
        "comment": "friend of Paul",
        "category": 2,
        "group_id": 1
}
'


ANSWER:

200 - success
404 - error


-------------------

*PUT:*

partial update available 

curl --location --request PUT 'http://127.0.0.1:8000/api/groups/2' \
--header 'Content-Type: application/json' \
--data-raw 
'
{"name": "Sport"}
'

ANSWER:

200 - success
404 - error

-------------------

*DELETE:*


curl --location --request DELETE 'http://127.0.0.1:8000/api/contacts/2' 


ANSWER:

200 - success
404 - error