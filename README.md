# [livremarketplace](https://salomax-marketplace.appspot.com)
[![Build Status](https://travis-ci.org/salomax/livremarketplace.svg?branch=master)](https://travis-ci.org/salomax/livremarketplace)
[![Code Climate](https://codeclimate.com/github/salomax/livremarketplace/badges/gpa.svg)](https://codeclimate.com/github/salomax/livremarketplace) [![Coverage Status](https://coveralls.io/repos/github/salomax/livremarketplace/badge.svg?branch=master)](https://coveralls.io/github/salomax/livremarketplace?branch=master) [![Issue Count](https://codeclimate.com/github/salomax/livremarketplace/badges/issue_count.svg)](https://codeclimate.com/github/salomax/livremarketplace) [![Gitter](https://badges.gitter.im/salomax/livremarketplace.svg)](https://gitter.im/salomax/livremarketplace?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

open source light ERP for e-commerces

### Enviroment

- Google Appengine (Endpoints API) and Datastore
- Python
- Bootstrap and JQuery

### Modules
- Products
- Suppliers
- Customers
- Purchases
- Sales
- Cash Flow
- Dashboard with many metrics
- Reports

### ROADMAP
- Integration with Correios, MercadoLivre and eBay
- Android and iOS clients

### Release Notes

- [v0.1.0-alpha](https://github.com/salomax/livremarketplace/milestones/v0.1.0-alpha) scheduled to 03/15/2016
 
### Git

	git add .
	git commit -m "Comments"
	git push

### Dev server

	$ dev_appserver.py . --log_level=debug [--clear_datastore] [--clear_search_indexes]

### Upload Application (Example)

	$ appcfg.py -A salomax-marketplace update .

### WebClient

	https://your-app-id.appspot.com/

### Endpoints API

	http://your-app-id.appspot.com/_ah/api/explorer

## Tests
  
### Install and Run

    $ pip install coverage 
    $ coverage run --source=app livremarketplace_test.py

### Create a Test Case

Add module in the livremarketplace_test.py

```python
# Add modules to test over here
MODULES_TO_TEST = ['example_test', ...]
```

Create your test case in /app_test

```python
# Import super class TestCase
import from test_utils import TestCase

class YourTestCase(TestCase):
""" Test case example.
"""

# Override setUp() to create a webtest
def setUp(self):

# Call super method
super(YourTestCase, self).setUp()

#  Create service
YourService = endpoints.api_server(
    [CustomerService], restricted=False)

# Create test
self.testapp = webtest.TestApp(YourService)    

... 
```

### Mock

Make sure mock has installed

	$ pip install mock
	
Use mock

```python
from mock import MagicMock

something = MagicMock(return_value=None)

something()
```

### Configure SSL

For more info check [Using custom domains and ssl](https://cloud.google.com/appengine/docs/python/console/using-custom-domains-and-ssl).

Generate key and crs
 
	$ openssl req -new -nodes -keyout yourname.key -out yourname.csr

Send to CA the .crs generated
Retrieve from CA .zip with certificate
Concat
	
	$ cat www_example_com.crt ASecureServerCA.crt ATrustCA.crt ATrustExternal.crt > concat.crt

Generate unencrypted format
	
	$ openssl rsa -in yourname.key -out yourname.key.pem 

Match 

	$ openssl x509 -noout -modulus -in concat.crt | openssl md5
	$ openssl rsa -noout -modulus -in yourname.key.pem | openssl md5

Upload to appengine

## License

See [LICENSE](https://github.com/salomax/livremarketplace/blob/master/LICENSE).	
