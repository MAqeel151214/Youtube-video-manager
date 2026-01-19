📺 YouTube Video Manager (Python CLI App)

A simple, interactive command-line YouTube video manager written in Python.
This project lets you:

📃 List saved YouTube videos

➕ Add new videos

✏️ Update video details

🗑️ Delete videos

💾 Automatically save everything to youtube.txt (JSON format)

🚀 Features

Clean and colorful terminal UI

Full CRUD support

Stores data in a local .txt JSON file

Safe handling of corrupted or missing files

UTF-8 support for emojis and multilingual titles

Fully cross-platform (Linux, Windows, macOS)

📸 Screenshots
🖥️ Main Menu

⌨️ Input Display Example

📂 Project Structure
Youtube-video-manager/
│
├── app.py               # Main application code
├── youtube.txt          # Database file (created automatically)
├── Readme.md            # Documentation
└── preview.png          # Screenshot
    
   

🛠️ Installation
1️⃣ Clone the repository
git clone https://github.com/MAqeel151214/Youtube-video-manager.git
cd Youtube-video-manager

2️⃣ Install dependencies

The project uses only Python’s standard library, but installing from requirements.txt keeps things consistent:

pip install -r requirements.txt

▶️ Run the Application
python app.py

Optional: use a custom data file
- CLI flag: python app.py --file my_videos.json
- Env var: YVM_FILE=/path/to/my_videos.json python app.py

📦 Data Storage

All videos are saved in a JSON-formatted text file:

youtube.txt


Example:

[
  {
    "Name": "Python Crash Course",
    "Time": "12:40"
  }
]

✨ How It Works
Menu Options
Option	Action
1	List all saved videos
2	Add a new video
3	Update a video
4	Delete a video
5	Exit
🐞 Known Terminal Issue (Linux)

Some Linux terminals (especially with Zsh/Bash history expansion) may eat or erase the number 1 when pressing Enter.

Fix:

set +o histexpand


or add this line to ~/.bashrc.

🤝 Contributing

Pull requests, issues, and suggestions are welcome!

📜 License

This project is open-source under the MIT License.