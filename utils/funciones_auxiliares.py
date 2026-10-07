from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configuración del driver de Chrome (Basado estrictamente en Clase 8)
def setup_driver():
    """Configura y devuelve una instancia del WebDriver de Chrome."""
    chrome_options = Options()
    # Opciones para ejecución en entornos CI o sin interfaz gráfica
    # chrome_options.add_argument("--headless") # Descomenta para modo headless
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Crear el servicio de Chrome
    service = Service()
    
    # Inicializar el driver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver