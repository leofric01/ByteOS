ByteOS - Modular CLI Simulator 🚀

ByteOS is a lightweight, modular Command Line Interface (CLI) Operating System simulator built with pure Python. It provides a simplified terminal environment executing standard core tools through clean, straightforward commands.

🌟 Features (Version 1.0)

ByteOS v1.0 delivers 5 essential core tools operating in a continuous execution loop:

0 | Help (show_help): Displays system command instructions and basic menu details.

1 | About (show_about): Fetches real-time system metadata (OS type, release, and processor specs) using Python's platform module.

2 | Date (date): Prints formatted local date and time via the datetime module.

3 | Clear (clear_screen): Cross-platform terminal screen cleaner (works seamlessly on Windows cls and Linux/macOS clear).

4 | Shutdown (shutdown): Safely closes the ByteOS execution loop.

🏗 Project Architecture

The project follows a clean separation of concerns design pattern:

ByteOS/
│
├── main.py            # Execution controller & continuous input loop
└── System_tools.py    # Core system function definitions & library integrations


🚀 How to Run Locally

Clone the repository:

git clone https://github.com/your-username/ByteOS.git
cd ByteOS


Run the application:

python main.py


🔮 Roadmap (Coming Soon in v2.0)

ByteOS is actively evolving! Planned features for v2.0 include:

📁 Basic File Manager: Create, list, read, and delete simple text files.

🧮 Built-in CLI Calculator: Quick mathematical evaluations.

⚙️ Extended Command Arguments: Support for multi-string parameters instead of numeric selection only.

🎨 Terminal Styling: Colored text and custom ASCII banners.

📄 License

This project is open-source and available under the MIT License
