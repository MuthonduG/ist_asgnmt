def shopping_branch_sales():
    # Define branches kori a 
    super_markets = ["KORI A", "KORI B", "KORI C", "KORI D", "KORI E"]
    {"brach_sales":[]}
    try:
        num_item = int(input("Enter estimated number of items: \n"))
        grand_total = 0
        kori_a, kori_b, kori_c, kori_d, kori_e = [], [], [], [], []

        # Get user inputs
        for i in range(num_item):
            market_branch = input("Enter market branch: \n")
            item_code = int(input("Enter item code: \n"))
            unit_price = float(input("Enter unit price: \n"))
            item_qty = int(input("Enter item qty: \n"))
            
            # check if branch exists
            if market_branch in super_markets:
                total = unit_price * item_qty
                grand_total += total

                if market_branch.lower() == "KORI A".lower():
                    kori = total
                    kori_a.append(kori)
                elif market_branch.lower() == "KORI B".lower():
                    kori = total
                    kori_b.append(kori)
                elif market_branch.lower() == "KORI C".lower():
                    kori = total
                    kori_c.append(kori)
                elif market_branch.lower() == "KORI D".lower():
                    kori = total
                    kori_d.append(kori)
                else:
                    kori = total
                    kori_e.append(kori)
                     
                
            else:
                print("Supermarkrt branch does not exist!!!")
                break;
            
        print(f"Grand Total for Kori Supermarkets is {grand_total}")
        print(f"Kori A total is {kori_a}")

    except ValueError:
        print("Number of items must be an integer!!!") 

shopping_branch_sales()