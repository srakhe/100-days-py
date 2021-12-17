import price_tracker

while True:
    choice = input('Enter your choice:\n1. Track all products.\n2. Add new product.\nEnter "exit" to stop.\n\n')
    if choice == '1':
        price_tracker.track()
    elif choice == '2':
        price_tracker.add_new()
    elif choice == 'exit':
        break
    else:
        print('Incorrect choice.')
    print('***********************************************************************************************************')
