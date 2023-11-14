# YouTube Watch Time Tracker

## Overview

This project allows you to analyze and track the total watch time spent on YouTube by processing your YouTube watch history data downloaded from Google Takeout. The provided Python script calculates the total watch time and the number of videos watched based on the extracted information from the watch history JSON file.

## Getting Started

To use this tool, follow these steps:

1. **Download YouTube Watch History Data:**
   - Go to [Google Takeout](https://takeout.google.com/) and select only the YouTube data for download.
   - Once downloaded, extract the contents, and locate the `watch-history.json` file.

2. **Install Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required Python packages using the following command:
     ```bash
     pip install pytube
     ```

3. **Run the Script:**
   - Place the `watch-history.json` file in the [ressources](ressources) folder.
   - Execute the script by running the following command in your terminal:
     ```bash
     python main.py
     ```

## Script Details

### `get_video_duration(video_url)`

- This function uses the `pytube` library to fetch the duration of a YouTube video given its URL.
- If an error occurs during fetching, it prints an error message and returns 0.

### `calculate_total_watch_time(json_data)`

- Iterates through each video entry in the provided JSON data.
- Extracts the video URL and fetches its duration using `get_video_duration`.
- Calculates the total watch time in seconds and converts it to hours.

### `calculate_nb_videos(json_data)`

- Returns the total number of videos in the provided JSON data.

### `main()`

- Specifies the path to the YouTube watch history JSON file (`watch-history.json` by default).
- Loads the JSON data, calculates total watch time and the number of videos, and prints the results.

## Usage

- Run the script using the steps mentioned in the "Getting Started" section.
- The script will display the total watch time and the number of videos watched.

## Note

- If you encounter any issues, ensure that you have the required dependencies installed and that your watch history JSON file is correctly located.

Feel free to contribute or customize the script based on your needs. Happy tracking!
