import hashlib
import random
import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (key TEXT PRIMARY KEY, value REAL)''')
#devnet = {}
#testnet = {}
#mainnet = {}
#def func(*args, **kwargs):
#  w1 = create_wallet(devnet)
#  create_sqlwallet(w1)
#  w2 = create_wallet(devnet)
#  create_sqlwallet(w2)
#  Element('wallet1').element.innerHTML = w1
#  Element('wallet2').element.innerHTML = w2
    
#  def func2(*args, **kwargs):
#    address = Element('balance').element.value
#    balanc1 = balance(devnet, address)
#    Element('wallet1').element.innerHTML = balanc1
#    balanc2 = balancesql(address)
#    Element('wallet2').element.innerHTML = balanc2
#  def main(*args, **kwargs):
#    sender = Element('sender').element.value
#    receiver = Element('receiver').element.value
#    amount = Element('amount').element.value
#    transaction(devnet, sender, receiver, amount)
 #   #Element('output1').element.innerHTML = text1
  #def transaction(network, send_address, receive_address, amount):
  #  val = float(amount)
  #  if(network[send_address] >= val and val >= 0.01):
  #    network[send_address] -= val
 #     network[receive_address] += val
 #   elif(network[send_address] < val or val < 0.01):
#      print("transaction can't be done -> low balance")
#    else:
#      print("transaction error")

##  def balance(network, address):
##    if(address in network):
##      return network[address]
##    else:
##      var = 0.00
##      return var

  def balancesql(address):
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT value FROM mytable WHERE key=?", (address,))
        result = cursor.fetchone()
        if result:
                return result[0]
        else:
                return 0
        conn.close()

      
##  def create_wallet(network):
##    address = generate_hash()
##    network[address] = 0.75
##    return address
##
  def create_sqlwallet(address):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mytable (key, value) VALUES (?, ?)", (address, 0.25))
    conn.commit()
    conn.close()

      
  def generate_hash():
    string_random = ""
    for i in range(100):
      random_number = random.uniform(1e-14, 1e14)
      str_random = str(random_number)
      string_random += str_random
    data = string_random.encode("utf-8")
    hash_object = hashlib.sha256()
    hash_object.update(data)
    hash = hash_object.hexdigest()
    return hash

  conn.close()
