import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)
base = communicator.stringToProxy("SimplePrinter:tcp -h 3.84.16.92 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

rep = printer.printString("Hello World!")
print("printString:", rep)

count = printer.countWords("Hello World from ICE middleware")
print("countWords:", count)

rev = printer.reverseString("Sistemas Distribuidos")
print("reverseString:", rev)
