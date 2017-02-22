import base64
import hashlib
import hmac
import os
import time
import urllib
import six
import string

from credentials import Credentials

from ..common import constants
from ..common import utils

class Authorization(object):
    '''
        Class containing methods responsible for adding authorization parameters in the API request.
        The methods of this class are used internally.
        
        The constructor of this class accepts the following arguments.
         
        Args:
            url (:obj:`str`): Request URL to which authorization parameters are added.
            
            request_method (:obj:`str`): Request method of the target API.
            
            credentials (:class:`jcs_sbs_sdk.auth.credentials.Credentials`): An object of :class:`jcs_sbs_sdk.auth.credentials.Credentials` that contains access and secret keys.
            
            headers (:obj:`dict`): Common headers to add to any API request.
        '''
        
    def __init__(self, url, request_method, credentials, headers):
        
        self._verb = utils.validate_string(request_method, "request_method")
        self._credentials = utils.validate_generic(credentials, "credentials", Credentials)
        self._headers = utils.validate_generic(headers, "headers", type({}))
        self._path = "/"
        protocol_and_host = utils.get_protocol_and_host(utils.validate_string(url, "url"))
        self._protocol = protocol_and_host.get("protocol")
        if self._protocol not in ["http", "https"]:
            raise ValueError("unsupported protocol present in given url : %s" % (url))
        self._host = protocol_and_host.get("host")
        self._port = ""
        
        colon_idx = self._host.find(":")
        
        if colon_idx > 0:
            self._port = self._host[colon_idx + 1:]
            self._host = self._host[:colon_idx]
        
        
    def add_params(self, query_params):
        '''
        Sets the required common parameters such as JCSAccessKeyId,
        SignatureVersion, SignatureMethod, etc., that are used
        to create request URL.
        
        Args:
            query_params (:obj:`dict`): Query parameters to add to the API request
        
        Raises:
            TypeError: If query_param is not of type :obj:`dict`
        '''
        utils.validate_generic(query_params, "query_params", type({}))
        query_params["JCSAccessKeyId"] = self._credentials.access_key
        query_params["SignatureVersion"] = "2"
        query_params["SignatureMethod"] = "HmacSHA256"
        query_params["Version"] = "2016-03-01"
        
        tmp = os.environ.get("TZ")
        os.environ['TZ'] = "GMT"
        
        time.tzset()
        query_params["Timestamp"] = time.strftime(constants.DATE_TIME_FORMAT)
        if tmp:
            os.environ['TZ'] = tmp
        
    def _get_utf8_value(self, value):
        """
        Returns the UTF8-encoded version of a value.
        
        Args:
            value (:obj:`str`): The string value to be converted to UTF8.
                If the given value is not a string then the given value is first converted to :obj:`str`.
                
        Returns:
            The UTF8-encoded version of a value.
        """
        if not isinstance(value, (six.binary_type, six.text_type)):
            value = str(value)
        if isinstance(value, six.text_type):
            return value.encode('utf-8')
        else:
            return value
    
    def serialize_params(self, query_params):
        '''
        Creates URL encoded string having alphabetically sorted keys.
        
        Args:
            query_params (:obj:`dict`): Query parameters to add to the API request.
        
        Raises:
            TypeError: If *query_params* is not a :obj:`dict`.
        '''
        utils.validate_generic(query_params, "query_params", type({}))
        keys = list(query_params)
        keys.sort()
        query_strings = []
        for key in keys:
            value = urllib.quote_plus(self._get_utf8_value(query_params.get(key)))
            query_strings.append("=".join([key, value]))
        return "&".join(query_strings)
    
    def string_to_sign(self, query_params):
        ''' 
        Generates the request string that needs to be signed.
         
        Args:
            query_params (:obj:`dict`): Query parameters to add to the API request.
        
        Returns:
            Request String that needs to be signed.
            
        Raises:
            TypeError: If *query_params* is not a :obj:`dict`.
        '''
        utils.validate_generic(query_params, "query_params", type({}))
        signature_strings = [self._verb, "\n", self._host]
        if self._port != "":
            signature_strings.append(":" + self._port)
        signature_strings.extend(["\n", self._path, "\n"])
        self.add_params(query_params)
        signature_strings.append(self.serialize_params(query_params))
        return "".join(signature_strings)
    
    def add_auth(self, query_params):
        '''
        Adds signature to the *query_params* :obj:`dict`.
         
        Args:
            query_params (:obj:`dict`): Query parameters to add to the API request.
            
        Raises:
            TypeError: If *query_params* is not a :obj:`dict`.
        '''
        utils.validate_generic(query_params, "query_params", type({}))
        hmac_256 = hmac.new(self._credentials.secret_key, digestmod=hashlib.sha256)
        signature_string = self.string_to_sign(query_params)
        hmac_256.update(signature_string.encode('utf-8'))
        b64 = base64.b64encode(hmac_256.digest()).decode('utf-8')
        b64 = urllib.quote(b64)
        b64 = string.replace(b64, "%2F", "/")
        query_params['Signature'] = b64
        