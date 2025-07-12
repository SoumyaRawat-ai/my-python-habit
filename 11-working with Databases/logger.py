import logging

## configure the basic logging setting
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt= '%Y-%m-%d %H:%H:%S')