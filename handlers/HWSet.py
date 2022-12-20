# Name: Jan C. Rubio
# UT EID: jcr4698

class HWSet():

    """ Constructor of HWSet class. QTY is the initial
        capacity and availability of units in storage. """
    def __init__(self, qty = 0):
        
        # valid input
        if(self.__valid_input(qty)):
            # Set maximum capacity in storage to initial value (QTY)
            self._capacity = qty
            # Set units available to the maximum capacity
            self._availability = self._capacity

        # invalid input
        else:
            # Set capacity and availability to zero
            self._capacity = 0
            self._availability = 0
            # display error message
            print("INVALID \"qty\" capacity value: No storage available")

    ## Accessors:

    """ Output the availability of units in storage. """
    def get_availability(self):
        # Get current units available
        return self._availability

    """ Output the maximum capacity of units in storage. """
    def get_capacity(self):
        # Get current maximum capacity
        return self._capacity

    """ Output the amount of units that have been
        checked-out in storage. """
    def get_checkedout_qty(self):
        # Calculate units checked-out
        return self._capacity - self._availability

    ## Modifiers:

    """ If there are enough units in storage, subtract
        the QTY amount from storage and return 0.
        Otherwise, subtract the units available and
        return -1. """
    def check_out(self, qty = 0):
        # Verify if QTY is a valid input
        if(not self.__valid_input(qty)):
            print("INVALID \"qty\" Checked-out value: No units subtracted to storage")
            return -1
        # Verify there are enough units to subtract
        if(self._availability - qty >= 0):
            # Subtract QTY from storage
            self._availability -= qty
            # Notify successful transaction
            return 0
        # otherwise, subtract all available units
        self._availability = 0
        # Notify incomplete transaction
        return -1

    """ If capacity isn't exceeded by units checked-in, add back
        the QTY amount of units into storage. Otherwise, add the
        units that restore storage to maximum capacity."""
    def check_in(self, qty = 0):
        # Verify if QTY is a valid input
        if(not self.__valid_input(qty)):
            print("INVALID \"qty\" checked-in: No units added to storage")
            return -1
        # Verify there is enough capacity to add
        if(self._availability + qty <= self._capacity):
            # Add QTY to storage
            self._availability += qty
            # Notify successful transaction
            return 0
        # Otherwise, add all remaining units
        self._availability = self._capacity
        # Notify incomplete transaction
        return -1

    ## Helper methods:

    """ Determine whether value is of type 'int'. """
    def __valid_input(self, qty):
        return str(type(qty)) == "<class \'int\'>"
