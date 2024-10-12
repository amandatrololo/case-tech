import requests
from behave.formatter import json


class APIClient:
    def get_users(self):
        return requests.get("http://jsonplaceholder.typicode.com/users")

    def get_user(self, user_id):  # Adicionar o argumento user_id
        return requests.get(f"http://jsonplaceholder.typicode.com/users/{user_id}")

    def create_user(self, user_data):
        return requests.post("http://jsonplaceholder.typicode.com/users", json=user_data)

    def update_user(self, user_id, user_update):
        return requests.put(f"http://jsonplaceholder.typicode.com/users/{user_id}", json=user_update)

    def delete_user(self, user_id):
        return requests.delete(f"http://jsonplaceholder.typicode.com/users/{user_id}")

    def delete_invalid_user(self):
        return requests.delete(f"http://jsonplaceholder.typicode.com/users/")

    def load_schema(self, schema_path):
        with open(schema_path, 'r') as schema_file:
            return json.load(schema_file)
