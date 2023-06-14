from web3 import Web3
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)


# Write Import API url
url = 'https://mainnet.infura.io/v3/7a1985edf2e743bfa6b00d5abc7ef539'
# write code to Store the url in variable
web3 = Web3(Web3.HTTPProvider(url))

def ethereum_block():
    number = int(block_entry.get())
    block_data = web3.eth.get_block(number)
    transaction = web3.eth.get_transaction(block_data['transactions'][-1].hex())
    value = transaction['value']

    value_in_ether = value / (10 ** 18)
    dollars = value_in_ether*1746.10
    gas = transaction['gas']

    gasused_info_label["text"] = "Value: $" + str(dollars)
    gaslimit_info_label["text"] = "gas: " + str(gas)
    block_name_label["text"] = block_entry.get()


# Write Code for Task 02 below.






    block_entry.destroy()
    search_btn.destroy()


search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()
