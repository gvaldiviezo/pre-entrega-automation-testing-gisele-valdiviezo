import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones_auxiliares import setup_driver

@pytest.mark.smoke
def test_login_saucedemo():
    """Prueba el inicio de sesión exitoso en SauceDemo y verifica la redirección al inventario."""
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        assert "/inventory.html" in driver.current_url, "Error: No se redirigió a la página de inventario."
        print(" ¡Login exitoso y verificado correctamente!")
        
    finally:
        driver.quit()

@pytest.mark.exception
def test_login_credenciales_invalidas():
    """Prueba el manejo de errores al intentar iniciar sesión con credenciales incorrectas."""
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys("usuario_bloqueado_o_falso")
        driver.find_element(By.ID, "password").send_keys("contraseña_incorrecta")
        driver.find_element(By.ID, "login-button").click()
        
        # Validar que aparezca el mensaje de error en pantalla
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        assert "Epic sadface" in error_msg.text, "No se mostró el mensaje de error esperado."
        print(" ¡Manejo de error de login validado correctamente!")
        
    finally:
        driver.quit()