"""
Contains constants that are used internally across the SDK.
"""

#:Regex used for extracting the values of protocol and host from an URL.
PROTOCOL_AND_HOST_REGEX = "(http[s]?)://((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"

#:The date and time format used for setting the 'Timestamp' field required for any API request.
DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

#:The date and time format used for converting datetime field in the API response to the python datetime object.
RESPONSE_DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
