import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.funciones_auxiliares import setup_driver
import time

@pytest.mark.smoke
def test_navegacion_y_catalogo():
    """Prueba la navegación, verificación del título y la presencia de productos en el catálogo."""
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        titulo_elemento = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header_secondary_container .title"))
        )
        assert titulo_elemento.text == "Products", f"El título esperado era 'Products', pero se obtuvo '{titulo_elemento.text}'"
        
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos visibles en la página."
        
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f" Primer producto -> Nombre: {nombre_producto} | Precio: {precio_producto}")
        time.sleep(1)
        
    finally:
        driver.quit()

@pytest.mark.smoke
def test_interaccion_carrito():
    """Prueba añadir un producto al carrito, verificar el contador (badge) y comprobarlo en el carrito con pausas visuales."""
    driver = setup_driver()
    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]").click()
        time.sleep(1)
        
        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "1", f"El contador del carrito debería mostrar 1, pero muestra {badge.text}"
        time.sleep(1)
        
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        
        cart_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
        )
        assert cart_item.is_displayed(), "El producto no es visible dentro del carrito de compras."
        print(" ¡Producto añadido y verificado en el carrito correctamente!")
        time.sleep(1)
        
    finally:
        driver.quit()