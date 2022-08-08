nominee_1 = "Afrah"
nominee_2 = "Abdikadir"

print(f"Nominee 1: {nominee_1} \nNominee 2: {nominee_2}")

nom_1_votes = 0
nom_2_votes = 0

voters_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Number of voters that are going to participate the voting process
num_of_voters = len(voters_id)

while True:
    voter = int(input("\nEnter your voter ID number: "))
    # checking if voter ID is in voters_id
    if voter in voters_id:
        vote = int(input("Enter your vote either 1 for nominee one or 2 for nominee two: "))
        if vote != 1 and vote != 2:
            print("You have entered a wrong voting number, please enter either 1 for nominee one or 2 for nominee two.")
        else:
            if vote == 1:
                nom_1_votes += 1
            elif vote == 2:
                nom_2_votes += 1
            # Thanking after each voter casts their vote
            print("Thank you for casting your vote.")
        # Removing the voter ID after they vote
        voters_id.remove(voter)
    else:
        # if the voter enters the wrong voter_id or repeats voter_id that has been used
        print("You're not a voter or you've already voted")

    # Checking if the voting session is over
    if not voters_id:  # it can also be written as if voters_id == []
        print("\nThe voting session is over.")
        # calculating the number of votes
        if nom_1_votes > nom_2_votes:
            percentage = (nom_1_votes / num_of_voters) * 100
            print(f"{nominee_1} has won with {percentage}% of the votes.")

        elif nom_2_votes > nom_1_votes:
            percentage = (nom_2_votes / num_of_voters) * 100
            print(f"{nominee_2} has won with {percentage}% of the votes.")
        else:
            print("The nominees have the same number of votes.")
        break
