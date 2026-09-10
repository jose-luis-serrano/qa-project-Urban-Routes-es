from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage
from helpers.retrieve_code import retrieve_phone_code

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)


    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        comfort_tariff = routes_page.get_comfort_icon_assert().text
        assert comfort_tariff == 'Comfort'

    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()

        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()
        add_phone_number = routes_page.get_phone_number_field_assert().text
        assert add_phone_number == number


    def test_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()

        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_number(card_number)
        routes_page.set_credit_code(card_code)
        routes_page.click_add_button()
        routes_page.click_close_add_card()
        assert routes_page.is_card_1_present()

    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_number(card_number)
        routes_page.set_credit_code(card_code)
        routes_page.click_add_button()
        routes_page.click_close_add_card()

        message= data.message_for_driver
        routes_page.set_message_for_driver(message)
        message_for_driver = routes_page.get_message_for_driver_assert()
        assert message_for_driver == message

    def test_blanket_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_number(card_number)
        routes_page.set_credit_code(card_code)
        routes_page.click_add_button()
        routes_page.click_close_add_card()
        message = data.message_for_driver
        routes_page.set_message_for_driver(message)

        routes_page.click_blanket_handkerchiefs()
        checkbox = routes_page.get_blanket_handkerchiefs_assert()
        assert checkbox.is_selected()

    def test_ice_creem(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_number(card_number)
        routes_page.set_credit_code(card_code)
        routes_page.click_add_button()
        routes_page.click_close_add_card()
        message = data.message_for_driver
        routes_page.set_message_for_driver(message)
        routes_page.click_blanket_handkerchiefs()

        routes_page.click_ice_creem()
        routes_page.click_ice_creem()
        ice_creem = routes_page.get_ice_creem_assert()
        assert ice_creem.text == '2'

    def test_call_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_number(card_number)
        routes_page.set_credit_code(card_code)
        routes_page.click_add_button()
        routes_page.click_close_add_card()
        message = data.message_for_driver
        routes_page.set_message_for_driver(message)
        routes_page.click_blanket_handkerchiefs()
        routes_page.click_ice_creem()
        routes_page.click_ice_creem()

        routes_page.click_call_taxi()
        taxi_modal = routes_page.get_find_taxi_modal()
        assert taxi_modal.is_displayed()

    def test_driver_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_icon()
        routes_page.click_phone_number_button()
        routes_page.click_phone_number()
        number = data.phone_number
        routes_page.set_phone_number(number)
        routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm()
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_credit_number(card_number)
        routes_page.set_credit_code(card_code)
        routes_page.click_add_button()
        routes_page.click_close_add_card()
        message = data.message_for_driver
        routes_page.set_message_for_driver(message)
        routes_page.click_blanket_handkerchiefs()
        routes_page.click_ice_creem()
        routes_page.click_ice_creem()
        routes_page.click_call_taxi()

        info = routes_page.get_info()
        assert "El conductor llegará" in info.text




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
