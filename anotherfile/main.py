class _Course:   #_ makes class private
    
    def __init__(self, Names):
        
        #Shop1 Information
        self.shop1 = "Default"
        self.location_shop1 = "Default"
        self.sales_shop1 = 0
        self.stock_shop1 = 0
        self.customer_shop1 = 0
        self.return_shop1 = 0
        
        #Shop 2 Information
        self.shop2 = "Default"
        self.location_shop2 = "Default"
        self.sales_shop2 = 0
        self.customer_shop2 = 0
        self.stock_shop2 = 0
        self.return_shop2 = 0
        
        #Shop 3 Information
        self.shop3 = "Default"
        self.location_shop3 = "Default"
        self.sales_shop3 = 0
        self.customer_shop3 = 0
        self.stock_shop3 = 0
        self.return_shop3 = 0
        
        #Shop 4 Information
        self.shop4 = "Default"
        self.location_shop4 = "Default"
        self.sales_shop4 = 0
        self.customer_shop4 = 0
        self.stock_shop4 = 0
        self.return_shop4 = 0
        
        
#Print menue Function: This function Displays all options needed for the first Menu
    def print_Menu(self):
        print("")
        print("Welcome")
        print("-----------------")
        print("1. Shop Management")
        print("2. Sales")
        print("3. Returns")
        print("4. Stock")
        print("99. Exit")
        print("-----------------")
        
#Shop Management Menu Function: Displays all options in the sales Management Menu    
    def print_ShopManagement(self):
        print("-----------------")
        print("1. Change Shop Names")
        print("2. Change Shop Locations")
        print("3. Display All Current Shops")
        print("4. Display All Shop Information")
        print("5. Back")
        print("-----------------")
        
        
#Disaplys Current Shops
    def display_Shops(self):
        print(f"1. {self.shop1}")
        print(f"2. {self.shop2}")
        print(f"3. {self.shop3}")
        print(f"4. {self.shop4}")
        
    def display_all_info(self):
        print(f"1. {self.shop1}, {self.location_shop1}, {self.sales_shop1}, {self.stock_shop1}, {self.customer_shop1}")
        print(f"2. {self.shop2}, {self.location_shop2}, {self.sales_shop2}, {self.stock_shop2}, {self.customer_shop2}")
        print(f"3. {self.shop3}, {self.location_shop3}, {self.sales_shop3}, {self.stock_shop3}, {self.customer_shop3}")
        print(f"4. {self.shop4}, {self.location_shop4}, {self.sales_shop4}, {self.stock_shop4}, {self.customer_shop4}")
       
            
#Change Shop Names Function Selects a shop and allows a user to change the name        
    def name_change(self):
        option_User = input("Please Select a number to change: ")
        if option_User == '1':
         option_User = input("Change the name: ")
         self.shop1 = option_User
         print(f"You have successfully Changed the shop name to {self.shop1}")
         
         
        elif option_User == '2':
         option_User = input("Change the name: ")
         self.shop2 = option_User
         print(f"You have successfully Changed the shop name to {self.shop2}")
         
        elif option_User == '3':
         option_User = input("Change the name: ")
         self.shop3 = option_User
         print(f"You have successfully Changed the shop name to {self.shop3}")
         
        elif option_User == '4':
         option_User = input("Change the name: ")
         self.shop4 = option_User
         print(f"You have successfully Changed the shop name to {self.shop4}")
         
        
#Change Location Name Function Selects a shop with its location and allows a user to change it
    def location_change(self):
        print(f"1. {self.shop1}, {self.location_shop1}")
        print(f"2. {self.shop2}, {self.location_shop2}")
        print(f"3. {self.shop3}, {self.location_shop3}")
        print(f"4. {self.shop4}, {self.location_shop4}")
        user_input = input("Please Select a Location:")
        if user_input == '1':
            user_change = input("Please change the name:")
            self.location_shop1 = user_change
            print(f"you have successfuly changed your location to {self.location_shop1}")
            
        elif user_input == '2':
            user_change = input("Please change the name:")
            self.location_shop2 = user_change
            print(f"you have successfuly changed your location to {self.location_shop2}")
        
        elif user_input == '3':
            user_change = input("Please change the name:")
            self.location_shop3 = user_change
            print(f"you have successfuly changed your location to {self.location_shop3}")
            
        elif user_input == '4':
            user_change = input("Please change the name:")
            self.location_shop4 = user_change
            print(f"you have successfuly changed your location to {self.location_shop4}")
            
