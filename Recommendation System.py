import pandas as pd

# Book dataset
books = {
    "Book": [
        # Self-Help
        "The Alchemist",
        "Atomic Habits",
        "Rich Dad Poor Dad",
        "Think and Grow Rich",
        "The Psychology of Money",
        "Deep Work",
        "The 7 Habits of Highly Effective People",

        # Fantasy
        "Harry Potter",
        "Percy Jackson",
        "The Hobbit",
        "The Lord of the Rings",
        "The Chronicles of Narnia",
        "Eragon",
        "The Name of the Wind",

        # Thriller
        "The Silent Patient",
        "Gone Girl",
        "The Girl on the Train",
        "Sherlock Holmes",
        "Da Vinci Code",
        "Angels and Demons",
        "The Woman in the Window",

        # Science Fiction
        "Dune",
        "Foundation",
        "Ender's Game",
        "Neuromancer",
        "The Martian",
        "Ready Player One",
        "Project Hail Mary",

        # Romance
        "Pride and Prejudice",
        "Me Before You",
        "The Notebook",
        "It Ends With Us",
        "Twilight",
        "The Fault in Our Stars",
        "Love Story"
    ],

    "Genre": [
        # Self-Help
        "Self-Help",
        "Self-Help",
        "Self-Help",
        "Self-Help",
        "Self-Help",
        "Self-Help",
        "Self-Help",

        # Fantasy
        "Fantasy",
        "Fantasy",
        "Fantasy",
        "Fantasy",
        "Fantasy",
        "Fantasy",
        "Fantasy",

        # Thriller
        "Thriller",
        "Thriller",
        "Thriller",
        "Thriller",
        "Thriller",
        "Thriller",
        "Thriller",

        # Science Fiction
        "Science Fiction",
        "Science Fiction",
        "Science Fiction",
        "Science Fiction",
        "Science Fiction",
        "Science Fiction",
        "Science Fiction",

        # Romance
        "Romance",
        "Romance",
        "Romance",
        "Romance",
        "Romance",
        "Romance",
        "Romance"
    ]
}

# Create DataFrame
df = pd.DataFrame(books)

print("=" * 60)
print("        📚 AI-BASED BOOK RECOMMENDATION SYSTEM")
print("=" * 60)

while True:

    print("\nAvailable Books:")
    for book in df["Book"]:
        print("•", book)

    book_name = input("\nEnter a book you like (or type 'exit'): ").strip()

    if book_name.lower() == "exit":
        print("\nThank you for using the Book Recommendation System!")
        break

    # Search book ignoring case
    match = df[df["Book"].str.lower() == book_name.lower()]

    if not match.empty:

        genre = match.iloc[0]["Genre"]

        recommendations = df[
            (df["Genre"] == genre) &
            (df["Book"].str.lower() != book_name.lower())
        ]["Book"]

        print(f"\n📖 Because you liked '{match.iloc[0]['Book']}',")
        print("you may also enjoy:\n")

        for book in recommendations:
            print("📚", book)

    else:
        print("\n❌ Book not found in database.")
        print("Please choose a book from the available list.")
