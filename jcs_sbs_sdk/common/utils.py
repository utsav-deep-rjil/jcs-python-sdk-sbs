import re
import constants


type_error_message = "%s must be of type %s."
    
def validate_string(value, name):
    if not isinstance(value, str):
        raise TypeError(type_error_message % (name, "str"))
    value = value.strip()
    if len(value) == 0:
        return None
    return value
    

def validate_positive_int(value, name):
    if not isinstance(value, int):
        raise TypeError(type_error_message % (name, "int"))
    if value < 1:
        raise ValueError("%s must be a positive integer" % (name))
    return value


def validate_generic(value, name, element_type):
    if type(value) != element_type:
        raise TypeError(type_error_message % (name, str(element_type)))
    return value


def validate_list(value, name, element_type):
    if not isinstance(value, list) and all(type(element) == element_type for element in value):
        raise TypeError("%s must be a list having each element of type %s" % (name, str(element_type)))
    return value


def get_protocol_and_host(url):
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
        
        
        