import subprocess
import pytest

ssl_command = "nuclei -u https://api.apilayer.com/exchangerates_data/latest -tags ssl -no-color > /home/tls_info.txt"
sql_command = "nuclei -u https://api.apilayer.com/exchangerates_data/latest -tags sql -no-color > /home/sql_info.txt"

subprocess.run(ssl_command, shell=True, capture_output=True, text=True)
subprocess.run(sql_command, shell=True, capture_output=True, text=True)

def test_tls():
    file_path = '/home/tls_info.txt'
    a = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ('tls-version' in line) and ('tls13' in line):
                print('target uses tls 1.3')
                assert 'tls13' in line, "'target uses tls 1.3'"
            if ('tls-version' in line) and ('tls12' in line):
                print('target uses tls 1.2')
            if ('tls-version' in line) and ('tls11' in line):
                print('target uses tls 1.1')
                a += 1
            if ('tls-version' in line) and ('tls10' in line):
                print('target uses tls 1.0')
                a += 1
    assert a == 0, "!!!test failed!!!"

def test_sql():
    file_path = '/home/sql_info.txt'
    a = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'sql-injection' in line:
                print(line)
                a += 1
    assert a == 0, "!!!test failed!!!"
    

