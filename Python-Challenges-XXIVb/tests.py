import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_create_device(self):

        x = Device(7)

        self.assertEqual(x.get_power_state(), False)


        x = Device(7)

        self.assertEqual(x.get_power_state(), False)

  def test_turn_on(self):
        x = Device(7)

        x.turn_on()

        self.assertEqual(x.get_power_state(), True)


        x = Device(7)

        x.turn_on()

        self.assertEqual(x.get_power_state(), True)


  def test_turn_off(self):

        x = Device(7)

        x.turn_on()

        x.turn_off()

        self.assertEqual(x.get_power_state(), False)


        x = Device(7)

        x.turn_on()

        x.turn_off()

        self.assertEqual(x.get_power_state(), False)

  def test_battery(self):
        x = Device(50)

        x.turn_on()

        self.assertEqual(x.get_battery(), 50)


        x = Device(50)

        x.turn_on()

        self.assertEqual(x.get_battery(), 50)

  def test_create_phone(self):

        y = Phone(50, "01234567898")

        self.assertEqual(y.get_power_state(), False)

        y.turn_on()

        self.assertEqual(y.get_power_state(), True)

        self.assertEqual(y.get_battery(), 50)


        y = Phone(50, "01234567898")

        self.assertEqual(y.get_power_state(), False)

        y.turn_on()

        self.assertEqual(y.get_power_state(), True)

        self.assertEqual(y.get_battery(), 50)


  def test_create_computer(self):
        z = Computer(100)

        y = Phone(100, "01234567898")

        self.assertEqual(z.get_battery(), y.get_battery())

        try:

          z.set_phone_number("01234567898")

          return False

        except Exception as e:

          pass


        z = Computer(100)

        y = Phone(100, "01234567898")

        self.assertEqual(z.get_battery(), y.get_battery())

        try:

          z.set_phone_number("01234567898")

          return False

        except Exception as e:

          pass


  def test_phone_number_error(self):
        try:

          y = Phone(2, "999")

        except InvalidPhoneNumber:

          print("Invalid phone number!")


        try:

          y = Phone(2, "999")

        except InvalidPhoneNumber:

          print("Invalid phone number!")

if __name__ == '__main__':
  unittest.main()