# jcs-python-sdk-sbs
====================

The JCS-SBS (Jio Cloud Services - Simple Block Storage) SDK for Python provides service methods for accessing the APIs provided by JCS-SBS. 
For more information on JCS Services, Console, APIs, and CLIs, see JCS Documentation.

To use it download or clone this project and then install it in your system (or in virtual environment).
After that you can import the classes and services of this SDK in your python project.

To generate documentation, go to docs folder of the project and run `make html` in the terminal.
To view the documentation, go to `docs/build/html` folder and double click the index.html.

Some basic examples for using the SDK is given in this README itself.


Before using the SDK:
=====================

CA-CERTIFICATE INSTALLATION:
----------------------------

**Get the ca-certificate for JIO cloud services from JIO Cloud Team and install it**

- For Linux : Place the ca-certificate inside the folder 
`/usr/local/share/ca-certificates/` and then run `update-ca-certificates --fresh` in terminal

- For Mac : Run the command 
`sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain <certificate>` in terminal 
(replace `<certificate>` with location of the `.crt` file).

- For Windows :
Follow the steps given in this [link](http://www.sqlservermart.com/HowTo/Windows_Import_Certificate.aspx)


Installing the project:
-----------------------

You can install the project either in system root directory or in virtual environment.
But it is recommended to install the project inside a virtual environment. Also, virtual environment lets you access the SDK without root access.

**Steps to setup and activate the virtual environment:**

*Linux and MAC:*

- Open a terminal.
- Run the command 
`virtualenv your_env_name` to setup the virtual environment.

- Run the command
`source your_env_name/bin/activate` to activate it.


*Windows:*

- 
Follow the steps given in this [link](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html)


**Installing the project in virtual environment**

- Now in virtualenv, go to the project's root directory and run the command
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

This file can also serve as an example code for all the operations provided by this SDK.


Examples:
---------

**Describe Volumes**

```
jcs = JCSComputeClient()
response = jcs.describe_volumes()
```

**Create Volume**
```
jcs = JCSComputeClient()
response = jcs.create_volume(size=10)
```







