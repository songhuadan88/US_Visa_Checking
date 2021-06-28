from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from absl import flags
from absl import app
import time

FLAGS = flags.FLAGS

flags.DEFINE_string('consulate', '', 'US consulate, e.g., MUN')
flags.DEFINE_string('ds160', '', 'DS160 number, e.g., AA00123ABC.')


def main(argv):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://ceac.state.gov/CEACStatTracker/Status.aspx')

    # Select non-immigration visa.
    visa_type = Select(driver.find_element_by_id('Visa_Application_Type'))
    visa_type.select_by_value('NIV')

    # Select the consulate.
    location = Select(driver.find_element_by_id('Location_Dropdown'))
    location.select_by_value(FLAGS.consulate)

    # Fill with DS160 number.
    case_number = driver.find_element_by_id('Visa_Case_Number')
    case_number.send_keys(FLAGS.ds160)

    # Focus on captcha to input.
    driver.find_element_by_id('Captcha').click()

    # Sleep some time, to allow user input the Captcha and check result.
    time.sleep(120)


if __name__ == '__main__':
    app.run(main)
