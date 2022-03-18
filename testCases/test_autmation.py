import pytest
from os import *
import pytest_ordering
from API_calls.api_methods import *

_test_obj = api_test()

@pytest.fixture(autouse=True)
def setUp():
    print("\nThis is API testing with 1.Get, 2.Put, 3.Post, 4.Delete methods")
    print("*"*70)

@pytest.mark.run(order=1)
def test_get_method():
    msg = _test_obj.get_resources('https://restful-booker.herokuapp.com/booking')
    return msg

@pytest.mark.run(order=2)
def test_get_single():
    msg = _test_obj.get_resources('https://restful-booker.herokuapp.com/booking/4')
    return msg

@pytest.mark.run(order=3)
def test_post_single():
    _data = {"firstname" : "Dave","lastname" : "Johnson","totalprice" : 11122,"depositpaid" : False,"bookingdates" : {"checkin" : "2018-01-01",
        "checkout" : "2019-01-01"},"additionalneeds" : "Dinner"}
    msg =  _test_obj.create_resource('https://restful-booker.herokuapp.com/booking',_data)
    return msg
@pytest.mark.run(order=4)
def test_post_multiple():
    _data = [{'firstname': 'Susan', 'lastname': 'Jackard', 'totalprice': 900, 'depositpaid': False, 'bookingdates': {'checkin': '2015-02-22', 'checkout'
: '2016-11-19'}, 'additionalneeds': 'Dinner'},{'firstname': 'Frank', 'lastname': 'Tim', 'totalprice': 8900, 'depositpaid': True, 'bookingdates': {'checkin': '2020-02-22', 'checkout'
: '2020-12-31'}, 'additionalneeds': 'Dinner'}]
    msg =  _test_obj.create_resources('https://restful-booker.herokuapp.com/booking',_data)
    return msg
@pytest.mark.run(order=5)
def test_update_single():
    _data = {"firstname": "David", "lastname": "cavin", "totalprice": 1109, "depositpaid": True,
             "bookingdates": {"checkin": "2018-08-01",
                              "checkout": "2019-07-01"}, "additionalneeds": "Dinner"}
    msg = _test_obj.update_resource('https://restful-booker.herokuapp.com/booking/88', _data)
    return msg

@pytest.mark.run(order=6)
def test_delete_single():
    msg = _test_obj.delete_resource('https://restful-booker.herokuapp.com/booking/96')
    return msg

@pytest.mark.run(order=7)
def tearDown():
    print("*"*70)
    print("API testing is successfully completed")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'IMDb project'
    config._metadata['Module Name'] = 'Clients'
    config._metadata['Tester'] = 'Sinchana'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
