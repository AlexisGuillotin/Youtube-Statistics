import json
from pytube import YouTube

def get_video_duration(video_url):
    try:
        yt = YouTube(video_url)
        duration_sec = yt.length
        return duration_sec
    except Exception as e:
        print(f"Error fetching duration for {video_url}: {e}")
        return 0
    
def calculate_nb_videos(json_data):
    return len(json_data)

def calculate_total_watch_time(json_data):
    total_watch_time_seconds = 0

    # Iterate through each video entry in the JSON data
    for entry in json_data:
        if 'subtitles' in entry:
            # Extract the duration from the subtitles (assuming it's available)
            url = entry['titleUrl']
            duration = get_video_duration(url)
            
            # Convert the duration to seconds and add to the total
            total_watch_time_seconds += duration

    # Convert the total watch time to hours
    total_watch_time_hours = total_watch_time_seconds / 3600

    return total_watch_time_hours

def main():
    # Specify the path to your YouTube watch history JSON file
    file_path = 'ressources/watch-history.json'

    try:
        # Load the JSON data
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Calculate the total watch time
        total_watch_time = calculate_total_watch_time(data)

        print(f'Total Watch Time: {total_watch_time:.2f} hours')
        
        # Calculate number of videos watched
        nb_videos = calculate_nb_videos(data)
        print(f"Nombre de vidéos regardées: {nb_videos}")
        
    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()
