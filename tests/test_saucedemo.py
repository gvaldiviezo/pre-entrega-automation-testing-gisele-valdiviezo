from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones_auxiliares import setup_driver

def test_login_saucedemo():
    """Prueba el inicio de sesión exitoso en SauceDemo y verifica la redirección al inventario."""
    driver = setup_driver()
    try:
        # 1. Navegar a la página de login de saucedemo.com
        driver.get("https://www.saucedemo.com/")
        
        # 2. Esperar a que se cargue el campo de usuario e ingresar credenciales válidas
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # 3. Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()
        
        # 4. Validar login exitoso verificando redirección a /inventory.html y presencia de elementos clave
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        assert "/inventory.html" in driver.current_url, "Error: No se redirigió a la página de inventario."
        
        print(" ¡Login exitoso y verificado correctamente!")
        
    finally:
        # Cerrar el navegador al finalizar la prueba
        driver.quit()