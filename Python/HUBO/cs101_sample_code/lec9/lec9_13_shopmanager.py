
stock_file_name = "data/stock.txt"

def load_stock(filename):
  stock = []
  f = open(filename, "r")
  for line in f:
    no, item, price = line.strip().split(",")
    stock.append((int(no), item, int(price)))
  f.close()
  return stock

def show_menu():
  print "What would you like to do:"
  print " S) Sell item"
  print " P) Print stock"
  print " R) Report sales"
  print " E) Exit"
  cmd = raw_input("Enter your choice> ")
  return cmd.strip().lower()

def sell(stock, sales):
  """ Selling items """
  print "Sell routine is called"
  
def print_stock(stock):
  """ Print items , price, amount """
  print "Print stock is called"
  
def print_sales(sales):
  """ Sale history today """
  print "Print sales is called "
  
def main():
  stock = load_stock(stock_file_name)
  sales = []
  while True:
    s = show_menu()
    if s == 'e':
      break
    elif s == 's':
      sell(stock, sales)
    elif s == 'p':
      print_stock(stock)
    elif s == 'r':
      print_sales(sales)          
    else:
      print "Don't know command %s!" % s

main()
