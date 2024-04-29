import random

class WordList:
    def __init__(self):
        self.celebrities = [
        "Taylor Swift", "Beyoncé", "Drake", "Adele", "Ed Sheeran", "Justin Bieber", 
        "Rihanna", "Kanye West", "Lady Gaga", "Billie Eilish", "Bruno Mars", "Ariana Grande", 
        "The Weeknd", "Jay-Z", "Katy Perry", "Dua Lipa", "Harry Styles", "Shakira", 
        "Coldplay", "Travis Scott", "Eminem", "Kendrick Lamar", "Maroon 5", "Nicki Minaj", 
        "Selena Gomez", "Snoop Dogg", "Post Malone", "Jennifer Lopez", "Miley Cyrus", 
        "John Legend", "Usher", "Lizzo", "Cardi B", "Sam Smith", "Pink", "Chris Brown", 
        "Lana Del Rey", "Camila Cabello", "Demi Lovato", "Halsey", "Marshmello", "Doja Cat", 
        "Calvin Harris", "Ellie Goulding", "Charlie Puth", "Pitbull", "50 Cent", "Lil Nas X", 
        "Megan Thee Stallion", "The Chainsmokers", "Alicia Keys", "Bruce Springsteen", "Britney Spears", 
        "Elton John", "Madonna", "David Bowie", "Paul McCartney", "Michael Jackson", "Prince", 
        "Whitney Houston", "Janet Jackson", "Stevie Wonder", "Celine Dion", "Shania Twain"
    ]
        self.foods = [
        "Pizza", "Burger", "Sushi", "Pasta", "Ice Cream", "Tacos", "Salad", "Steak", 
        "Chicken curry", "Fried rice", "Doughnut", "Chocolate", "Sandwich", "Bagel", 
        "Falafel", "Pancakes", "Dumplings", "Lasagna", "Hummus", "Ribs", 
        "Cheesecake", "Fish and chips", "Paella", "Samosa", "Croissant", "Nachos", 
        "Ramen", "Hot dog", "Pho", "Apple pie", "Macaroni and Cheese", "Tiramisu", 
        "Poutine", "Burrito", "Jollof rice", "Jambalaya", "Lobster", "Escargot", 
        "Currywurst", "Baklava", "Gumbo", "Borscht", "Udon", "Cannoli", "Jerk Chicken", 
        "Kimchi", "Miso soup", "Empanada", "Bruschetta", "Quiche", "Omelette", 
        "Chicken Wings", "Pulled Pork", "Spring Rolls", "Fajitas", "Churros", 
        "Biryani", "Ratatouille", "Stir Fry", "Taco Salad", "Tempura", "Focaccia", 
        "Meatloaf", "Goulash", "Chicken Parmesan"
    ]
        self.athletes = [
        "LeBron James", "Tom Brady", "Lionel Messi", "Stephen Curry", "Cristiano Ronaldo", 
        "Kevin Durant", "Kylian Mbappe", "Patrick Mahomes", "Alexander Ovechkin", "Neymar", 
        "Sidney Crosby", "Giannis Antetokounmpo", "Virat Kohli", "Russell Wilson", "James Harden", 
        "Connor McDavid", "Drew Brees", "Luka Doncic", "Aaron Rodgers", "Mohamed Salah", 
        "Mike Trout", "Zlatan Ibrahimovic", "Kawhi Leonard", "Eli Manning", "Peyton Manning", 
        "Julio Jones", "Derek Jeter", "Floyd Mayweather", "Novak Djokovic", "Roger Federer", 
        "Luis Suarez", "Sergio Ramos", "David Beckham", "Zinedine Zidane", "Wayne Rooney", 
        "Clayton Kershaw", "Bryce Harper", "Manny Machado", "Jose Altuve", "Mookie Betts", 
        "Fernando Tatis Jr.", "Jacob deGrom", "Max Scherzer", "Vladimir Guerrero Jr.", "Ronald Acuna Jr.", 
        "Shohei Ohtani", "Giancarlo Stanton", "Aaron Judge", "Yadier Molina", "Gerrit Cole", 
        "Josh Donaldson", "Kris Bryant", "Javier Baez", "Freddie Freeman", "Christian Yelich", 
        "Nikita Kucherov", "Evgeni Malkin", "Patrick Kane", "Jonathan Toews", "Anze Kopitar", 
        "Steven Stamkos", "Henrik Lundqvist", "Carey Price", "Brad Marchand", "Joe Thornton"
    ]
        
    def returnRandomWord(self, category: str) -> str:
        """
        Returns a random word from a specified category.
        :param category: A string specifying the category ('celebrities', 'foods', or 'athletes')
        :return: A random word from the specified list.
        """
        if category == 'celebrities':
            return random.choice(self.celebrities)
        elif category == 'foods':
            return random.choice(self.foods)
        elif category == 'athletes':
            return random.choice(self.athletes)
        else:
            return "Category not found"
        

            





