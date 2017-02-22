import logging

def get_global_logger():
    """
    Returns instance of :obj:`logging` module after performing basic configurations.
    
    Returns:
        (:obj:`logging`) Instance of logging object.
    """
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
    return logging