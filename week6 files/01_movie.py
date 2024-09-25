"""
week 6 lab 3
Question: phython program to create a movie rental system ussing python OOP
Author Charanpreet singh
"""
class Movie:
    def __init__(self,title,gener,year):
        self.title=title
        self.gener=gener
        self.year=year
        self.avabliable=True
    def mark_as_rented(self):
        self.avabliable=False
    def mark_as_avabliable(self):
        self.avabliable=True
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.gener} - {' Avaliable ' if self.avabliable else 'Rented'}"

class Customer:
    def __init__ (self, name):
        self.name=name
        self.rented_movies=[]
    def rent_movie(self,movie):
        if movie.avaliable:
            movie.mark_as_rented()
            self.rented_movies.append(movie)
            print (f"{self.name} Rented {movie.title}")
        else:
            print (f"{movie.title} is not avabliable")
    def return_movie(self,movie):
        if movie in self.rented_movies:
            movie.mark_as_avabliable()
            self.rented_movies.remove(movie)
            print(f"{self.name} returned {movie.title}")
        else:
            print(f"{self.name} did not rent {movie.title}")
    def list_rent_movies(self):
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies:")
            for movie in self.rented_movies:
                print(movie)
        else:
            print(f"{self.name} has no rented movies.")
class RentalStore:  
    def __init__(self):  
        self.movies = []  
    def add_movie(self, movie): 
         self.movies.append(movie)  
    def list_movies(self): 
        if self.movies:  
            print("Available Movies:") 
            for movie in self.movies: 
                print(movie)  
        else: 
            print("No movies available.")  
    def find_movie(self, title): 
        for movie in self.movies: 
            if movie.title.lower() == title.lower():  
                return movie 
        return None  
def menu(): 
    print("InMovie Rental System Menu")
    print("1. List Available Movies") 
    print("2. Rent a Movie") 
    print("3. Return a Movie")  
    print("4. List Rented Movies") 
    print("5. Add a Movie to Store")
    print("6. Exit")  

def main():  
    # Initialize the store and movies 
    store = RentalStore() 
    store.add_movie(Movie("Inception","Sci-Fi", 2010)) 
    store.add_movie(Movie("The Matrix", "Action", 1999))  
    store.add_movie(Movie("The Godfather", "Crime", 1972))  

    # Initialize customers  
    customers = {
        "Alice": Customer("Alice"), 
        "Bob": Customer("Bob")
    }

    while True:  
        menu()  
        choice = input("Enter your choice: ").strip()  

        if choice == "1":
            store.list_movies()
        elif choice == "2":
            customer_name = input("Enter your name: ").strip()
            movie_title = input("Enter movie title to rent: ").strip() 
            customer = customers.get(customer_name)  
            movie = store.find_movie(movie_title)
            if customer and movie: 
                customer.rent_movie(movie) 
            elif not customer:  
                print("Customer not found.")  
            elif not movie:
                print("Movie not found.")
            elif choice == "3":
                customer_name = input("Enter your name: ").strip() 
                movie_title = input("Enter movie title to return: ").strip() 
                customer = customers.get(customer_name)  
                movie = store.find_movie(movie_title) 
                if customer and movie:  
                    customer.return_movie(movie)  
                elif not customer: 
                    print("Customer not found.") 
                elif not movie: 
                    print("Movie not found.") 
        elif choice == "4": 
            customer_name = input("Enter your name: ").strip() 
            customer = customers.get(customer_name) 
            if customer: 
                customer.list_rented_movies()  
            else:  
                print("Customer not found.") 
        elif choice == "5":  
            title=input("Enter movie title: ").strip()  
            genre=input("Enter movie genre: ").strip()  
            year=int(input("Enter movie year: ").strip())  
            store.add_movie(Movie(title, genre, year))  
            print(f"Movie '{title}' added to the store.")  
        elif choice == "6":  
            print("Exiting...")  
            break  
        else:
            print("Invalid choice, please try again.")  
if __name__ == "__main__": 
    main() 
