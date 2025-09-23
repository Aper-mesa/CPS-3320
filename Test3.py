def showTax(price = 10, taxRate = 0.07):
    tax = taxRate * price
    print("Tax: ", tax)

if __name__ == '__main__':
    showTax(10,0.2)