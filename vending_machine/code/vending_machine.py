"""
Your task is to design a classic vending machine, using the template below.
Each row should be specified with a letter (A-Z) and each column should be
specified by a number (1-9). No valid vending machine can be created with more
than 26 rows or more than 9 columns. The maximum price of any vending machine
item is $2, the minimum price is $0.25. This vending machine accepts $1, 25¢,
10¢, and 5¢ denominations (as integers: 100, 25, 10, 5). No more than $2 of
funds can be added to the machine at any time. You can assume an unlimited
supply of change within the machine. A request to dispense from the vending
should result in success if conditions allow, but otherwise raise a
VendingError. Any error/invalid inputs inside the machine should raise a
VendingError. When setting up the vending machine, a price must be set for a
slot before items are loaded. A maximum of 50 items can be added per slot.

Some additional notes:
- Row inputs should be case insensitive.
- Change should be returned in the fewest possible number of coins (no bills).
- Please do not alter the return types or method signatures.
- Note any assumptions in comments; use your real-world experience to inform
  those assumptions.


EXAMPLE USAGE:

my_machine = VendingMachine(6, 5)

# This vending machine will have 30 slots specified with a letter and a number:
# A1 A2 A3 A4 A5
# B1 B2 B3 B4 B5
# C1 C2 C3 C4 C5
# D1 D2 D3 D4 D5
# E1 E2 E3 E4 E5
# F1 F2 F3 F4 F5

for i in 'ABCDEF':
    for j in range(1, 6):
        my_machine.set_price(i, j, 100)
        my_machine.load_slot(i, j, 5)

my_machine.accept_payment(100)  # dollar
change = my_machine.dispense('A', 4)
"""

from typing import Tuple


class VendingError(Exception):
    pass


class VendingMachine:

    def __init__(self, nrows: int, ncols: int):
        pass

    def set_price(self, row: str, col: int, price: int):
        """
        Set the price for items in the specified slot.  Price is in integer
        number of cents ($1 = 100).
        """
        pass

    def get_price(self, row: str, col: int) -> int:
        """
        Get the price that has been set for the specified slot or None if not
        set.
        """
        pass

    def load_slot(self, row: str, col: int, num_items: int):
        """
        Load `num_items` (number of items) into the specified slot.
        """
        pass

    def inventory_slot(self, row: str, col: int) -> int:
        """
        Return number of items currently in slot. 0 if none.
        """
        pass

    def accept_payment(self, denom: int):
        """
        Accept payment from user.  Can accept payment anytime after
        VendingMachine is initialized.
        """
        pass

    def check_funds(self) -> int:
        """
        Returns value of available funds for display.
        """
        pass

    def dispense(self, row: str, col: int) -> Tuple[int, int, int]:
        """
        User is attempting to dispense an item.  If conditions allow,
        dispense is successful, otherwise raise a VendingError.

        ::return Tuple[number of quarters, number of dimes, number of nickels]
        """
        pass

    def cancel(self) -> Tuple[int, int, int]:
        """
        Ends current transaction and returns change.

        ::return Tuple[number of quarters, number of dimes, number of nickels]
        """
        pass
