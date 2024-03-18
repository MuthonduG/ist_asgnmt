def shopping_branch_sales():
    super_markets = ["KORI A", "KORI B", "KORI C", "KORI D", "KORI E"]
    branch_sales = []

    try:
        num_item = int(input("Enter estimated number of items: \n"))
        grand_total = 0
        kori_a, kori_b, kori_c, kori_d, kori_e = [0, 0, 0, 0, 0]

        # Get user inputs
        for i in range(num_item):
            market_branch = input("Enter market branch: \n")
            
            # check if branch exists
            if market_branch.upper() in super_markets:
                item_code = int(input("Enter item code: \n"))
                unit_price = float(input("Enter unit price: \n"))
                item_qty = int(input("Enter item qty: \n"))
                
                total = unit_price * item_qty
                grand_total += total

                if market_branch.upper() == "KORI A":
                    kori_a += total
                elif market_branch.upper() == "KORI B":
                    kori_b += total
                elif market_branch.upper() == "KORI C":
                    kori_c += total
                elif market_branch.upper() == "KORI D":
                    kori_d += total
                else:
                    kori_e += total
            else:
                if market_branch.upper() == "DONE":
                    break;
                else:
                    print("Supermarket branch does not exist!!!")
                    break;
            
        # Append branch sales to list of dictionaries
        branch_sales.append({"KORI A": kori_a})
        branch_sales.append({"KORI B": kori_b})
        branch_sales.append({"KORI C": kori_c})
        branch_sales.append({"KORI D": kori_d})
        branch_sales.append({"KORI E": kori_e})
        
        print(f"Grand Total for Kori Supermarkets is {grand_total}")
        print(f"Branch Sales: {branch_sales}")
        # for branch in branch_sales:
        #     print(branch)

    except ValueError:
        print("Number of items must be an integer!!!")

shopping_branch_sales()
