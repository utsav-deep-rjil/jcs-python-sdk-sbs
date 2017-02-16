import ConfigParser, os
import re

import constants
import log


LOG = log.get_global_logger()

type_error_message = "%s must be of type %s."
    
def validate_string(value, name):
    """
    Validates if the given *value* is a string or not. If the value is a string, it returns the trimmed value.
    
    Args:
        value (:obj:`str`): The value that needs validation.
        
        name (:obj:`str`): The name of the given value used in the error message.
        
    Raises:
        TypeError: If the given *value* is not a :obj:`str`.
    """
    if not isinstance(value, str):
        raise TypeError(type_error_message % (name, "str"))
    value = value.strip()
    if len(value) == 0:
        return None
    return value
    

def validate_positive_int(value, name):
    """
    Validates if the given *value* is a positive integer or not.
    
    Args:
        value (+ve :obj:`int`): The value that needs validation.
        
        name (:obj:`str`): The name of the given *value* used in the error message.
        
    Raises:
        TypeError: If the given *value* is not a positive :obj:`int`.
    """
    if not isinstance(value, int):
        raise TypeError(type_error_message % (name, "int"))
    if value < 1:
        raise ValueError("%s must be a positive integer" % (name))
    return value


def validate_generic(value, name, element_type):
    """
    Validates if the given *value* is an instance of 'element_type' or not.
    
    Args:
        value: The value that needs validation.
        
        name (:obj:`str`): The name of the given *value* used in the error message.
        
    Raises:
        TypeError: If the given *value* is not of type 'element_type'.
    """
    if type(value) != element_type:
        raise TypeError(type_error_message % (name, str(element_type)))
    return value


def validate_list(value, name, element_type):
    """
    Validates if the given *value* is a list or not.
    
    Args:
        value (:obj:`list`): The value that needs validation.
        
        name (:obj:`str`): The name of the given *value* used in the error message.
        
    Raises:
        TypeError: If the given *value* is not a :obj:`list` of given 'element_type' type.
    """
    if not isinstance(value, list) and all(type(element) == element_type for element in value):
        raise TypeError("%s must be a list having each element of type %s" % (name, str(element_type)))
    return value


def get_protocol_and_host(url):
    """
    Splits the protocol and host portions from the given *url* and returns a :obj:`dict` containing the *protocol* and *host* keys.
    If the given value of the *url* is not valid, then the values of the *protocol* and *host* keys are set to empty strings.

    Args:
        url (:obj:`str`): The URL from which the *protocol* and *host* values are extracted.
        
    Returns:
        (:obj:`dict`) A dict containing  *protocol* and *host* keys.
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
    Returns an instance of :class:`ConfigParser` object that reads values from 'fixtures/config.properties' file.
    
    Returns:
        An instance of :class:`ConfigParser` object.
    """
    
    ROOT = os.path.dirname(__file__)
    config = ConfigParser.RawConfigParser()
    config_path = ROOT+"/../../fixtures/config.properties"
    if os.path.exists(config_path):
        config.read(config_path)
    else:
        LOG.warn("%s not found",config_path)
        return None
    return config
