import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler()
        ],
        force=True  # asegura configuración limpia aunque ya exista logging previo
    )
