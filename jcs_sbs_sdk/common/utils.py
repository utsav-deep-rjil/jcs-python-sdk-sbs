import ConfigParser, os
import re

import constants
import log


LOG = log.get_global_logger()

type_error_message = "%s must be of type %s."
    
def validate_string(value, name):
    """
    Validates if the given 'value' is a string or not. If the value is a string, it returns the trimmed value.
    
    Args:
        value (str): The 'value' to be tested.
        
        name (str): The name of the given value used in the error message.
        
    Raises:
        TypeError: If the given 'value' is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(type_error_message % (name, "str"))
    value = value.strip()
    if len(value) == 0:
        return None
    return value
    

def validate_positive_int(value, name):
    """
    Validates if the given 'value' is a positive integer or not.
    
    Args:
        value (+ve int): The 'value' to be tested.
        
        name (str): The name of the given 'value' used in the error message.
        
    Raises:
        TypeError: If the given 'value' is not a positive integer.
    """
    if not isinstance(value, int):
        raise TypeError(type_error_message % (name, "int"))
    if value < 1:
        raise ValueError("%s must be a positive integer" % (name))
    return value


def validate_generic(value, name, element_type):
    """
    Validates if the given 'value' is an instance of 'element_type' or not.
    
    Args:
        value: The 'value' to be tested.
        
        name (str): The name of the given 'value' used in the error message.
        
    Raises:
        TypeError: If the given 'value' is not of type 'element_type'.
    """
    if type(value) != element_type:
        raise TypeError(type_error_message % (name, str(element_type)))
    return value


def validate_list(value, name, element_type):
    """
    Validates if the given 'value' is a list or not.
    
    Args:
        value: The 'value' to be tested.
        
        name (str): The name of the given 'value' used in the error message.
        
    Raises:
        TypeError: If the given 'value' is not of type 'element_type'.
    """
    if not isinstance(value, list) and all(type(element) == element_type for element in value):
        raise TypeError("%s must be a list having each element of type %s" % (name, str(element_type)))
    return value


def get_protocol_and_host(url):
    """
    Splits protocol and host from given 'url' and returns a dict having keys 'protocol' and 'host'.
    If the given value of 'url' is not a valid URL then values of 'protocol' and 'host' are set to empty strings.
    
    Args:
        url (str): The url whose 'protocol' and 'host' needs to be found.
        
    Returns:
        A dict containing 'protocol' and 'host' values.
    """
    protocol_and_host = {}
    compiled_regex = re.compile(constants.PROTOCOL_AND_HOST_REGEX)
    result = compiled_regex.match(url)
    if result is None:
        protocol_and_host["protocol"] = ""
        protocol_and_host["host"] = ""
    else:
        protocol_and_host["protocol"] = result.group(1)
        protocol_and_host["host"] = result.group(2)
    return protocol_and_host
        

def get_config():
    """
    Returns an instance of ConfigParser object that reads values from 'fixtures/config.properties' file.
    
    Returns:
        An instance of ConfigParser object.
    """
    config = ConfigParser.RawConfigParser()
    if os.path.exists("../../fixtures/config.properties"):
        config.read("../../fixtures/config.properties")
    else:
        LOG.warn("%s/../../fixtures/config.properties not found", os.getcwd())
    return config
