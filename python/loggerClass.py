
import logging

class Logger:
    def __init__(self):
        # Configuración del logger principal
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
        # Logger para información
        self.info_logger = logging.getLogger('info_logger')
        info_handler = logging.FileHandler('info.log')  # Archivo para logs de información
        info_handler.setLevel(logging.INFO)  # Solo registrar mensajes de INFO
        info_formatter = logging.Formatter('%(asctime)s - INFO - %(message)s')
        info_handler.setFormatter(info_formatter)
        self.info_logger.addHandler(info_handler)

        # Logger para errores
        self.error_logger = logging.getLogger('error_logger')
        error_handler = logging.FileHandler('error.log')  # Archivo para logs de errores
        error_handler.setLevel(logging.ERROR)  # Solo registrar mensajes de ERROR y superiores
        error_formatter = logging.Formatter('%(asctime)s - ERROR - %(message)s')
        error_handler.setFormatter(error_formatter)
        self.error_logger.addHandler(error_handler)

    def log_info(self, message):
        self.info_logger.info(message)
        print(f"Error: {message}")

    def log_error(self, message):
        self.error_logger.error(message)
        print(f"Error: {message}")