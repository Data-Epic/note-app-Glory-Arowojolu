from datetime import datetime

# Base class
class Note:
    def __init__(self, content):
        self.content = content
        self.created_at = datetime.now()
    
    def display(self):
        print(f"Note created at: {self.created_at}")
        print(f"Content: {self.content}")

# Subclass for simple text notes
class TextNote(Note):
    def __init__(self, content):
        super().__init__(content)

# Subclass for reminder notes
class ReminderNote(Note):
    def __init__(self, content, reminder_time):
        super().__init__(content)
        self.reminder_time = reminder_time
    
    def display(self):
        super().display()
        print(f"Reminder set for: {self.reminder_time}")


# Notes Manager class
class NotesManager:
    def __init__(self):
        self.notes = []
        self.next_id = 1
    
    def add_note(self, note_type, content, reminder_time=None):
        if note_type == "text":
            note = TextNote(content)
        elif note_type == "reminder" and reminder_time:
            note = ReminderNote(content, reminder_time)
        else:
            print("Invalid note type or missing reminder time.")
            return
        
        self.notes.append((self.next_id, note))
        print(f"Note added with ID: {self.next_id}")
        self.next_id += 1
    
    def delete_note(self, note_id):
        self.notes = [(id, note) for id, note in self.notes if id != note_id]
        print(f"Note with ID {note_id} deleted.")
    
    def show_notes(self):
        for id, note in self.notes:
            print(f"\nNote ID: {id}")
            note.display()
    
    def search_notes(self, keyword):
        found_notes = [note for id, note in self.notes if keyword.lower() in note.content.lower()]
        for note in found_notes:
            note.display()
        if not found_notes:
            print("No notes found with that keyword.")

# Main Program Execution
def main():
    manager = NotesManager()
    while True:
        print("\n1. Add Note\n2. Delete Note\n3. Show Notes\n4. Search Notes\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            note_type = input("Enter note type (text/reminder): ")
            content = input("Enter note content: ")
            reminder_time = None
            if note_type == "reminder":
                reminder_input = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
                try:
                    reminder_time = datetime.strptime(reminder_input, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("Invalid date format.")
                    continue
            manager.add_note(note_type, content, reminder_time)
        elif choice == "2":
            note_id = int(input("Enter note ID to delete: "))
            manager.delete_note(note_id)
        elif choice == "3":
            manager.show_notes()
        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            manager.search_notes(keyword)
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()