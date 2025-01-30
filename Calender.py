import datetime
import tkinter as tk
from tkinter import ttk
import calendar
import json



class EventTime:
    def __init__(self):
        self.day, self.month, self.year = 0, 0, 0
        self.hour, self.minute = 0, 0

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def set_day(self, day):
        self.day = day

    def set_month(self, month):
        self.month = month

    def set_year(self, year):
        self.year = year

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute



class Event:
    def __init__(self, name="", place="", description=""):
        self.name = name
        self.place = place
        self.description = description
        self.time = EventTime()


class Calendar:
    def __init__(self):
        print("This is your Calendar")
        self.events = {}

    def add_event(self, event):
        date_key = f"{event.time.get_year()}-{event.time.get_month():02d}-{event.time.get_day():02d}"
        if date_key not in self.events:
            self.events[date_key] = []
        self.events[date_key].append(event)

    def get_events_for_day(self, year, month, day):
        date_key = f"{year}-{month:02d}-{day:02d}"
        return self.events.get(date_key, [])

    def remove_event(self, event):
        date_key = f"{event.time.get_year()}-{event.time.get_month():02d}-{event.time.get_day():02d}"
        if date_key in self.events:
            self.events[date_key].remove(event)
            if not self.events[date_key]:
                del self.events[date_key]

    def save_to_json(self, filename):
        serializable_events = {
            date: [
                {
                    "name": event.name,
                    "place": event.place,
                    "description": event.description,
                    "time": {
                        "day": event.time.get_day(),
                        "month": event.time.get_month(),
                        "year": event.time.get_year(),
                        "hour": event.time.get_hour(),
                        "minute": event.time.get_minute()
                    }
                }
                for event in event_list
            ]
            for date, event_list in self.events.items()
        }

        with open(filename, "w") as f:
            json.dump(serializable_events, f, indent=4)

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)

        self.events = {}
        for date, event_list in data.items():
            self.events[date] = []
            for event_data in event_list:
                event = Event(
                    name=event_data["name"],
                    place=event_data["place"],
                    description=event_data["description"]
                )
                event.time.set_day(event_data["time"]["day"])
                event.time.set_month(event_data["time"]["month"])
                event.time.set_year(event_data["time"]["year"])
                event.time.set_hour(event_data["time"]["hour"])
                event.time.set_minute(event_data["time"]["minute"])
                self.events[date].append(event)


