"""
Classic Vending Machine
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
