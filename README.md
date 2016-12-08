# jcs-python-sdk-sbs
=====================

This is the python sdk for APIs provided by Jio Cloud Services - Simple Block Storage.
To use it download or clone this project and then import it in your project.

Some basic examples for using the SDK is given in this README itself.


Before using the SDK:
=====================

CA-CERTIFICATE INSTALLATION:
----------------------------

- 
**Get the ca-certificate for JIO cloud services from JIO Cloud Team and install it**

- For Linux : Place the ca-certificate inside the folder 
*/usr/local/share/ca-certificates/* and then run *update-ca-certificates --fresh* in terminal

- For Mac : 
- For Windows :


Setting up the Project:
-----------------------

The following properties must be set for proper working of this SDK:

- BASE_URL
- ACCESS_KEY
- SECRET_KEY

You can set these properties in any of the following locations:

- OS Environment Variables
- In 
*config.properties* file under *fixtures* folder of this project. The content of this file must be like this:

```
[dev]
ACCESS_KEY=*JCSAccessKey of staging*
SECRET_KEY=*JCSScretKey of staging*
BASE_URL=*endpoint or base url of staging*

[prod]
ACCESS_KEY=*JCSAccessKey of production*
SECRET_KEY=*JCSScretKey of production*
BASE_URL=*endpoint or base url of production*

[branch]
# change this to point the script at a specific environment
env=dev
```

Running this SDK to test basic operations:
------------------------------------------

Run the file: *__init__.py* of the package: *jcs_sbs_sdk.main*.

This file can also serve as an example code for all the operations provided by this SDK






