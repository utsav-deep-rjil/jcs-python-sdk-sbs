# jcs-python-sdk-sbs
=====================

This is the python sdk for APIs provided by Jio Cloud Services - Simple Block Storage.
To use it download or clone this project and then import it in your project.

To generate documentation, go to docs folder of the project and run `make html` in the terminal.
To view the documentation, go to `docs/build/html` folder and double click on index.html.

Some basic examples for using the SDK is given in this README itself.


Before using the SDK:
=====================

CA-CERTIFICATE INSTALLATION:
----------------------------

**Get the ca-certificate for JIO cloud services from JIO Cloud Team and install it**

- For Linux : Place the ca-certificate inside the folder 
`/usr/local/share/ca-certificates/` and then run `update-ca-certificates --fresh` in terminal

- For Mac : 
- For Windows :


Installing the Project:
-----------------------

- 
Setup a virtual environment using command `virtualenv your_env_name` and activate it using `source your_env_name/bin/activate`

- Now in virtualenv, go to the project root directory and run the command
`python setup.py install` to install the SDK.



Setting up the Project Configurations:
--------------------------------------

The following properties must be set for proper working of this SDK:

- BASE_URL
- ACCESS_KEY
- SECRET_KEY

You can set these properties in any of the following locations:

- OS Environment Variables
- In 
`config.properties` file under `fixtures` folder of this project. The content of this file should be like this:

```
[dev]
ACCESS_KEY="JCSAccessKey of staging"
SECRET_KEY="JCSScretKey of staging"
BASE_URL="endpoint or base url of staging"

[prod]
ACCESS_KEY="JCSAccessKey of production"
SECRET_KEY="JCSScretKey of production"
BASE_URL="endpoint or base url of production"

[branch]
# change this to point the script at a specific environment
env=dev
```

Running this SDK to test basic operations:
------------------------------------------

Run the file: `__init__.py` of the root package: `jcs_sbs_sdk`.

This file can also serve as an example code for all the operations provided by this SDK






