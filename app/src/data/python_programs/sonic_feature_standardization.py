from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler

def standardize_sonic_features(input_csv_path, output_csv_path):
    df = pd.read_csv(input_csv_path)
    
    sonic_features = [
        'bpm', 'danceability', 'onset_rate',
        'average_loudness', 'dynamic_complexity',
        'spectral_energy', 'chords_changes_rate', 'pitch_salience', 'spectral_complexity',
        'spectral_centroid', 'barkbands_flatness_db', 'zerocrossingrate'
    ]
    
    valid_rows = df[sonic_features].notna().all(axis=1)
    df_valid = df[valid_rows].copy()
    
    skipped_count = len(df) - len(df_valid)
    if skipped_count > 0:
        print(f"Observe: Dropped {skipped_count} rows from the dataset due to missing sonic feature data.")

    scaler = StandardScaler()
    scaled_sonic_features_matrix = scaler.fit_transform(df_valid[sonic_features])
    
    scaled_column_names = [f"scaled_{feature}" for feature in sonic_features]
    df_scaled_features = pd.DataFrame(scaled_sonic_features_matrix, columns=scaled_column_names, index=df_valid.index)
    
    df_final = pd.concat([df_valid, df_scaled_features], axis=1)
    
    df_final.to_csv(output_csv_path, index=False)
    print(f"Successfully scaled sonic features. Saved standardized matrix to {output_csv_path}")

program_dir = Path(__file__).parent
csv_directory = program_dir.parent / "csv_files"

input_csv_path = csv_directory / "music_preferences_and_feelings_survey_data_master_sonic_feature_calculations.csv"
output_csv_path = csv_directory / "music_preferences_and_feelings_survey_data_master_sonic_feature_standardization.csv"

standardize_sonic_features(input_csv_path, output_csv_path)