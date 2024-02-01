import json
from datetime import datetime
import matplotlib.pyplot as plt
from pytube import YouTube

def load_watch_history(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_video_duration(video_url):
    try:
        yt = YouTube(video_url)
        duration_sec = yt.length
        return duration_sec
    except Exception as e:
        print(f"Error fetching duration for {video_url}: {e}")
        return 0

def process_watch_history(watch_history):
    total_time_seconds = 0
    channel_times = {}
    watched_times = []

    for entry in watch_history:
        time_watched_str = entry['time'][:-1]  # Remove 'Z' at the end
        time_watched = datetime.strptime(time_watched_str, "%Y-%m-%dT%H:%M:%S.%f")
        video_url = entry['titleUrl']
        duration = get_video_duration(video_url)

        total_time_seconds += duration
        watched_times.append((time_watched, total_time_seconds))

        for subtitle in entry.get('subtitles', []):
            channel_name = subtitle['name']
            channel_times[channel_name] = channel_times.get(channel_name, 0) + duration

    total_time_hours = total_time_seconds / 3600  # Convert seconds to hours
    return total_time_hours, channel_times, watched_times

def plot_watch_history(total_time, channel_times, watched_times):
    # Plot total time
    print(f"Total time spent on YouTube: {total_time} seconds")

    # Plot most-watched channels
    sorted_channels = sorted(channel_times.items(), key=lambda x: x[1], reverse=True)
    top_channels = dict(sorted_channels[:5])  # Display top 5 channels
    print("Top 5 most-watched channels:")
    for channel, time in top_channels.items():
        print(f"{channel}: {time} seconds")

    # Plot time distribution
    plt.figure(figsize=(10, 6))
    plt.bar(channel_times.keys(), channel_times.values())
    plt.xlabel('Channels')
    plt.ylabel('Time (seconds)')
    plt.title('Time Distribution Across Channels')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot total watched time over time
    plt.figure(figsize=(10, 6))
    watched_dates, watched_seconds = zip(*watched_times)
    watched_hours = [seconds / 3600 for seconds in watched_seconds]
    plt.plot(watched_dates, watched_hours, label='Total Watched Time (hours)', color='blue')
    plt.xlabel('Date and Time')
    plt.ylabel('Time (hours)')
    plt.title('Total Watched Time Over Time')
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    watch_history_file = "ressources/test.json"
    watch_history_data = load_watch_history(watch_history_file)

    total_time, channel_times, watched_times = process_watch_history(watch_history_data)
    plot_watch_history(total_time, channel_times, watched_times)