import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)
base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 3.84.16.92 -p 11000")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 3.84.16.92 -p 11000")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print("printString:", rep)
rep = printer2.printString("Hello World from printer2!")
print("printString:", rep)

count = printer1.countWords("Hello World from ICE middleware")
print("countWords printer1:", count)
count = printer2.countWords("Sistemas Distribuidos UFG")
print("countWords printer2:", count)

rev = printer1.reverseString("Sistemas Distribuidos")
print("reverseString printer1:", rev)
rev = printer2.reverseString("Hello World")
print("reverseString printer2:", rev)

communicator.waitForShutdown()
