from main import _Course
TU225 = _Course("TU225")

runApp_bool = True #close app if False
while runApp_bool:
    TU225.print_Menu()
    option = input("Please Choose an Option:")
    if option == '1': #Shop Management
            TU225.print_ShopManagement()
            user_Option1 = input("Please Choose an option:")
            if user_Option1 == '1':
                TU225.display_Shops()
                TU225.name_change()
                
            elif user_Option1 == '2':
                TU225.location_change()
                
            elif user_Option1 == '3':
                TU225.display_Shops()
            
            elif user_Option1 == '4':
                TU225.display_all_info()
                
            elif user_Option1 == '5':
                TU225.print_Menu()
                
            
    elif option == '2':  #Sales Option
         TU225.dislay_sales()
         
    elif option == '3': #Returns Option
       TU225.user_return()
        
    elif option == '4': #Stock Option
        TU225.display_stock()
        
    elif option == '99': # exits the loop to end program
        runApp_bool = False
    
    else:
        print("Invalid option, please retry")