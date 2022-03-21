import json, pytest, os

CONFIG_DIR = os.path.join('tests', 'config.json')
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']

# Config fixture - 'session' so it only runs once per session
@pytest.fixture(scope='session')
def config():
    with open(CONFIG_DIR) as config_file:
        config_contents = json.load(config_file)
    return config_contents

# Config-browser validation fixture
@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('"browser" missing from config file')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not supported. ETPDFC01')
    return config['browser']

# Config-wait time validation fixture. Return wait time, or 10
@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

# Generator fixture - called each test
@pytest.fixture
def browser(config_browser, config_wait_time):
    # Setup webdriver
    if config_browser == 'chrome':
        from selenium.webdriver import Chrome
        driver = Chrome()
    elif config_browser == 'firefox':
        from selenium.webdriver import Firefox
        driver = Firefox()
    elif config_browser == 'edge':
        from selenium.webdriver import Edge
        driver = Edge()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser. ETPDFC02')

    # setup wait time
    driver.implicitly_wait(config_wait_time)

    # Return driver to tests that need it
    yield driver

    # Cleanup
    driver.quit()