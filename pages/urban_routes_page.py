from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR,'.tcard.active .tcard-title')

    phone_number_button = (By.CSS_SELECTOR,'.np-text')
    request_phone_number = (By.CSS_SELECTOR,'.np-input')
    enter_phone_number = (By.ID, 'phone')
    phone_number_field = (By.CSS_SELECTOR,'.np-text')
    next_button = (By.XPATH, '//button[text()="Siguiente"]')
    code = (By.ID, 'code')
    confirm = (By.XPATH, '//button[text()="Confirmar"]')
    phone_number_field_assert = (By.CSS_SELECTOR,'.np-text')

    payment_method = (By.CSS_SELECTOR, '.pp-text')
    add_card_button = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    credit_number = (By.ID, 'number')
    credit_code = (By.CSS_SELECTOR,'input#code.card-input')
    add_button = (By.XPATH, '//button[@class="button full"  and text()="Agregar"]')
    card_1 = (By.ID, 'card-1')
    close_add_card = (By.CSS_SELECTOR,'div.payment-picker.open button.close-button.section-close')


    message = (By.ID, 'comment')
    message_assert = (By.ID, 'comment')

    blanket_handkerchiefs = (By.XPATH, '//div[contains(@class,"r-type-switch")][.//div[contains(@class,"r-sw-label") and normalize-space()="Manta y pañuelos"]]//span[contains(@class,"slider")]')
    blanket_handkerchiefs_assert = (By.XPATH, '//div[contains(@class,"r-type-switch")][.//div[contains(@class,"r-sw-label") and normalize-space()="Manta y pañuelos"]]//input[@type="checkbox"]')

    ice_creem = (By.XPATH, '//div[contains(@class,"r-counter-container")][.//div[contains(@class,"r-counter-label") and normalize-space()="Helado"]]//div[contains(@class,"counter-plus")]')
    ice_creem_assert = (By.XPATH, '//div[contains(@class,"r-counter-container")][.//div[contains(@class,"r-counter-label") and normalize-space()="Helado"]]//div[contains(@class,"counter-value")]')

    call_taxi = (By.CSS_SELECTOR, 'button.smart-button')
    find_taxi_modal = (By.CSS_SELECTOR, 'div.order-body')
    info = (By.XPATH, '//div[contains(@class,"order-header-title") and contains(.,"El conductor llegará")]')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.comfort_icon_assert)
        )

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_request_phone_number(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.request_phone_number)
        )

    def click_phone_number(self):
        self.get_request_phone_number().click()

    def get_set_phone_number(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.enter_phone_number)
        )

    def set_phone_number(self, number):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.enter_phone_number)
        ).send_keys(number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        )
    def click_next_button(self):
        self.get_next_button().click()

    def get_code(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.code)
        )

    def set_code(self, code):
        self.get_code().send_keys(code)

    def get_confirm(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.confirm)
        )

    def click_confirm(self):
        self.get_confirm().click()

    def get_phone_number_field_assert(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.phone_number_field_assert)
        )

    def get_payment_method(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method)
        )

    def click_payment_method(self):
        self.get_payment_method().click()

    def get_add_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_credit_number(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.credit_number)

        )

    def set_credit_number(self,card_number):
        self.get_credit_number().send_keys(card_number)

    def get_credit_code(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.credit_code)
        )

    def set_credit_code(self,card_code):
        self.get_credit_code().send_keys(card_code)
        self.get_credit_code().send_keys(Keys.TAB)

    def get_add_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_button)
        )

    def click_add_button(self):
        self.get_add_button().click()

    def is_card_1_present(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.card_1)
        )

    def get_close_add_card(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.close_add_card)
        )

    def click_close_add_card(self):
        self.get_close_add_card().click()

    def get_message_for_driver(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.message)
        )

    def set_message_for_driver(self,message):
        self.get_message_for_driver().send_keys(message)

    def get_message_for_driver_assert(self):
        return self.driver.find_element(*self.message_assert).get_property('value')

    def get_blanket_handkerchiefs(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.blanket_handkerchiefs)
        )

    def click_blanket_handkerchiefs(self):
        self.get_blanket_handkerchiefs().click()

    def get_blanket_handkerchiefs_assert(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.blanket_handkerchiefs_assert)
        )

    def get_ice_creem(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.ice_creem)
        )

    def click_ice_creem(self):
        self.get_ice_creem().click()

    def get_ice_creem_assert(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.ice_creem_assert)
        )

    def get_call_taxi(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.call_taxi)
        )

    def click_call_taxi(self):
        self.get_call_taxi().click()

    def get_find_taxi_modal(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.find_taxi_modal)
        )

    def get_info(self):
        return WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(self.info)
        )
