import requests
from utils.config import BASE_URL, AUTH_BASE_URL, HEADERS, AUTH_HEADERS


class APIClient:
    
    # ─── User Management API methods
    def get(self, endpoint):
        return requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS)

    def post(self, endpoint, payload):
        return requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)

    def put(self, endpoint, payload):
        return requests.put(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)

    def delete(self, endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
    
    # ─── Authentication API methods
    def auth_post(self, endpoint, payload):
        return requests.post(f"{AUTH_BASE_URL}{endpoint}", data=payload, headers=AUTH_HEADERS)