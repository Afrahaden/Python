def vote_reg():
    voters_id_list = []
    count = 0
    while True:
        voters_id = int(input("Enter your ID number: "))

        if voters_id in voters_id_list:
            print("\nThe ID you have entered is already registered.\n")
        else:
            voters_id_list.append(voters_id)
            count += 1
            print(f"\nA total of {count} voters are registered.")
            print(f"The registered voters are {voters_id_list} \n")

            if len(voters_id_list) == 5:  # you can increase the number of voter you want to register
                break


vote_reg()
