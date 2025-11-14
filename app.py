import json
import os
import sys

# Configuration
VIDEO_FILE = "youtube.txt"


# --- Data Handling Helper Functions ---

def load_data():
    """Loads video data from youtube.txt or returns an empty list if not found."""
    try:
        if not os.path.exists(VIDEO_FILE):
            return []
        with open(VIDEO_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️  Error: Video file is corrupted. Starting with empty list.")
        return []
    except Exception as e:
        print(f"⚠️  Error loading data: {e}")
        return []


def save_data_helper(videos):
    """Writes the current list of videos to youtube.txt."""
    try:
        with open(VIDEO_FILE, "w", encoding="utf-8") as file:
            json.dump(videos, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Error saving data: {e}")


# --- Core CRUD Functions ---

def list_all_videos(videos):
    """Prints all videos with 1-based indexing."""
    # Add an explicit newline to ensure previous input echo is separated from output
    print()
    if not videos:
        print("\n" + "=" * 70)
        print("📭 No videos found. Add some videos to get started!")
        print("=" * 70)
        return

    print("\n" + "=" * 70)
    print("🎬 YOUR YOUTUBE VIDEOS".center(70))
    print("=" * 70)

    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video.get('Name', 'N/A'):<50} | Duration: {video.get('Time', 'N/A')}")

    print("=" * 70 + "\n")


def add_video(videos):
    """Prompts user for details and adds a new video dictionary to the list."""
    print("\n" + "-" * 70)
    print("➕ ADD NEW VIDEO")
    print("-" * 70)

    # Validate video name
    name = input("Enter video name: ").strip()
    if not name:
        print("❌ Error: Video name cannot be empty!")
        return

    # Validate video duration
    time = input("Enter video duration (e.g., 10:30): ").strip()
    if not time:
        print("❌ Error: Video duration cannot be empty!")
        return

    videos.append({'Name': name, 'Time': time})
    save_data_helper(videos)
    print(f"✅ Video '{name}' added successfully!\n")


def update_video(videos):
    """Updates the details of an existing video based on user input."""
    if not videos:
        print("❌ No videos to update!")
        return

    list_all_videos(videos)

    try:
        raw = input("Enter the video number to update: ").strip()
        index = int(raw)
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        return

    if 1 <= index <= len(videos):
        print("\n" + "-" * 70)
        print(f"✏️  UPDATING VIDEO #{index}")
        print("-" * 70)

        new_name = input("Enter new video name (or press Enter to keep): ").strip()
        new_time = input("Enter new video duration (or press Enter to keep): ").strip()

        if new_name:
            videos[index - 1]['Name'] = new_name
        if new_time:
            videos[index - 1]['Time'] = new_time

        save_data_helper(videos)
        print(f"✅ Video #{index} updated successfully!\n")
    else:
        print("❌ Invalid video number selected!")


def delete_video(videos):
    """Deletes a video entry based on user-provided index."""
    if not videos:
        print("❌ No videos to delete!")
        return

    list_all_videos(videos)

    try:
        raw = input("Enter the video number to delete: ").strip()
        index = int(raw)
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        return

    if 1 <= index <= len(videos):
        deleted_video = videos[index - 1]['Name']
        del videos[index - 1]
        save_data_helper(videos)
        print(f"✅ Video '{deleted_video}' deleted successfully!\n")
    else:
        print("❌ Invalid video number selected!")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 70)
    print("🎥 YOUTUBE VIDEO MANAGER 🎥".center(70))
    print("=" * 70)
    print("1. 📺 List All Videos")
    print("2. ➕ Add a New Video")
    print("3. ✏️  Update a Video")
    print("4. 🗑️  Delete a Video")
    print("5. 🚪 Exit")
    print("=" * 70 + "\n")


# --- Main Application Logic ---

def main():
    videos = load_data()
    print("\n🎬 Welcome to YouTube Video Manager!\n")

    while True:
        display_menu()

        try:
            # Use sys.stdout.flush to ensure the prompt appears before input on some terminals
            sys.stdout.flush()
            choice = input("Enter your choice (1-5): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Exiting. Goodbye!\n")
            break

        # Use if/elif instead of match to avoid potential compatibility/terminal quirks
        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            print("\n👋 Thank you for using YouTube Video Manager. Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()
