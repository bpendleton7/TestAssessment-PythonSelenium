from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class TestAssessment():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_assessment(self):
    # Open page URL and set window size
    self.driver.get("https://www.demoblaze.com/")
    self.driver.maximize_window()

    # Create User
    self.driver.find_element(By.ID, "signin2").click() 
    self.driver.find_element(By.ID, "sign-username").click()
    self.driver.find_element(By.ID, "sign-username").send_keys("test71322")
    self.driver.find_element(By.ID, "sign-password").click()
    self.driver.find_element(By.ID, "sign-password").send_keys("test71322")
    self.driver.find_element(By.CSS_SELECTOR, "#signInModal .btn-primary").click()
    alert = Alert(self.driver)
    msg_sign_up = alert.text()
    assert msg_sign_up == "Sign up successful."
    alert.accept()

    # Login with new user
    self.driver.find_element(By.ID, "login2").click()
    self.driver.find_element(By.ID, "loginusername").click()
    self.driver.find_element(By.ID, "loginusername").send_keys("test71322")
    self.driver.find_element(By.ID, "loginpassword").click()
    self.driver.find_element(By.ID, "loginpassword").send_keys("test71322")
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
    assert self.driver.find_element(By.ID, "nameofuser").is_displayed

    # Add 2 items to cart
    self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    alert = Alert(self.driver)
    msg_product_added = alert.text()
    assert msg_product_added == "Product added."
    alert.accept()
    self.driver.find_element(By.ID, "nava").click()
    self.driver.find_element(By.LINK_TEXT, "Sony vaio i7").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    alert = Alert(self.driver)
    msg_product_added = alert.text()
    assert msg_product_added == "Product added."
    alert.accept()

    # Navigate to cart
    self.driver.find_element(By.ID, "cartur").click()

    # Enter information on form
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("test")
    self.driver.find_element(By.ID, "country").send_keys("USA")
    self.driver.find_element(By.ID, "city").send_keys("NYC")
    self.driver.find_element(By.ID, "card").send_keys("1111222233334444")
    self.driver.find_element(By.ID, "month").send_keys("02")
    self.driver.find_element(By.ID, "year").send_keys("2025")

    # Click Cancel
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-secondary").click()

    # Delete 2 items from cart
    self.driver.find_element(By.LINK_TEXT, "Delete").click()
    self.driver.find_element(By.LINK_TEXT, "Delete").click()

    # Logout
    self.driver.find_element(By.ID, "logout2").click()

    # Login again
    self.driver.find_element(By.ID, "login2").click()
    self.driver.find_element(By.ID, "loginusername").click()
    self.driver.find_element(By.ID, "loginusername").send_keys("test71322")
    self.driver.find_element(By.ID, "loginpassword").send_keys("test71322")
    self.driver.find_element(By.CSS_SELECTOR, "#logInModal .btn-primary").click()
    assert self.driver.find_element(By.ID, "nameofuser").is_displayed

    # Navigate to cart and assert there is nothing in the cart
    self.driver.find_element(By.ID, "cartur").click()
    assert not len(self.driver.find_element(By.LINK_TEXT, "Delete"))

    # Add 1 item to cart
    self.driver.find_element(By.ID, "nava").click()
    self.driver.find_element(By.LINK_TEXT, "Nokia lumia 1520").click()
    self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
    alert = Alert(self.driver)
    msg_product_added = alert.text()
    assert msg_product_added == "Product added."
    alert.accept()

    # Navigate to cart
    self.driver.find_element(By.ID, "cartur").click()

    # Enter information
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("test")
    self.driver.find_element(By.ID, "country").send_keys("USA")
    self.driver.find_element(By.ID, "city").send_keys("NYC")
    self.driver.find_element(By.ID, "card").send_keys("1111222233334444")
    self.driver.find_element(By.ID, "month").send_keys("02")
    self.driver.find_element(By.ID, "year").send_keys("2025")

    # Click cancel
    self.driver.find_element(By.CSS_SELECTOR, "#orderModal .btn-secondary").click()

    # Delete item from cart
    self.driver.find_element(By.LINK_TEXT, "Delete").click()

    # Logout
    self.driver.find_element(By.ID, "logout2").click()
  
