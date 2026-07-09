from pathlib import Path
import pandas as pd
import essentia.standard as es

def extract_sonic_features(input_csv_path, output_csv_path, wav_directory_path):
    df = pd.read_csv(input_csv_path)

    sonic_features_data = {
        # Rhythm Group
        'bpm': [], 'danceability': [], 'onset_rate': [],
        # Dynamics Group
        'average_loudness': [], 'dynamic_complexity': [],
        # Spectral and Tonal Group
        'spectral_energy': [], 'chords_changes_rate': [], 'pitch_salience': [], 'spectral_complexity': [],
        # Texture and Timbre Group
        'spectral_centroid': [], 'barkbands_flatness_db': [], 'zerocrossingrate': []
    }
    
    for index, row in df.iterrows():
        if row['song_download_status'] != 'Success' or row['wav_filename'] == 'None' or pd.isna(row['wav_filename']):
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
            sonic_features, _ = es.MusicExtractor(lowlevelStats=['mean'], rhythmStats=['mean'], tonalStats=['mean'])(str(wav_filepath))
            
            # Rhythm Group
            sonic_features_data['bpm'].append(sonic_features['rhythm.bpm'])
            sonic_features_data['danceability'].append(sonic_features['rhythm.danceability'])
            sonic_features_data['onset_rate'].append(sonic_features['rhythm.onset_rate'])
            
            # Dynamics Group
            sonic_features_data['average_loudness'].append(sonic_features['lowlevel.average_loudness'])
            sonic_features_data['dynamic_complexity'].append(sonic_features['lowlevel.dynamic_complexity'])
            
            # Spectral and Tonal Properties Group
            sonic_features_data['spectral_energy'].append(sonic_features['lowlevel.spectral_energy.mean'])
            sonic_features_data['chords_changes_rate'].append(sonic_features['tonal.chords_changes_rate'])
            sonic_features_data['pitch_salience'].append(sonic_features['lowlevel.pitch_salience.mean'])
            sonic_features_data['spectral_complexity'].append(sonic_features['lowlevel.spectral_complexity.mean'])
            
            # Texture and Timbre Group
            sonic_features_data['spectral_centroid'].append(sonic_features['lowlevel.spectral_centroid.mean'])
            sonic_features_data['barkbands_flatness_db'].append(sonic_features['lowlevel.barkbands_flatness_db.mean'])
            sonic_features_data['zerocrossingrate'].append(sonic_features['lowlevel.zerocrossingrate.mean'])
            
        except Exception as e:
            print(f"Error processing {wav_filepath.name}: {e}. Assigning NA values.")
            for key in sonic_features_data.keys():
                sonic_features_data[key].append(None)

    for column_name, data_list in sonic_features_data.items():
        df[column_name] = data_list
        
    df.to_csv(output_csv_path, index=False)
    print(f"\nSuccessfully extracted sonic features from Essentia and saved dataset to: {output_csv_path}")

program_dir = Path(__file__).parent
csv_directory = program_dir.parent / "csv_files"
wav_download_directory = program_dir.parent / "wav_downloads"

input_csv_path = csv_directory / "survey_data_master_song_download.csv"
output_csv_path = csv_directory / "survey_data_master_sonic_feature_calculations.csv"

extract_sonic_features(input_csv_path, output_csv_path, wav_download_directory)