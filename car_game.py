choice = ""
started = False
while True:
    choice = input('> ').lower()
    if choice == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
''')
    elif choice == 'start':
        if started:
            print('The car already started!')
        else:
            started = True
            print("Car started...")
    elif choice == 'stop':
        if not started:
            print('The car already stopped!')
        else:
            started = False
            print("Car stopped")
    elif choice == 'quit':
        break
    else:
        print("Sorry!, I don't understand that...")
