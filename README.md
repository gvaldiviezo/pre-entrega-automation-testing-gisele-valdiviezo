# Pre-Entrega Automation Testing - SauceDemo

**Autora:** Gisele Valdiviezo  

## 📌 Propósito del Proyecto
Proyecto de automatización de pruebas End-to-End (E2E) desarrollado para la plataforma [SauceDemo](https://www.saucedemo.com), aplicando los conocimientos de localización de elementos, interacciones web y sincronización con Selenium WebDriver y Pytest.

## 🚀 Tecnologías Utilizadas
- Python
- Selenium WebDriver
- Pytest
- Git y GitHub

---

## 📂 Estructura del Proyecto
```text
pre-entrega-automation-testing-gisele-valdiviezo/
│
├── tests/                    # Carpeta contenedora de los casos de prueba
│   ├── test_login.py         # Pruebas de inicio de sesión (éxito y errores)
│   └── test_catalogo_carrito.py # Pruebas de navegación, catálogo e interacción con el carrito
│
├── utils/                    # Funciones y componentes reutilizables
│   └── funciones_auxiliares.py # Configuración centralizada del WebDriver de Chrome
│
├── reports/                  # Carpeta de salida para los reportes HTML de Pytest
├── pytest.ini                # Archivo de configuración global de Pytest y marcadores
└── README.md                 # Documentación y manual del proyecto
```

---

## 🛠️ Instalación y Configuración Inicial

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/pre-entrega-automation-testing-gisele-valdiviezo.git
   cd pre-entrega-automation-testing-gisele-valdiviezo
   ```

2. **Instalar las dependencias necesarias:**
   Ejecuta el siguiente comando en tu terminal para instalar Selenium y el plugin de reportes HTML de Pytest:
   ```bash
   pip install selenium
   pip install pytest pytest-html
   ```

---

## ⚙️ Cómo Ejecutar las Pruebas
El proyecto está diseñado para ejecutarse mediante comandos de Pytest en la terminal, aprovechando el soporte por módulo (`-m`). A continuación se detallan las distintas formas de ejecución:

### 1. Ejecutar todas las pruebas del proyecto de forma unificada
Este comando buscará y ejecutará todos los archivos de prueba dentro de la carpeta `tests/` mostrando un detalle paso a paso:
```bash
python -m pytest -v
```

### 2. Ejecutar pruebas críticas mediante el marcador `smoke`
El marcador `smoke` agrupa las pruebas principales y críticas del flujo de negocio (como el login exitoso, la validación del catálogo y el proceso de compra/carrito):
```bash
python -m pytest -v -m smoke
```
* **¿Qué valida?** Verifica que los flujos principales de la aplicación respondan correctamente sin errores bloqueantes.

### 3. Ejecutar pruebas de manejo de errores mediante el marcador `exception`
Este marcador se utiliza para aislar y probar los escenarios negativos o de validación de fallos:
```bash
python -m pytest -v -m exception
```
* **¿Qué valida?** Comprueba que la aplicación maneje adecuadamente los errores, por ejemplo, mostrando el mensaje de alerta correspondiente ante credenciales de usuario inválidas.

---

## 📊 Generación de Reportes HTML
Para respaldar la ejecución de las pruebas mediante un informe visual, el proyecto permite compilar los resultados en un archivo HTML interactivo y autónomo.

Ejecuta el siguiente comando en la raíz del proyecto:
```bash
python -m pytest -v --html=reports/reporte.html --self-contained-html
```

* **Explicación de los parámetros:**
  * `-v`: Ejecuta en modo verboso, listando el nombre y estado de cada test.
  * `--html=reports/reporte.html`: Indica a Pytest que compile los resultados y guarde el archivo en la carpeta `reports/` con el nombre `reporte.html`.
  * `--self-contained-html`: Empaqueta todos los estilos, gráficos y datos en un único archivo HTML autocontenido, facilitando su visualización en cualquier navegador o su adjunto en revisiones de código.