
from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../pytest07')
from main import app

Client = TestClient(app)
_id = None


def test_hello_msg():
    url = "/hello"
    expected_result = {"msg": "Hello World"}
    actual_result = Client.get(url)
    assert actual_result.status_code == 200
    assert actual_result.json() == expected_result


def test_post_insert():
    url = "/"
    actual_result = Client.post( 
        url,
        json={
            
            "course_code": "SWE62-353",
            "course_name": "TDD",
            "year": 3,
            "group": 1,
            "number": 30
        }
    )
    expected_result = "SWE62-353"
    global _id
    _id = actual_result.json()['data'][0]['id']
    assert actual_result.status_code == 200
    assert actual_result.json()['data'][0]['course_code'] == expected_result


def test_get_all():
    url = "/"
    actual_result = Client.get(url)
    assert actual_result.status_code == 200


def test_get_by_id():
    url = "/"+_id
    actual_result = Client.get(url)
    expected_result = "SWE62-353"
    assert actual_result.status_code == 200
    assert actual_result.json()['data'][0]['course_code'] == expected_result
    

def test_put_by_id():
    url = "/"+_id
    actual_result = Client.put(
        url,
        json={
            "course_code": "SWE77-799",
            "course_name": "Test9999",
            "year": 2,
            "group": 10,
            "number": 1000
        }
    )
    expected_result = "SWE77-799"
    assert actual_result.status_code == 200
    assert actual_result.json()['data'][0]['course_code'] == expected_result


def test_delete_by_id():
    url = "/"+_id
    actual_result = Client.delete(url)
    assert actual_result.status_code == 200
    assert actual_result.json()['status'] == "ok"
