# okay less go

bidders = {}
bidAdd = []
nameAdd = []
def Bid():
    name = input("What is your name?\n")
    bid = input("how much your bid?\n")
    bidAdd.append(bid)
    nameAdd.append(name)
    for i in bidAdd:
        for j in nameAdd:
            bidders[j] = i
    cheeck_status = input("Do you want add new participant?\n")
    print("type yes or no.")

    if cheeck_status == "yes":
        Bid()

    elif cheeck_status == "no":
        #first check
        Winner = max(bidders.values())

        for key, value in bidders.items():
            if value == Winner:
                print(f"Winner {key} witch {Winner}$")
                break

    else :
        print("Type yes or no.")

Bid()