class GUI:
    def __init__(self, root, calendar):
        self.root = root
        self.calendar = calendar
        self.root.title("Calendar App")
        self.root.geometry("500x500")

        self.minimize_button = tk.Button(self.root, text="_", command=self.minimize)
        self.minimize_button.place(x=10, y=10)

        self.close_button = tk.Button(self.root, text="X", command=self.root.quit)
        self.close_button.place(x=900, y=10)

        self.months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        self.month_var = tk.StringVar()
        self.month_var.set(self.months[datetime.datetime.now().month - 1])  # Setzt den aktuellen Monat als Standardwert

        self.month_dropdown = ttk.Combobox(self.root, textvariable=self.month_var, values=self.months, state="readonly")
        self.month_dropdown.place(x=150, y=10)
        self.month_dropdown.bind("<<ComboboxSelected>>", self.update_calendar)

        self.year_var = tk.StringVar()
        self.year_var.set(str(datetime.datetime.now().year))

        self.year_dropdown = ttk.Combobox(self.root, textvariable=self.year_var, state="readonly",
                                          values=[str(year) for year in
                                                  range(2020, 2031)])  # Beispiel Jahre 2020 bis 2030
        self.year_dropdown.place(x=250, y=10)
        self.year_dropdown.bind("<<ComboboxSelected>>", self.update_calendar)

        self.calendar_frame = tk.Frame(self.root)
        self.calendar_frame.place(x=50, y=50)

        self.scroll_frame = tk.Frame(self.root)
        self.scroll_frame.place(x=950, y=20)

        scrollbar = tk.Scrollbar(self.scroll_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_display = tk.Text(self.scroll_frame, height=20, width=30, yscrollcommand=scrollbar.set)
        self.text_display.pack(side=tk.LEFT)

        scrollbar.config(command=self.text_display.yview)

        self.update_calendar()

    def minimize(self):
        self.root.iconify()

    def update_calendar(self, event=None):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        month = self.months.index(self.month_var.get()) + 1
        year = int(self.year_var.get())  # Das Jahr aus dem Dropdown-Menü holen

        first_day, num_days = calendar.monthrange(year, month)

        days_of_week = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        for i, day in enumerate(days_of_week):
            label = tk.Label(self.calendar_frame, text=day, width=5, height=2, anchor='center')
            label.grid(row=0, column=i, padx=5, pady=5)

        row = 1
        col = first_day
        for day in range(1, num_days + 1):
            day_button = tk.Button(self.calendar_frame, text=str(day), width=5, height=2,
                                   command=lambda d=day: self.select_day(d))
            day_button.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 6:
                col = 0
                row += 1

    def select_day(self, day):
        print(f"Tag {day} wurde ausgewählt!")
        selected_month = self.months.index(self.month_var.get()) + 1
        selected_year = int(self.year_var.get())

        self.selected_day = day

        events_on_day = self.calendar.get_events_for_day(selected_year, selected_month, day)
        self.show_event_options(events_on_day)

    def show_event_options(self, events):
        options_popup = tk.Toplevel(self.root)
        options_popup.title("Ereignis Optionen")

        if events:
            for event in events:
                frame = tk.Frame(options_popup)
                frame.pack(padx=10, pady=5, fill="x")

                time_str = f"{event.time.get_hour():02d}:{event.time.get_minute():02d}"
                label = tk.Label(frame, text=f"{event.name} ({time_str})", anchor="w")
                label.pack(side="left", padx=5)

                # Buttons für die Aktionen
                show_button = tk.Button(frame, text="Anzeigen",
                                        command=lambda e=event: self.show_event_details(e))
                show_button.pack(side="right", padx=5)

                edit_button = tk.Button(frame, text="Bearbeiten",
                                        command=lambda e=event: self.edit_event(e, options_popup))
                edit_button.pack(side="right", padx=5)

                delete_button = tk.Button(frame, text="Löschen",
                                          command=lambda e=event: self.delete_event(e, options_popup))
                delete_button.pack(side="right", padx=5)
        else:
            label = tk.Label(options_popup, text="Keine Ereignisse für diesen Tag.")
            label.pack(padx=10, pady=10)

        add_button = tk.Button(options_popup, text="Neues Ereignis hinzufügen",
                               command=lambda: self.add_event(options_popup))
        add_button.pack(pady=10)

    def show_event_details(self, event):
        details_popup = tk.Toplevel(self.root)
        details_popup.title("Ereignis Details")

        time_str = f"{event.time.get_hour():02}:{event.time.get_minute():02}"

        message = (
            f"Name: {event.name}\n"
            f"Ort: {event.place}\n"
            f"Beschreibung: {event.description}\n"
            f"Uhrzeit: {time_str}"
        )
        label = tk.Label(details_popup, text=message, padx=10, pady=10)
        label.pack()

        close_button = tk.Button(details_popup, text="Schließen", command=details_popup.destroy)
        close_button.pack()

    def delete_event(self, event, popup):
        self.calendar.remove_event(event)
        popup.destroy()
        print(f"Ereignis '{event.name}' wurde gelöscht.")
        self.calendar.save_to_json("events.json")
        print("Ereignisse in JSON-Datei gespeichert.")
        self.display_events()

    def edit_event(self, event, popup):
        edit_popup = tk.Toplevel(self.root)
        edit_popup.title("Ereignis bearbeiten")

        name_label = tk.Label(edit_popup, text="Name des Ereignisses:")
        name_label.pack()
        name_entry = tk.Entry(edit_popup)
        name_entry.insert(0, event.name)
        name_entry.pack()

        place_label = tk.Label(edit_popup, text="Ort:")
        place_label.pack()
        place_entry = tk.Entry(edit_popup)
        place_entry.insert(0, event.place)
        place_entry.pack()

        description_label = tk.Label(edit_popup, text="Beschreibung:")
        description_label.pack()
        description_entry = tk.Entry(edit_popup)
        description_entry.insert(0, event.description)
        description_entry.pack()

        time_label = tk.Label(edit_popup, text="Uhrzeit (HH:MM):")
        time_label.pack()
        time_entry = tk.Entry(edit_popup)
        time_str = f"{event.time.get_hour():02}:{event.time.get_minute():02}"
        time_entry.insert(0, time_str)
        time_entry.pack()

        save_button = tk.Button(edit_popup, text="Speichern",
                                command=lambda: self.save_event_edit(
                                    event, name_entry.get(), place_entry.get(),
                                    description_entry.get(), time_entry.get(), edit_popup))
        save_button.pack()
        popup.destroy()
        self.display_events()

    def save_event_edit(self, event, name, place, description, time_str, popup):
        try:
            hour, minute = map(int, time_str.split(":"))
        except ValueError:
            hour, minute = 0, 0  # sets time to 00:00, if input is invalid

        event.name = name
        event.place = place
        event.description = description
        event.time.set_hour(hour)
        event.time.set_minute(minute)

        popup.destroy()
        print(f"Ereignis '{event.name}' wurde bearbeitet.")
        self.calendar.save_to_json("events.json")
        print("Ereignisse in JSON-Datei gespeichert.")
        self.display_events()

    def add_event(self, options_popup):
        add_popup = tk.Toplevel(self.root)
        add_popup.title("Neues Ereignis hinzufügen")

        name_label = tk.Label(add_popup, text="Name des Ereignisses:")
        name_label.pack()
        name_entry = tk.Entry(add_popup)
        name_entry.pack()

        place_label = tk.Label(add_popup, text="Ort:")
        place_label.pack()
        place_entry = tk.Entry(add_popup)
        place_entry.pack()

        description_label = tk.Label(add_popup, text="Beschreibung:")
        description_label.pack()
        description_entry = tk.Entry(add_popup)
        description_entry.pack()

        time_label = tk.Label(add_popup, text="Uhrzeit (HH:MM):")
        time_label.pack()
        time_entry = tk.Entry(add_popup)
        time_entry.pack()

        selected_day = self.selected_day
        selected_month = self.months.index(self.month_var.get()) + 1
        selected_year = 2025

        save_button = tk.Button(add_popup, text="Speichern",
                                command=lambda: self.save_new_event(
                                    name_entry.get(), place_entry.get(),
                                    description_entry.get(), time_entry.get(),
                                    selected_day, selected_month, selected_year,
                                    add_popup, options_popup))
        save_button.pack()
        self.display_events()

    def save_new_event(self, name, place, description, time_str, day, month, year, add_popup, options_popup):
        try:
            hour, minute = map(int, time_str.split(":"))
        except ValueError:
            hour, minute = 0, 0  # sets time to 00:00, if input is invalid

        # make a new event
        new_event = Event(name, place, description)
        new_event.time.set_day(day)
        new_event.time.set_month(month)
        new_event.time.set_year(year)
        new_event.time.set_hour(hour)
        new_event.time.set_minute(minute)
        self.calendar.add_event(new_event)

        # close every pop up
        add_popup.destroy()
        options_popup.destroy()
        print(f"Neues Ereignis '{name}' wurde hinzugefügt.")
        self.calendar.save_to_json("events.json")
        print("Ereignisse in JSON-Datei gespeichert.")
        self.display_events()

    def display_events(self):
        self.text_display.delete(1.0, tk.END)
        for date, events in self.calendar.events.items():
            self.text_display.insert(tk.END, f"Datum: {date}\n")
            for event in events:
                self.text_display.insert(tk.END, f"- {event.name}\n")
            self.text_display.insert(tk.END, "\n")


# main program
if __name__ == "__main__":
    calendar_instance = Calendar()

    try:
        calendar_instance.load_from_json("events.json")
        print("JSON-Datei gefunden.")
    except FileNotFoundError:
        print("JSON-Datei nicht gefunden. Eine neue Datei wird erstellt.")

    root = tk.Tk()
    app = GUI(root, calendar_instance)
    app.display_events()  # Events beim Start anzeigen
    root.mainloop()

