from main import *
import pytest
import time

my_client = Client('https://api.apilayer.com/exchangerates_data', 'Dftk6hUYPZSqm6zabMAV6qaHmhefvr7d')

@pytest.mark.parametrize("headers_for_request, parameters, endpoint, normal_diff, sleep_t", [
    ({}, {'symbols': 'RUB,EUR', 'base': 'USD'}, '/latest', 10, 0),
    ({}, {'symbols': 'RUB,USD', 'base': 'USD'}, '/latest', 10, 2),
    ({}, {'symbols': 'USD,EUR', 'base': 'RUB'}, '/latest', 10, 2),
    ({}, {'symbols': 'USD,EUR', 'base': 'RUB'}, '/latest', 10, 2),
    ({}, {'symbols': 'USD,EUR', 'base': 'RUB'}, '/latest', 1, 2)
])
def test_smoke(headers_for_request, parameters, endpoint, normal_diff,sleep_t):
    time.sleep(sleep_t)
    response = my_client.ultimate_request(headers_for_request=headers_for_request, parameters=parameters, endpoint=endpoint,\
                                          normal_diff=normal_diff)
    print(response[0])
    
