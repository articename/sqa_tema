# sqa_tema
File name                  | File content
---------------------------|----------------------
Dockerfile.txt             | This dockerfile is needed to create the image. The created image contains all necessary dependencies and components for successful launching of information security tests (ib_tests.py).
Dockerfile_smoke.txt       | This dockerfile is needed to create the image. The created image contains all necessary dependencies and components for successful launching of smoke tests (smoke_tests.py).
ib_tests.py                | This file containing two tests. The first one checks the tls protocol version, the test is considered passed if tls version 1.2 or higher is used. The second test checks endpoints for sql injection, the test is considered passed if no information is found that the endpoint is subject to sql injection.
smoke_tests.py             | This file containing the tests. Checking the work of API call classes written in the file (main.py). The tests check the fact of successful communication with api, as well as the work of the cache.
main.py                    | This file contains classes of api (https://api.apilayer.com/exchangerates_data/) call, cache storing answers to the request for a specified time, as well as a client class combining the logic of the two previous classes.
requirements.txt           | This file contains dependencies required for classes (main.py) and smoke tests (smoke_tests.py) to work.
work_of_ib_tests.png       | This picture shows how the security tests work.
work_of_smoke_tests1.png   | This picture shows how smoke tests work, part 1.
work_of_smoke_tests1.png   | This picture shows how smoke tests work, part 2.
ib_check.docx              | This file containing description of API security tests.
README.md                  | You are currently reading this file.
