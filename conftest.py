import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Configurando opções do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Ativar modo incógnito

    # Inicializando o WebDriver com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def driver_class(request):
    driver = request.config.getoption("driver") or "Chrome"  # Define 'Chrome' como padrão
    if driver is None:
        raise pytest.UsageError("--driver must be specified")
    return driver