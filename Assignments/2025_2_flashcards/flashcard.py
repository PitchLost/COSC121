'''Docstring'''
import json
import glob
import copy
from datetime import datetime, timedelta

DATE_FORMAT = "%Y/%m/%d"
TABLE_FORMAT = "{:10} {:>4} {:>4} {:>4}"


def read_deck(filename):
    """Standard means to read a json file to a list of cards"""
    with open(filename, encoding='utf-8') as file:
        deck = json.load(file)

    for card in deck:
        if card["due"] is not None:
            card["due"] = datetime.strptime(card["due"], DATE_FORMAT)
    return deck

# Dumps deck to JSON files
def write_deck(filename, deck):
    """Standard means to write a list of cards to a json file"""
    deck = copy.deepcopy(deck)
    for card in deck:
        if card["due"] is not None:
            card["due"] = card["due"].strftime(DATE_FORMAT)

    with open(filename, "w", encoding='utf-8') as file:
        json.dump(deck, file, indent=4)


def deck_filenames():
    """Provides and alphabetized list of all deck (*.json) files"""
    return sorted(glob.glob("*.json"))


def user_prompt(options):
    """Returns the index of the option selected"""
    def choice():
        """Returns the correct an index if it is valid index"""
        for i, value in enumerate(options):
            print(f"{i}: {value}")
        try:
            index = int(input("enter a number: "))
        except ValueError:
            return None
        else:
            return index if index < len(options) else None

    while (selection := choice()) is None:
        print("Invalid selection")
    return selection


def select_deck_and_study():
    """Manager of a Study functionality
      - displaying available decks
      - loads a selected deck
      - runs the student through each due card
        - the updater pattern is used to record each change
      - writes the deck to a .json file again
    """
    prompts = deck_filenames() + ["Back"]
    choice = user_prompt([name.rsplit('.', maxsplit=1)[0] for name in prompts])

    if choice == len(prompts) - 1:
        return
    deck_name = prompts[choice]
    deck = read_deck(deck_name)
    run_test(deck)
    write_deck(deck_name, deck)


def due_cards(deck):
    """returns the indices of cards that are due today"""
    due = []
    for i, card in enumerate(deck):
        is_new = card["due"] is None
        is_due = is_new or card["due"] <= datetime.today()
        if is_due:
            due.append(i)
    return due

# Checks if the user got it right or wrong and also updates the due date?
def run_test(deck):
    """Runs a student through the cards that a student should study.
    Each card that is attempted is updated."""
    due = due_cards(deck)
    print(f"You have {len(due)} to translate today")

    for i in due:
        card = deck[i]
        print(f"{card['lang1']}: {card['term1']}")
        attempt = input(f"{card['lang2']}: ")
        answer = card['term2']
        if attempt.casefold() == answer.casefold():
            print("Correct")
            card["streak"] += 1
            card["due"] = datetime.today() + timedelta(days=2**(card['streak'] - 1)) # My code

            # print(f"[DEBUG] days={(card['streak'] - 1) * 2}")
        else:
            print("Incorrect")
            print(f"Answer: {answer}")
            card["streak"] = 0
            card["due"] = datetime.today()

def overview():
    """Prints a summary table of cards grouped by type and status."""
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    # Initialize the dynamic stats dictionary
    stats_dynamic = {}

    for filename in deck_filenames():
        deck = read_deck(filename)

        # Initialize the stats for this deck
        stats_dynamic[filename] = {'New': 0, 'Due': 0, 'Done': 0}

        for card in deck:
            # Determine the card's category
            if card['due'] is None:
                category = 'New'
            elif card['due'].replace(hour=0, minute=0, second=0, microsecond=0) <= today:
                category = 'Due'
            else:
                category = 'Done'

            # Increment the appropriate counter
            stats_dynamic[filename][category] += 1

    # Print header
    print(TABLE_FORMAT.format("", "New", "Due", "Done"))

    # Print rows sorted by deck filename
    for filename in sorted(stats_dynamic):
        new = stats_dynamic[filename]['New']
        due = stats_dynamic[filename]['Due']
        done = stats_dynamic[filename]['Done']
        name_without_ext = filename.rsplit('.', 1)[0]
        print(TABLE_FORMAT.format(name_without_ext, new, due, done))
    print('')


def main():
    """Enters the main program loop"""
    prompts = ["Study", "Overview", "Create Deck", "Quit"]
    while True:
        choice = user_prompt(prompts)
        if choice == 0:
            select_deck_and_study()
        elif choice == 1:
            overview() # Call the implemented overview function
            user_prompt({'Back'})
        elif choice == 2:
            print("The Create Deck feature has not been implemented yet.")
            print("Aspects of this feature are discussed in question 6, 7 and 8.")
        else:
            print("Bye!")
            return


main()