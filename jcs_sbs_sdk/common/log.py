import logging

def get_global_logger():
    """
    Returns instance of 'logging' after doing some basic configurations.
    
    Returns:
        Instance of logging object.
    """
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
    return logging