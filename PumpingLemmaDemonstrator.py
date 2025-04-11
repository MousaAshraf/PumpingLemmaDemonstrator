import tkinter as tk
from tkinter import ttk, messagebox

def is_in_language(language, s):
    """Check if the pumped string belongs to the language with basic pattern matching."""
    if not language.strip():
        return True  # Accept all if no language specified
    if language.lower() == "a^n b^n":
        a_count = s.count('a')
        b_count = s.count('b')
        return a_count == b_count and all(c == 'a' for c in s[:a_count]) and all(c == 'b' for c in s[a_count:])
    elif language.lower() == "a^n b^n c^n":
        a_count = s.count('a')
        b_count = s.count('b')
        c_count = s.count('c')
        return (a_count == b_count == c_count and 
                all(c == 'a' for c in s[:a_count]) and 
                all(c == 'b' for c in s[a_count:a_count+b_count]) and 
                all(c == 'c' for c in s[a_count+b_count:]))
    elif language.lower() == "palindromes":
        return s == s[::-1]
    else:
        return True

def pump_string(x, y, z, i):
    return x + y * i + z

def validate_inputs():
    """Validate all inputs and return error message if any, else None."""
    s = entry_string.get().strip()
    x = entry_x.get().strip()
    y = entry_y.get().strip()
    z = entry_z.get().strip()
    try:
        pumping_length = int(entry_pumping_length.get())
    except ValueError:
        return "Please enter a valid integer for pumping length."
    
    if not s:
        return "Please enter a string s."
    if not x or not y or not z:
        return "Please enter values for x, y, and z."
    if not entry_i.get().strip():
        return "Please enter a value for i."
    
    try:
        i = int(entry_i.get())
        if i < 0:
            return "i must be a non-negative integer."
    except ValueError:
        return "Please enter an integer value for i."
    
    if x + y + z != s:
        return "Ensure that x + y + z equals the original string s."
    if not y:
        return "Substring y must not be empty (|y| > 0)."
    
    if len(x + y) > pumping_length:
        return f"The length of xy ({len(x + y)}) must be ≤ pumping length p ({pumping_length})."
    
    return None

def on_pump():
    error = validate_inputs()
    if error:
        messagebox.showerror("Invalid Input", error)
        return
    
    s = entry_string.get().strip()
    x = entry_x.get().strip()
    y = entry_y.get().strip()
    z = entry_z.get().strip()
    i = int(entry_i.get())
    language = entry_language.get("1.0", tk.END).strip()
    
    pumped = pump_string(x, y, z, i)
    result = is_in_language(language, pumped)
    
    result_text = (
        f"Original String: {s}\n"
        f"Split as: x='{x}', y='{y}', z='{z}'\n"
        f"Pumped String (i={i}): {pumped}\n"
        f"Belongs to Language: {'✅ Yes' if result else '❌ No'}"
    )
    
    if not language.strip():
        result_text += "\n\nNote: No language specified - result assumes all strings are valid."
    
    result_label.config(text=result_text)

def reset_inputs():
    """Reset all inputs and outputs to their default state."""
    entry_string.delete(0, tk.END)
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    entry_z.delete(0, tk.END)
    entry_i.delete(0, tk.END)
    entry_language.delete("1.0", tk.END)
    entry_pumping_length.delete(0, tk.END)
    entry_pumping_length.insert(0, "5")
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Pumping Lemma Demonstrator")


try:
    app_icon = tk.PhotoImage(file="logo.png") 
    root.iconphoto(False, app_icon)
except Exception as e:
    print(f"Error loading icon: {e}")

# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", font=("Arial", 11), background="#f8f9fa")
style.configure("TButton", font=("Arial", 11, "bold"))
style.configure("Header.TLabel", font=("Arial", 16, "bold"), background="#f8f9fa", foreground="#343a40")

# Main frame
main_frame = ttk.Frame(root, padding=(20, 15))
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Header
header = ttk.Label(main_frame, text="Pumping Lemma Demonstrator", style="Header.TLabel")
header.pack(pady=(0, 15))

# Input sections
def create_section(frame, title):
    section = ttk.Frame(frame)
    ttk.Label(section, text=title, font=("Arial", 11, "bold")).pack(anchor=tk.W, pady=(5, 2))
    return section

# Language section
lang_section = create_section(main_frame, "Language Definition")
lang_section.pack(fill=tk.X, pady=5)
ttk.Label(lang_section, text="Describe the language (e.g., aⁿbⁿ, palindromes):").pack(anchor=tk.W)
entry_language = tk.Text(lang_section, height=3, font=("Arial", 11), wrap=tk.WORD)
entry_language.pack(fill=tk.X, pady=5)

# String section
str_section = create_section(main_frame, "String to Pump")
str_section.pack(fill=tk.X, pady=5)
ttk.Label(str_section, text="Enter string s:").pack(anchor=tk.W)
entry_string = ttk.Entry(str_section)
entry_string.pack(fill=tk.X, pady=2)

# Pumping length
p_section = create_section(main_frame, "Pumping Length")
p_section.pack(fill=tk.X, pady=5)
ttk.Label(p_section, text="Enter pumping length p (≥0):").pack(anchor=tk.W)
entry_pumping_length = ttk.Entry(p_section)
entry_pumping_length.insert(0, "5")
entry_pumping_length.pack(fill=tk.X, pady=2)

# Split section
split_section = create_section(main_frame, "String Split")
split_section.pack(fill=tk.X, pady=5)
ttk.Label(split_section, text="Split s into x, y, z (s = xyz):").pack(anchor=tk.W)

split_grid = ttk.Frame(split_section)
split_grid.pack(fill=tk.X, pady=5)

ttk.Label(split_grid, text="x:").grid(row=0, column=0, padx=(0, 5), sticky=tk.W)
entry_x = ttk.Entry(split_grid)
entry_x.grid(row=0, column=1, sticky=tk.EW)

ttk.Label(split_grid, text="y:").grid(row=1, column=0, padx=(0, 5), sticky=tk.W)
entry_y = ttk.Entry(split_grid)
entry_y.grid(row=1, column=1, sticky=tk.EW)

ttk.Label(split_grid, text="z:").grid(row=2, column=0, padx=(0, 5), sticky=tk.W)
entry_z = ttk.Entry(split_grid)
entry_z.grid(row=2, column=1, sticky=tk.EW)

split_grid.columnconfigure(1, weight=1)

# Pumping factor
i_section = create_section(main_frame, "Pumping Factor")
i_section.pack(fill=tk.X, pady=5)
ttk.Label(i_section, text="Enter pumping factor i (≥0):").pack(anchor=tk.W)
entry_i = ttk.Entry(i_section)
entry_i.pack(fill=tk.X, pady=2)

# buttons 3ashan aconfirm
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=15)
pump_button = ttk.Button(button_frame, text="Pump String", command=on_pump)
pump_button.pack(side=tk.LEFT, padx=10)
reset_button = ttk.Button(button_frame, text="Reset", command=reset_inputs)
reset_button.pack(side=tk.LEFT, padx=10)

# Result display
result_frame = create_section(main_frame, "Result")
result_frame.pack(fill=tk.BOTH, expand=True, pady=5)
result_label = ttk.Label(
    result_frame, 
    text="", 
    font=("Consolas", 10), 
    foreground="#343a40",
    background="#e9ecef",
    relief=tk.GROOVE,
    padding=10,
    wraplength=650
)
result_label.pack(fill=tk.BOTH, expand=True)

root.mainloop()