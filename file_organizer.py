import os
import shutil

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css"],
}


def get_category(extension):
    extension = extension.lower()
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        destination = os.path.join(folder_path, category)
        os.makedirs(destination, exist_ok=True)

        shutil.move(file_path, os.path.join(destination, filename))
        print(f"Moved: {filename} -> {category}")
        moved += 1

    print(f"\n✅ Done! Organized {moved} files.")


def main():
    print("=" * 40)
    print("      Simple CLI File Organizer")
    print("=" * 40)

    folder = input("Enter the folder path to organize: ").strip()
    organize_folder(folder)


if __name__ == "__main__":
    main()