# 📅 Python Calendar Planner

A terminal-based calendar planner that allows users to add, view, and manage personal events with automatic tagging for overdue and upcoming tasks using intuitive emoji icons.

---

## ✅ Features

- ➕ Add new events (with date, time, and event name)
- 📋 View all events
- 🔜 Show only upcoming events
- ❌ Delete events
- 🚪 Exit the planner

---

## 📄 Data Structure

All event data is stored in a file called `events.csv` with the following **4 columns**:

| Date       | Time   | Event Name           | Status        |
|------------|--------|----------------------|----------------|
| 2025-07-15 | 15:30  | Doctor Appointment    | ⌛ OVERDUE     |
| 2025-07-20 | 10:00  | DS Internship Call    | 📍 UPCOMING    |

> ⚠️ Note: The "Status" is automatically calculated based on the current date and time.

---

## 🧠 Status Logic

- ⌛ **OVERDUE**: If the event’s date and time are in the past.
- 📍 **UPCOMING**: If the event’s date and time are today or in the future.

---

## 📋 Menu Overview

📅 Welcome to Python Calendar Planner

Please choose an option:

1. ➕ Add New Event

2. 📋 Show All Events

3. 🔜 Show Upcoming Events

4. ❌ Delete an Event

5. 🚪 Exit


---

## 🔧 Functional Overview

- `add_event()` — Add a new event to the planner.
- `show_all_events()` — Display all saved events with automatic status tags.
- `show_upcoming_events()` — Display only upcoming events.
- `delete_event()` — Remove an event from the planner by index.
- `main_menu()` — Interactive loop to navigate the planner options.

---

## 💾 File Handling

- All events are saved in **`events.csv`**.
- Columns: `Date`, `Time`, `Event Name`
- Status (`OVERDUE` / `UPCOMING`) is **not stored**, it is dynamically shown at runtime.

---

## 📌 Technologies Used

- Python (Built-in)
- CSV module
- `datetime` module for date/time comparison

---

## 🚀 Future Improvements

- [ ] Add event reminders

---
