import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

"""
Test case practices inpired by "The Art of Software Testing" by Glenford J. Myers, Corey Sandler, and Tom Badgett 
"""

@pytest.mark.usefixtures("chrome_driver_init")
class FrontendTests(StaticLiveServerTestCase):
    
    def side_inputs(self, a, b, c):
        self.driver.get(self.live_server_url)
        input_a = self.driver.find_element_by_id('id_a')
        input_b = self.driver.find_element_by_id('id_b')
        input_c = self.driver.find_element_by_id('id_c')

        # Need to give string to send_keys()
        input_a.send_keys(str(a))
        input_b.send_keys(str(b))
        input_c.send_keys(str(c))

    def test_isScalene(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(3, 4, 5)

        message = self.driver.find_element_by_id('message')
        assert message.text == "A scalene triangle"

    def test_isEquilateral(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(3, 3, 3)

        message = self.driver.find_element_by_id('message')
        assert message.text == "An equilateral triangle"
    
    def test_isIsosceles(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(5, 5, 6)

        message = self.driver.find_element_by_id('message')
        assert message.text == "An isosceles triangle"
        self.side_inputs(5, 6, 5)
        message = self.driver.find_element_by_id('message')
        assert message.text == "An isosceles triangle"
        self.side_inputs(6, 5, 5)
        message = self.driver.find_element_by_id('message')
        assert message.text == "An isosceles triangle"

    def test_Zero(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(3, 0, 3)

        message = self.driver.find_element_by_id('message')
        assert message.text == ""

    def test_Negative(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(-10, 11, 12)

        message = self.driver.find_element_by_id('message')
        assert message.text == "Error: Negative integer is invalid"

    def test_Unvalid1(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(1, 2, 3)

        message = self.driver.find_element_by_id('message')
        assert message.text == "Error: The sum of the lengths of any two sides of a triangle has to be greater than the length of the third side."
        self.side_inputs(2, 2, 4)
        message = self.driver.find_element_by_id('message')
        assert message.text == "Error: The sum of the lengths of any two sides of a triangle has to be greater than the length of the third side."

    def test_Unvalid2(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(1, 2, 30000)

        message = self.driver.find_element_by_id('message')
        assert message.text == "Error: The sum of the lengths of any two sides of a triangle has to be greater than the length of the third side."
        self.side_inputs(1, 2, 4)
        message = self.driver.find_element_by_id('message')
        assert message.text == "Error: The sum of the lengths of any two sides of a triangle has to be greater than the length of the third side."
    
    def test_AllZero(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(0, 0, 0)

        message = self.driver.find_element_by_id('message')
        assert message.text == ""
    
    def test_Decimal(self):
        self.driver.get(self.live_server_url)
        self.side_inputs(5.5, 6.6, 7.7)

        message = self.driver.find_element_by_id('message')
        assert message.text == "Error: Please enter integer value"
    
    def test_OtherInput(self):
        self.driver.get(self.live_server_url)
        self.side_inputs('a', '-', '=')

        message = self.driver.find_element_by_id('message')
        assert message.text == ""
