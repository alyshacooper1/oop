import CellphoneClass as c
# Creating an instance of CellPhone
def main():
   man = input('Enter manufacture:')
   mod = input('Enter the model number: ')
   retail = input('Enter the retail price;')

   apple = c.CellPhone(man,mod, retail)

   print(f"the original price is {apple.get_retail_price()}")

   new_price = 1200

   apple.set_retail_price(new_price)

   print('Manufacture: ', apple.get_manufact())
   print('Model Number: ', apple.get_model())
   print(f'Updated Retail price: {apple.get_retail_price()}')

main()