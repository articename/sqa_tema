import requests
import abc
import json
import time


class AbstractApiCall(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def request(self):
        pass


class AbstractCache(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def accumulate(self):
        pass

    @abc.abstractmethod
    def check_get(self):
        pass


def get_full_url(url, endpoint, parameters):
    count_of_param = len(parameters)
    if count_of_param == 0:
        param_list = ''
    else:
        param_list = '?'
    num_of_iter = 0
    for key, value in parameters.items():
        if num_of_iter != 0:
            param_list += '&'
        param_list += f'{key}={value}'
        num_of_iter += 1

    full_url = url + endpoint + param_list
    return full_url


class ApiCall(AbstractApiCall):

    def __init__(self, url, api_token):
        super().__init__()
        self.url = url
        self.api_token = api_token
        self.headers = {'apikey': self.api_token}

    def request(self, headers_for_request, parameters, endpoint='', method='get'):
        super().request()
        headers = self.headers
        headers.update(headers_for_request)

        url = get_full_url(self.url, endpoint, parameters)

        match method:
            case 'get':
                req = requests.get(url, headers=headers)
                return req


class Cache(AbstractCache):
    def __init__(self, path='Cache.json'):
        super().__init__()
        self.path = path

    def accumulate(self, url, parameters, data_to_add, endpoint=''):
        super().accumulate()
        key = get_full_url(url, endpoint, parameters)
        try:
            with open(self.path, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}
        data.update({key: data_to_add})
        with open(self.path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def check_get(self, url, parameters, endpoint=''):
        super().check_get()
        key = get_full_url(url, endpoint, parameters)
        try:
            with open(self.path, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}
        received_data = data.get(key)
        return received_data


class Client:
    def __init__(self, url, api_token):
        self.url = url
        self.api_token = api_token
        self.Cache = Cache()
        self.call = ApiCall(self.url, self.api_token)

    def ultimate_request(self, headers_for_request, parameters, endpoint='',
                         method='get', normal_diff = 20):
        data_Cache = self.Cache.check_get(self.url, parameters, endpoint)
        if (data_Cache is None) or (int(round(time.time()))-data_Cache[2]>normal_diff):
            answer = self.call.request(headers_for_request, parameters, endpoint, method)
            self.Cache.accumulate(self.url, parameters, [answer.text, answer.status_code, int(round(time.time()))], endpoint)
            print('111111')
            return [answer.text, answer.status_code]
        else:
            print('222222')
            return [data_Cache[0], data_Cache[1]]
