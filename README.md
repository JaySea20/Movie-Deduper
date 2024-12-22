# Movie-Deduper

## Overview
`deduper.py` is a Python script designed to help manage and clean up duplicate media files in a directory. It scans through a specified directory, identifies folders containing multiple files, and prompts the user to select which file to keep while removing the others. This is particularly useful for cleaning up media libraries with redundant or duplicate files.

---

## Features
- Recursively scans a specified directory for files.
- Identifies folders containing multiple files.
- Interactively prompts the user to choose which file to keep.
- Deletes unselected files while retaining the chosen one.
- Automatically ignores common metadata, subtitles, artwork, torrent files, and other non-media files during the deduplication process.

---

## Requirements
- Python 3.x
- Permissions to delete files in the specified directory.

---

## Usage

### 1. Clone or Copy the Script
Save the script as `deduper.py` in a desired location.

### 2. Run the Script
The script requires a directory path as an argument. Use the following command:

```bash
python3 deduper.py <MEDIA_DIR>
```

### Example
If your media files are located in `/home/user/media`, run:

```bash
python3 deduper.py /home/user/media
```

### 3. Interactive Selection
For each folder with multiple files, the script will:
1. List all files in the folder, excluding ignored file types (e.g., `.srt`, `.nfo`, `.jpg`, `.torrent`).
2. Prompt you to select the file to keep by entering the corresponding number.
3. Delete the other files in the folder.

---

## Ignored File Types
By default, the script ignores the following file types:
- Subtitles: `.srt`, `.sub`, `.idx`
- Metadata: `.nfo`, `.xml`, `.json`
- Artwork: `.jpg`, `.png`, `.bmp`
- Torrent files: `.torrent`

You can modify the script to adjust which file types are ignored.

---

## Error Handling
- If the specified directory does not exist, the script will display an error message and exit.
- Invalid inputs during file selection will prompt the user to try again until a valid choice is made.

---

## Example Output
### Input Directory:
```
/media/movies
    ├── Movie1
    │   ├── Movie1-720p.mkv
    │   └── Movie1-1080p.mkv
    ├── Movie2
    │   ├── Movie2-480p.mp4
    │   └── Movie2-1080p.mp4
```

### Script Execution:
```bash
python3 deduper.py /media/movies
```

### Output:
```
Multiple files found in: /media/movies/Movie1
[1] Movie1-720p.mkv
[2] Movie1-1080p.mkv
Select the file to keep (enter the number): 2
Deleting: Movie1-720p.mkv
Keeping: Movie1-1080p.mkv

Multiple files found in: /media/movies/Movie2
[1] Movie2-480p.mp4
[2] Movie2-1080p.mp4
Select the file to keep (enter the number): 2
Deleting: Movie2-480p.mp4
Keeping: Movie2-1080p.mp4
```

---

## Notes
- Ensure you have backups of your files before running the script to prevent accidental data loss.
- This script only works on local files and directories. For remote media libraries, consider syncing them locally first.
- You can customize the ignored file types in the script to suit your specific needs.

---

## License
This script is provided "as is" without warranty of any kind. Feel free to modify and distribute it as needed.

