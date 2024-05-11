import os
import sys

def create_playlist(directory):
    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return

    # Get folder name
    folder_name = os.path.basename(os.path.normpath(directory))

    # Set playlist filename
    playlist_path = os.path.join(directory, folder_name + ".m3u")

    # Create playlist
    print(f"Creating playlist from files in {directory}...")
    with open(playlist_path, "w", encoding="utf-8") as playlist_file:
        playlist_file.write("#EXTM3U\n")
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".flac"):
                    file_path = os.path.join(root, file)
                    playlist_file.write(file_path + "\n")

    print(f"Playlist created: {playlist_path}")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: python create_playlist.py <directory>")
            sys.exit(1)

        directory = sys.argv[1]
        create_playlist(directory)
    except Exception as e:
        # Catching any exception and printing the error message
        print("An error occurred:", e)
    
    input()
