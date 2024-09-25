"""
week 7 lab 3
author Bipin

"""
class RequestSystem:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.age = input("Please enter your age: ")
        self.email = input("Please enter your email: ")
        self.uniqueid = 200
        self.products = []
        self.total = 0
        self.approved_request = 100
        self.pending_request = 50
        self.notapproved_request = 50
        self.requests = []  
    def userinfo(self):
        self.uniqueid += 1  
    def request_details(self):
        self.products = []  
        self.total = 0      
        while True:
            item = input("Enter the item (Enter 'exit' when finished): ")
            if item.lower() == 'exit':
                break
            price = float(input("Enter the price of the item: "))
            self.products.append((item, price))  
            self.total += price

        self.referenceid = self.name[-3:] + str(self.uniqueid)[-3:]  
        self.userinfo() 
        return self.total, self.products, self.referenceid

    def request_approval(self):
        if self.total < 150:
            self.status = "Approved"
            self.approved_request += 1
            
        else:
            self.status = "Pending"
            self.pending_request += 1
        print(F"Total:{self.total}")
        print(f"Request Status: {self.status}")


        
        request = {
            "name": self.name,
            "total": self.total,
            "referenceid": self.referenceid,
            "status": self.status,
            "products": self.products
        }
        self.requests.append(request)  

    def respond_request(self, manager_respond):
        if manager_respond.lower() == "approved":
            self.status = "Approved"
        else:
            self.status = "Not Approved"
        return self.status

    def display_requests(self):
        if not self.requests:
            print("No requests have been submitted yet.")
        else:
            print("-" * 30)
            print("       All Requests      ")
            print("-" * 30)
            for req in self.requests:
                print(f"Name: {req['name']}, Total: ${req['total']}, "
                      f"Approval reference: {req['referenceid']}, Status: {req['status']}")
            print("-" * 30)

    def statistics(self):
        print(f"Approved Requests: {self.approved_request}")
        print(f"Pending Requests: {self.pending_request}")
        print(f"Not Approved Requests: {self.notapproved_request}")



def main():
    system = RequestSystem()

    while True:
        choice = input("\n1. Submit Request\n2. Display Requests\n3. View Statistics\n4. Exit\nChoose an option: ")
        if choice == "1":
            system.request_details()
            system.request_approval()
        elif choice == "2":
            system.display_requests()
        elif choice == "3":
            system.statistics()
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

