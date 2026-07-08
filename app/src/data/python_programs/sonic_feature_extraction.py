from pathlib import Path
import pandas as pd
import essentia.standard as es

def extract_sonic_features(input_csv_path, output_csv_path, wav_directory_path):
    df = pd.read_csv(input_csv_path)
    
    sonic_features_data = {
        'bpm': [], 'danceability': [], 'onset_rate': [],
        'average_loudness': [], 'dynamic_complexity': [],
        'mood_happy': [], 'mood_sad': [], 'mood_aggressive': [], 'mood_party': [],
        'acousticness': [], 'electronicness': [], 'instrumentalness': []
    }
    
    for index, row in df.iterrows():
        if row['song_download_status'] != 'Success' or row['wav_filename'] == 'None':
            print(f"Skipping feature extraction for row {index}: No valid WAV file. Assigning NA values.")
            for key in sonic_features_data.keys():
                sonic_features_data[key].append(None)
            continue
            
        wav_filepath = Path(wav_directory_path) / row['wav_filename']
        
        if not wav_filepath.exists():
            print(f"Warning: File {wav_filepath.name} expected but not found in the wav_downloads directory. Assigning NA values.")
            for key in sonic_features_data.keys():
                sonic_features_data[key].append(None)
            continue
        
        try:
            sonic_features, features_frames = es.MusicExtractor(lowlevelStats=['mean'], rhythmStats=['mean'], tonalStats=['mean'])(str(wav_filepath))
            sonic_features_data['bpm'].append(sonic_features['rhythm.bpm'])
            sonic_features_data['danceability'].append(sonic_features['rhythm.danceability'])
            sonic_features_data['onset_rate'].append(sonic_features['rhythm.onset_rate'])
            sonic_features_data['average_loudness'].append(sonic_features['lowlevel.average_loudness'])
            sonic_features_data['dynamic_complexity'].append(sonic_features['lowlevel.dynamic_complexity'])
            sonic_features_data['mood_happy'].append(sonic_features['highlevel.mood_happy.probability'])
            sonic_features_data['mood_sad'].append(sonic_features['highlevel.mood_sad.probability'])
            sonic_features_data['mood_aggressive'].append(sonic_features['highlevel.mood_acoustic.probability'])
            sonic_features_data['mood_party'].append(sonic_features['highlevel.mood_party.probability'])
            sonic_features_data['acousticness'].append(sonic_features['highlevel.mood_acoustic.probability'])
            sonic_features_data['electronicness'].append(sonic_features['highlevel.mood_electronic.probability'])
            sonic_features_data['instrumentalness'].append(sonic_features['highlevel.voice_instrumental.probability'])
        except Exception as e:
            print(f"Error processing {wav_filepath.name}: {e}. Assigning NA values.")
            for key in sonic_features_data.keys():
                sonic_features_data[key].append(None)

    for column_name, data_list in sonic_features_data.items():
        df[column_name] = data_list
        
    df.to_csv(output_csv_path, index=False)
    print(f"\nSuccessfully extracted sonic features from Essentia and saved dataset to{output_csv_path}")

program_dir = Path(__file__).parent
csv_directory = program_dir.parent / "csv_files"
wav_download_directory = program_dir.parent / "wav_downloads"

input_csv_path = csv_directory / "music_preferences_and_feelings_survey_data_master_song_download.csv"
output_csv_path = csv_directory / "music_preferences_and_feelings_survey_data_master_sonic_feature_calculations.csv"

extract_sonic_features(input_csv_path, output_csv_path, wav_download_directory)