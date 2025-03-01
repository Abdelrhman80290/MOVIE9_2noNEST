import logging

# API Keys
TMDB_API_KEY = "8e189679b6876e2d56b2c8c12df5ea52"
BOT_TOKEN = "8114555250:AAFsFfu6bhoHy9jazmKlTuPVUBWTpC3XmOY"

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Cache dictionary
cache = {}
