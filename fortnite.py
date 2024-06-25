import tkinter as tk
from tkinter import messagebox

class FortniteQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fortnite Drop Spot Quiz")
        
        self.questions = [
            "What type of environment do you prefer?",
            "What kind of loot density are you looking for?",
            "Do you prefer crowded or quiet drop spots?",
            "Do you want to be close to the center of the map or on the outskirts?"
        ]
        
        self.options = [
            ["Urban areas with lots of buildings", "Forested areas with lots of cover", "Remote areas with few buildings", "Coastal areas with water access"],
            ["High loot density", "Moderate loot density", "Low loot density", "Mixed loot density"],
            ["Crowded with lots of players", "Moderately crowded", "Quiet with few players", "Very quiet and secluded"],
            ["Close to the center", "Moderately close", "Far from the center", "Very far from the center"]
        ]
        
        self.answers = []
        self.current_question = 0
        
        self.question_label = tk.Label(root, text=self.questions[self.current_question])
        self.question_label.pack(pady=20)
        
        self.var = tk.IntVar()
        self.create_radio_buttons()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)
    
    def create_radio_buttons(self):
        for i, option in enumerate(self.options[self.current_question]):
            rb = tk.Radiobutton(self.root, text=option, variable=self.var, value=i+1)
            rb.pack(anchor=tk.W)
        self.var.set(1)
    
    def clear_radio_buttons(self):
        for widget in self.root.pack_slaves():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()
    
    def next_question(self):
        self.answers.append(self.var.get())
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            self.clear_radio_buttons()
            self.create_radio_buttons()
        else:
            self.show_result()
    
    def show_result(self):
        drop_spot = self.get_drop_spot(self.answers)
        messagebox.showinfo("Recommended Drop Spot", f"Based on your answers, you should drop at: {drop_spot}")
        self.root.destroy()
    
    def get_drop_spot(self, answers):
        if answers[0] == 1:
            if answers[1] == 1:
                return "Nitrodrome"
            elif answers[1] == 2:
                return "Rebel’s Roost"
            elif answers[1] == 3:
                return "Reckless Railways"
            else:
                return "Restored Reels"
        elif answers[0] == 2:
            if answers[1] == 1:
                return "Brutal Beachhead"
            elif answers[1] == 2:
                return "Redline Rig"
            elif answers[1] == 3:
                return "Grim Gate"
            else:
                return "The Underworld"
        elif answers[0] == 3:
            if answers[1] == 1:
                return "Mount Olympus"
            elif answers[1] == 2:
                return "Brawler’s Battleground"
            elif answers[1] == 3:
                return "Lavish Lair"
            else:
                return "Classy Courts"
        else:
            if answers[1] == 1:
                return "Grand Glacier"
            elif answers[1] == 2:
                return "Pleasant Piazza"
            elif answers[1] == 3:
                return "Snooty Steppes"
            else:
                return "Restored Reels"

if __name__ == "__main__":
    root = tk.Tk()
    app = FortniteQuizApp(root)
    root.mainloop()
