import json
from rich.console import Console
from rich.table import Table

from ItemClasses.book import Book
from ItemClasses.item import Item
from ItemClasses.magazine import Magazine
from ItemClasses.dvd import DVD
from databaseClass.database import Database

try:
    console = Console()
    db = Database()
    db.create_table("books")
    db.create_table("dvd")
    db.create_table("magazine")

    while True:
        console.print("[bold cyan]=== Menu ===[/bold cyan]")
        console.print("1. [green]Add an item[/green]")
        console.print("2. [red]Delete an item[/red]")
        console.print("3. [blue]View all (or one) item/s[/blue]")
        console.print("4. [yellow]Search for item/s[/yellow]")
        console.print("5. [white]Purshase item/s[/white]")
        console.print("6. [magenta]Exit[/magenta]")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            try:
                console.print("\n[bold cyan]Select an item type:[/bold cyan]")
                console.print("[green]1. Book[/green]")
                console.print("[yellow]2. DVD[/yellow]")
                console.print("[blue]3. Magazine[/blue]")

                item_type = input("\nEnter your choice: ")

                if item_type == "1":
                    title = input("Enter the title: ")
                    author = input("Enter the author: ")
                    price = float(input("Enter the price: "))
                    isbn = input("Enter the ISBN: ")
                    genre = input("Enter the genre: ")
                    num_pages = int(input("Enter the number of pages: "))
                    item = Book(title, author, price, isbn, genre, num_pages)
                    item.save_to_database(db, "books")
                    console.print("[bold green]Item saved successfully![/bold green]")
                elif item_type == "2":
                    title = input("Enter the title: ")
                    author = input("Enter the author: ")
                    price = float(input("Enter the price: "))
                    director = input("Enter the director: ")
                    duration = int(input("Enter the duration: "))
                    genre = input("Enter the genre: ")
                    item = DVD(title, author, price, director, duration, genre)
                    item.save_to_database(db, "dvd")
                    console.print("[bold green]Item saved successfully![/bold green]")
                elif item_type == "3":
                    title = input("Enter the title: ")
                    author = input("Enter the author: ")
                    price = float(input("Enter the price: "))
                    publisher = input("Enter the publisher: ")
                    issue = int(input("Enter the issue: "))
                    editor = input("Enter the editor: ")
                    item = Magazine(title, author, price, publisher, issue, editor)
                    item.save_to_database(db, "magazine")
                    console.print("[bold green]Item saved successfully![/bold green]")
                else:
                    console.print("[bold red]Invalid item type[/bold red]")
            except ValueError:
                console.print("[bold red]Invalid input. Please enter valid data.[/bold red]")
                continue

        elif choice == "2":
            try:
                console.print("\n[bold cyan]Select the item type:[/bold cyan]")
                console.print("[green]1. Book[/green]")
                console.print("[yellow]2. DVD[/yellow]")
                console.print("[blue]3. Magazine[/blue]")

                item_type = input("\nEnter your choice: ")

                if item_type == "1":
                    console.print("Select the item to delete:")
                    console.print("Keys:", db.keys("books"))
                    item_id = input("Enter the item ID: ")
                    if item_id not in db.keys("books"):
                        console.print("[bold red]Item not found![/bold red]")
                    else:
                        db.remove('books', item_id)
                        console.print("[bold green]Item deleted successfully![/bold green]")
                elif item_type == "2":
                    console.print("Select the item to delete:")
                    console.print("Keys:", db.keys("dvd"))
                    item_id = input("Enter the item ID: ")
                    if item_id not in db.keys("dvd"):
                        console.print("[bold red]Item not found![/bold red]")
                    else:
                        db.remove('dvd', item_id)
                        console.print("[bold green]Item deleted successfully![/bold green]")
                elif item_type == "3":
                    console.print("Select the item to delete:")
                    console.print("Keys:", db.keys("magazine"))
                    item_id = input("Enter the item ID: ")
                    if item_id not in db.keys("magazine"):
                        console.print("[bold red]Item not found![/bold red]")
                    else:
                        db.remove('magazine', item_id)
                        console.print("[bold green]Item deleted successfully![/bold green]")
                else:
                    console.print("[bold red]Invalid item type[/bold red]")
            except ValueError:
                console.print("[bold red]Invalid input. Please enter valid data.[/bold red]")
                continue

        elif choice == "3":
            try:
                console.print("\n[bold cyan]Select the item type:[/bold cyan]")
                console.print("[green]1. All item types[/green]")
                console.print("[yellow]2. Book[/yellow]")
                console.print("[blue]3. DVD[/blue]")
                console.print("[magenta]4. Magazine[/magenta]")

                item_type = input("\nEnter your choice: ")

                if item_type == "1":
                    console.print("[bold cyan]=== All Items ===[/bold cyan]")
                    table = Table(show_header=True, header_style="bold cyan")
                    table.add_column("ID", style="bold")
                    table.add_column("Type", style="bold")
                    table.add_column("Details", style="bold")
                    for key in db.keys("books"):
                       table.add_row(key, "Book", str(db.get("books", key)))
                    for key in db.keys("dvd"):
                        table.add_row(key, "DVD", str(db.get("dvd", key)))
                    for key in db.keys("magazine"):
                        table.add_row(key, "Magazine", str(db.get("magazine", key)))
                    console.print(table)
                elif item_type == "2":
                    console.print("[bold cyan]=== Books ===[/bold cyan]")
                    table = Table(show_header=True, header_style="bold cyan")
                    table.add_column("ID", style="bold")
                    table.add_column("Details", style="bold")
                    for key in db.keys("books"):
                        table.add_row(key, str(db.get("books", key)))
                    console.print(table)
                elif item_type == "3":
                    console.print("[bold cyan]=== DVDs ===[/bold cyan]")
                    table = Table(show_header=True, header_style="bold cyan")
                    table.add_column("ID", style="bold")
                    table.add_column("Details", style="bold")
                    for key in db.keys("dvd"):
                        table.add_row(key, str(db.get("dvd", key)))
                    console.print(table)
                elif item_type == "4":
                    console.print("[bold cyan]=== Magazines ===[/bold cyan]")
                    table = Table(show_header=True, header_style="bold cyan")
                    table.add_column("ID", style="bold")
                    table.add_column("Details", style="bold")
                    for key in db.keys("magazine"):
                        table.add_row(key, str(db.get("magazine", key)))
                    console.print(table)
                else:
                    console.print("[bold red]Invalid item type[/bold red]")
            except ValueError:
                console.print("[bold red]Invalid input. Please enter valid data.[/bold red]")
                continue


        elif choice == "4":
            console.print("[bold cyan]=== Search ===[/bold cyan]")
            console.print("1. [green]Search by author[/green]")
            console.print("2. [yellow]Search by title[/yellow]")
            search_option = input("\nEnter your search option (1 or 2): ")
            if search_option == "1":
                search_term = input("Enter author name: ")
                results = Item.search_item(db, search_term)
            elif search_option == "2":
                search_term = input("Enter title: ")
                results = Item.search_item(db, search_term)
            else:
                console.print("[bold red]Invalid search option[/bold red]")
                continue
            if results:
                console.print("[bold cyan]=== Search Results ===[/bold cyan]")
                table = Table(show_header=True, header_style="bold cyan")
                table.add_column("ID", style="bold")
                table.add_column("Type", style="bold")
                table.add_column("Details", style="bold")
                for result in results:
                    table.add_row(result[0], result[1]['type'], str(result[1]))
                    console.print(table)
            else:
                console.print("[bold red]No results found[/bold red]")

        elif choice == "5":
            # id all items id
            console.print("[bold cyan]=== All Items ===[/bold cyan]")
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("ID", style="bold")
            table.add_column("Type", style="bold")
            table.add_column("Details", style="bold")
            # loop in all tables
            for table_name in ['books', 'dvd', 'magazine']:
                for key in db.keys(table_name):
                    table.add_row(key, table_name, str(db.get(table_name, key)))
            console.print(table)

            # make user select item/s
            selected_items = []
            total_price = 0
            while True:
                item_id = input("Enter the item ID to add (or '0' to finish selecting): ")
                for table_name in ['books', 'dvd', 'magazine']:
                    for key in db.keys(table_name):
                        if key == item_id:
                            selected_items.append(item_id)
                            parsed_data = json.loads(db.get(table_name, key))
                            price = parsed_data['price']
                            total_price += float(price)
                            break
                if item_id == '0':
                    console.print(f"Selected items: {selected_items}")
                    console.print(f"Total price: {total_price}")
                    break
                if item_id not in db.keys('books') and item_id not in db.keys('dvd') and item_id not in db.keys('magazine'):
                    console.print("[bold red]Invalid item ID[/bold red]")

        elif choice == "6":
            console.print("[bold magenta]Goodbye![/bold magenta]")
            db.close()
            exit()

        else:
            console.print("[bold red]Invalid choice[/bold red]")

except KeyboardInterrupt:
    console.print("[bold red]Program terminated by user[/bold red]")
    db.close()
except Exception as e:
    console.print(f"[bold red]An error occurred:[/bold red] {str(e)}")
    db.close()
