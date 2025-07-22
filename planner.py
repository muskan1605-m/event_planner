import csv
import os
from datetime import datetime

# Display the main menu to the user
def show_menu():
    print("\n📅 Welcome to Python Calendar Planner\n")
    print("Please choose an option:")
    print("1. ➕ Add New Event")
    print("2. 📋 Show All Events")
    print("3. 🔜 Show Upcoming Events")
    print("4. ❌ Delete an Event")
    print("5. 🚪 Exit")

# Validate that the date string is in the correct format (YYYY-MM-DD)
def validate_date(date_str): 
    try:
        datetime.strptime(date_str, "%Y-%m-%d") # specifies the date format
        return True
    except ValueError: 
        return False

# Validate that the time string is in the correct format (HH:MM)
def validate_time(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

# Calculate the status of an event (OVERDUE or UPCOMING) based on current date and time
def get_event_status(event_date, event_time):
    try:
        event_dt = datetime.strptime(f"{event_date} {event_time}", "%Y-%m-%d %H:%M")
        now = datetime.now()
        if event_dt < now:
            return "⌛ OVERDUE"
        else:
            return "📍 UPCOMING"
    except Exception:
        return "?"  # Return ? if date/time is invalid

# Add a new event to the planner and store it in events.csv
def add_event():
    try:
        # Get and validate the event date
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not date:
            print("❌ Date cannot be empty.")
            return
        if not validate_date(date):
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            return

        # Get and validate the event time
        time = input("Enter time (HH:MM): ").strip()
        if not time:
            print("❌ Time cannot be empty.")
            return
        if not validate_time(time):
            print("Invalid time format. Please use HH:MM")
            return

        # Get and validate the event name
        event_name = input("Enter event name: ").strip()
        if not event_name:
            print("Event cannot be empty.")
            return

        # Calculate the status for the event
        status = get_event_status(date, time)  # calculates the status

        # Open the file in append mode and write the event
        with open("events.csv", "a", newline='') as file:  # opens the file in append mode
            writer = csv.writer(file)
            writer.writerow([date, time, event_name, status])  # writes the event to the file

        print("✅ Event added successfully.")

    except Exception as e:
        print(f"❌ Error adding event: {e}")

# Show all events in a formatted table, with their status calculated live
def show_all_events():
    # Open the events.csv file and read all rows
    with open("events.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) <= 1:
            print("\n📝 No events recorded yet.")
            return
        print("\n--- All Events ---")
        print(f"{'No.':<4} {'Date':<12} {'Time':<6} {'Event Name':<25} {'Status':<12}")
        print("-" * 65)
        # Loop through each event (skip header row)
        for i, row in enumerate(rows[1:], 1):
            if len(row) >= 3:
                date, time, event_name = row[:3]
                status = get_event_status(date, time)
                print(f"{i:<4} {date:<12} {time:<6} {event_name:<25} {status:<12}")

#show only UPCOMING status
def show_upcoming_events():
    # Open the events.csv file and read all rows
    with open("events.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) <= 1:
            print("\n📝 No Upcoming events found.")
            return
        print("\n--- Upcoming Events----")
        print(f"{'No.':<4} {'Date':<12} {'Time':<6} {'Event Name':<25} {'Status':<12}")
        print("-" * 65)
        count = 0
        for i, row in enumerate(rows[1:], 1):  # skip header
            if len(row) >= 3:
                date, time, event_name = row[:3]
                status = get_event_status(date, time)
                if status == "📍 UPCOMING":
                    count += 1
                    print(f"{count:<4} {date:<12} {time:<6} {event_name:<25} {status:<12}")
        if count == 0:
            print("No upcoming events found.")

# To delete an event from the planner
def delete_event():
    try:
        file_path = "events.csv"
        with open(file_path, "r", newline='') as file:
            reader = csv.reader(file)
            all_rows = list(reader)

        if not all_rows:
            print("\nNo events file found.")
            return

        header = all_rows[0]
        events = [row for row in all_rows[1:] if any(row)]  # Get a clean list of events, skipping header and blank rows

        if not events:
            print("\nNo events to delete.")
            return

        # Display the clean list of events for the user to choose from
        print("\n--- Select an Event to Delete ---\n")
        print(f"{'No.':<4} {'Date':<12} {'Time':<6} {'Event Name':<25} {'Status'}")
        print("-" * 65)
        for i, row in enumerate(events, 1):
            if len(row) >= 4:
                print(f"{i:<4} {row[0]:<12} {row[1]:<6} {row[2]:<25} {row[3]}")
            else: # Fallback for rows with missing data
                print(f"{i:<4} {row[0]:<12} {row[1]:<6} {row[2]:<25}")
        
        # Get user input and validate it against the number of displayed events
        try:
            choice = int(input("\nEnter the number of the event to delete: "))
            if not (1 <= choice <= len(events)):
                print("❌ Invalid number.")
                return
        except ValueError:
            print("❌ Please enter a valid number.")
            return

        # Confirm deletion with a correctly formatted message
        event_to_delete = events[choice - 1]
        print(f"\nYou are about to delete: {event_to_delete[0]} - {event_to_delete[2]}")
        confirm = input("Are you sure? (yes/no): ").lower().strip()

        if confirm != 'yes':
            print("❌ Deletion cancelled.")
            return

        # Remove the selected event from our clean list
        events.pop(choice - 1)

        # Write the header and the updated events list back to the file
        with open(file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(events)

        print("✅ Event deleted successfully!")

    except FileNotFoundError:
        print("❌ Events file not found.")
    except Exception as e:
        print(f"❌ Error deleting event: {e}")


# Main loop: show the menu and handle user choices
while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()
    if choice == '1':
        add_event()
    elif choice == '2':
        show_all_events()
    elif choice == '3':
        show_upcoming_events()
    elif choice == '4':
        delete_event()
    elif choice == '5':
        exit()
        print("Exiting the planner.")
    else:
        print("Invalid choice, please try again.")


