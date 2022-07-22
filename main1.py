from views import delete_product, list_of_products, retrieve_data, create_product, update_product
def main():
    print('privet tebe doctepny next funtion: \n\tLIST-1:\n\tRETRIEVE-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('vvedite deicstie(1,2,3,4,5):  ')
    if choice == '1':
        print(list_of_products())
    elif choice == '2':
        print(retrieve_data())
    elif choice == '3':
        print(create_product())
    elif choice == '4':
        print(update_product())
    elif choice == '5':
        print(delete_product())
    else:
        print('invalid choice!!')
        main()
    ask = input('hotite prodolzhit\?YES/NO')
    if ask.lower() == 'yes':
        main()
    else:
        print('poka! poka')
main()
