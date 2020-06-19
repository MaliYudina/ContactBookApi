GET:

curl --location --request GET 'http://127.0.0.1:8000/api/authors/'

ANSWER:
{
    "authors": [
        {
            "name": "Kate Willson",
            "email": "my@email.ru",
            "id": 1
        },
        {
            "name": "Bell Winders",
            "email": "winders2@email.com",
            "id": 2
        },
 }
 


curl --location --request GET 'http://127.0.0.1:8000/api/groups/'

-------------------

POST:

curl --location --request POST 'http://127.0.0.1:8000/api/articles/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "article": {
        "title": "Release of research documentation on GHT-6",
        "description": "Results for the latest research",
        "body": "Ipsum Lorem",
        "author_id": "1"
    }
}'


ANSWER:

{"success":"Article 'Release of research documentation on GHT-6' created successfully"}

-------------------

PUT:

curl --location --request PUT 'http://127.0.0.1:8000/api/authors/2' \
--header 'Content-Type: application/json' \
--data-raw '{
    "author": 
        {
            "name": "John Winders",
            "email": "winders2@email.ru"
        }
}'


{
    "success": "Author 'John Winders' updated successfully"
}

-------------------

DELETE:

curl --location --request DELETE 'http://127.0.0.1:8000/api/authors/2' \
--header 'Content-Type: application/json' \
--data-raw '{
    "author": 
        {
            "name": "Bell Winders",
            "email": "winders2@email.ru"
        }
}'

ANSWER:

{
    "message": "Author with id `2` has been deleted."
}