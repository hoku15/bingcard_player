import tkinter as tk
import random

class BingoCard:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Bingo Card Generator")
        self.card_numbers = []
        self.buttons = []
        self.selected = set()
        self.create_bingo_card()

    def generate_card_numbers(self):
        self.card_numbers = []
        columns = {
            0: range(1, 16),     # B列の範囲
            1: range(16, 31),    # I列の範囲
            2: range(31, 46),    # N列の範囲（中央はFree）
            3: range(46, 61),    # G列の範囲
            4: range(61, 76)     # O列の範囲
        }
        for col in range(5):
            column_numbers = random.sample(columns[col], 5)
            if col == 2:
                column_numbers[2] = "FREE"
            self.card_numbers.append(column_numbers)

    def create_bingo_card(self):
        self.generate_card_numbers()
        for row in range(5):
            button_row = []
            for col in range(5):
                number = self.card_numbers[col][row]
                button = tk.Button(self.root, text=number, width=6, height=3, font=("Arial", 16),
                                   command=lambda r=row, c=col: self.select_number(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def select_number(self, row, col):
        button = self.buttons[row][col]
        if button["bg"] == "lightgreen":
            button["bg"] = "SystemButtonFace"
            self.selected.discard((row, col))
        else:
            button["bg"] = "lightgreen"
            self.selected.add((row, col))
        self.check_bingo()

    def check_bingo(self):
        for line in self.get_lines():
            if len(self.selected.intersection(line)) == 5:
                self.show_message("Bingo!")
                return
            elif len(self.selected.intersection(line)) == 4:
                self.show_message("Reach!")

    def get_lines(self):
        lines = []
        # 横のライン
        for row in range(5):
            lines.append({(row, col) for col in range(5)})
        # 縦のライン
        for col in range(5):
            lines.append({(row, col) for row in range(5)})
        # 斜めのライン
        lines.append({(i, i) for i in range(5)})
        lines.append({(i, 4 - i) for i in range(5)})
        return lines

    def show_message(self, message):
        popup = tk.Toplevel()
        popup.title("Notification")
        label = tk.Label(popup, text=message, font=("Arial", 16))
        label.pack(padx=20, pady=20)
        button = tk.Button(popup, text="OK", command=popup.destroy)
        button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoCard(root)
    root.mainloop()