#Sales Function takes amount bought and sales increases by amount bought
    def dislay_sales(self):
        print(f"1. {self.shop1}, {self.stock_shop1}")
        print(f"2. {self.shop2}, {self.stock_shop2}")
        print(f"3. {self.shop3}, {self.stock_shop3}")
        print(f"4. {self.shop4}, {self.stock_shop4}") 
        
        user_input = input("Please Select a store:")
        if user_input == '1':
            user_amount = int(input("How much do you want to buy:"))
            new_amount = self.stock_shop1 - user_amount 
            self.stock_shop1 = new_amount
            print(f"you have successfuly bought {user_amount} items")
            self.customer_shop1 = self.customer_shop1 +1
            
        elif user_input == '2':
            user_amount = int(input("How much do you want to buy:"))
            new_amount = self.stock_shop2 - user_amount
            self.stock_shop2 = new_amount
            print(f"you have successfuly bought {user_amount} items")
            self.customer_shop2 = self.customer_shop2 +1
            
        elif user_input == '3':
            user_amount = int(input("How much do you want to buy:"))
            new_amount = self.stock_shop3 - user_amount 
            self.stock_shop3 = new_amount
            print(f"you have successfuly bought {user_amount} items")
            self.customer_shop3 = self.customer_shop3 +1
            
        elif user_input == '4':
            user_amount = int(input("How much do you want to buy:"))
            new_amount = self.stock_shop4 - user_amount 
            self.stock_shop4 = new_amount
            print(f"you have successfuly bought {user_amount} items")
            self.customer_shop4 = self.customer_shop4 +1
        else:
            print("Invalid Syntax please Type a number")
        
#stock Function when items are bought stock will be decreased by amount
    def display_stock(self):
        print(f"1. {self.shop1}, {self.stock_shop1}")
        print(f"2. {self.shop2}, {self.stock_shop2}")
        print(f"3. {self.shop3}, {self.stock_shop3}")
        print(f"4. {self.shop4}, {self.stock_shop4}") 
            
#Return function that will select the store and return the amount      
    def user_return(self):
        print(f"1. {self.shop1}, {self.location_shop1}, {self.stock_shop1}")
        print(f"2. {self.shop2}, {self.location_shop2}, {self.stock_shop2}")
        print(f"3. {self.shop3}, {self.location_shop3}, {self.stock_shop3}")
        print(f"4. {self.shop4}, {self.location_shop4}, {self.stock_shop4}")
        user_input = input("Please Select a shop")
        
        if user_input == '1':
            print(f"1. {self.shop1}, {self.location_shop1}, {self.stock_shop1}")
            users_return = int(input("How much are you returning:"))
            self.stock_shop1 = users_return + self.stock_shop1
            print(f"You have returned {self.stock_shop1}")
            
        elif user_input == '2':
            print(f"1. {self.shop2}, {self.location_shop2}, {self.stock_shop2}")
            users_return = int(input("How much are you returning:"))
            self.stock_shop2 = users_return + self.stock_shop2
            print(f"You have returned {self.stock_shop2}")
            
        elif user_input == '3':
            print(f"1. {self.shop3}, {self.location_shop3}, {self.stock_shop3}")
            users_return = int(input("How much are you returning:"))
            self.stock_shop3 = users_return + self.stock_shop3
            print(f"You have returned {self.stock_shop3}")
            
        elif user_input == '4':
            print(f"1. {self.shop4}, {self.location_shop4}, {self.stock_shop4}")
            users_return = int(input("How much are you returning:"))
            self.stock_shop4 = users_return + self.stock_shop4
            print(f"You have returned {self.stock_shop4}")