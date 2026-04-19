import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def countWords(self, s, current=None):
        count = len(s.split())
        print(f"countWords('{s}') = {count}")
        return count

    def reverseString(self, s, current=None):
        result = s[::-1]
        print(f"reverseString('{s}') = '{result}'")
        return result

communicator = Ice.initialize(sys.argv)
adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()
communicator.waitForShutdown()
