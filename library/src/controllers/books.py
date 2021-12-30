from flask import Flask
from flask_restx import Api, Resource

from server.instance import server

app, api = server.app, server.api

books_db = [
    {"id":0, "title": "A Biblia" },
    {"id":1, "title":"Assim falou Zaratrusta"}
]

@api.route("/books")
class BookList(Resource): # Resource: responsável por GET, POST, PUT, DELETE (HTTP)
    def get(self, ):
        return books_db 

