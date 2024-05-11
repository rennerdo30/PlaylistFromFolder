# PlaylistFromFolder

This script allows you to generate a music playlist from all the music files in a directory. It provides a context menu option in Windows Explorer to create a playlist file (`*.m3u`) with the same name as the selected folder.

## Installation

1. **Download Python:** If you don't have Python installed on your system, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Clone or download this repository:** 
   ```bash
   git clone https://github.com/rennerdo30/PlaylistFromFolder.git
   ```

3. **Navigate to the repository directory:** 
   ```bash
   cd music-playlist-generator
   ```

4. **Add context menu entry:**
   - Run the `add_context_menu_entry.bat` script by double-clicking it.
   - This script adds a "Generate Playlist" option to the context menu in Windows Explorer.

5. **Usage:**
   - Right-click on a folder containing music files.
   - Select "Generate Playlist" from the context menu.
   - A playlist file (`*.m3u`) with the same name as the folder will be created inside the folder.

## Requirements

- Windows operating system
- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

