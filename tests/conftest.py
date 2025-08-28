import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pytest_plugins = ["tests.steps.common_steps"]
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Valid browser options: chrome, edge, firefox"
    )
    parser.addoption(
        "--headless", action="store", default=False, help="Run browser tests in headless mode"
    )

@pytest.fixture(autouse=True)
def driver(request):
    browser = request.config.getoption("browser")
    headless = request.config.getoption("headless")

    options = Options()
    options.add_argument("--disable-gpu")

    if headless:
        options.add_argument("--headless")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == "edge":
        driver = webdriver.Edge(options=options)
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(options=options)
    else:
        raise Exception("Browser name has not been passed or incorrect or not configured in the test.")
    
    driver.implicitly_wait(5)

    # a custom attribute to track whether the driver quit
    driver._already_quit = False

    yield driver

     # Only quit if it hasn't already been quit in the test
    if not driver._already_quit:
        try:
            driver.quit()
        except:
            pass

def pytest_bdd_before_scenario(feature, scenario):
    allure.dynamic.feature(feature.name)
    allure.dynamic.story(scenario.name)

# Attach screenshot to Allure report on scenario failure
@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_after_scenario(request):
    outcome = yield
    if outcome.excinfo:
        driver = request.getfixturevalue('driver')
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )

# @pytest.hookimpl( hookwrapper=True )
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin( 'html' )
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr( report, 'extra', [] )

#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr( report, 'wasxfail' )
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "reports"))
#             file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ).replace("/","_") + ".png" )
#             print( "file name is " + file_name )
#             _capture_screenshot( file_name )
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append( pytest_html.extras.html( html ) )
#         report.extras = extra


# def _capture_screenshot(file_name: str):
#     driver.get_screenshot_as_file(file_name) # type: ignore