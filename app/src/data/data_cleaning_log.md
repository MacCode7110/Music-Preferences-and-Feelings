# Data Cleaning Log

Web Developer and Data Researcher: Matthew McAlarney (Web Developer, Data Researcher)

As music_preference_survey_data_master_cleaned is a small dataset and contains open-response survey data that represents human thought and writing, certain steps are manually executed to remove and correct song and artist information using human evaluation and decision. Python scripts are executed to build music_preference_survey_data_master_cleaned to add WAV files and sonic features through Essentia for each song.

## [2026-6-22 - V1] - [Matthew McAlarney - Web Developer, Data Researcher]

- **Target File:** `music_preference_survey_data_master_raw.csv` -> `music_preference_survey_data_master_cleaned_v1.csv`
- **Data Shape Change:** 277 rows * 19 columns -> 269 rows * 3 columns
- **Purpose:** [Initial Quality Sweep - Manual Context Review]

### Steps Executed:

1. **[Removal and Schema Renaming]** Deleted 16 columns and renamed the 3 remaining survey response columns to standard identifiers:
    a. [Song Name] -> [song_name]
    b. [Artist Name] -> [artist_name]
    c. [Open-Ended Response] -> [primary_feeling]
2. **[Removal]** Deleted 1 filler row (Row 1) containing survey question column names [What is your favorite song? Please enter (1) the song name and (2) the corresponding artist name. Please use correct spelling.], [What is the primary feeling that your favorite song creates within you? Please enter only one feeling and use correct spelling.].
3. **[Correction]** Standardized 22 null values to display NA.
4. **[Removal]** Deleted 7 rows each containing all NA values.

## [2026-6-22 - V2] - [Matthew McAlarney - Web Developer, Data Researcher]

- **Target File:** `music_preference_survey_data_master_cleaned_v1.csv` -> `music_preference_survey_data_master_cleaned_v2.csv`
- **Data Shape Change:** 269 rows * 3 columns -> _ rows * 3 columns
- **Purpose:** [Dataset Truncation (Chronological Slicing) - Manual Context Review]
- **Initial Raw Submissions:** 275 total survey responses
- **Methodology:** To maintain an efficient manual data-cleaning workflow and prevent arbitrary selection bias, a Chronological Slicing (First-Come, First-Served) method was applied. The first 85 consecutive survey responses were selected maintaining the original chronological submission order. All subsequent 190 survey responses were excluded from this phase of analysis.
- **Resulting Batch Size:** 85 rows.

### Steps Executed:

1. **[Removal]** Deleted all subsequent 190 survey responses submitted after the first 85 consecutive survey responses according to submission timestamp.

## [2026-6-22 - V3] - [Matthew McAlarney - Web Developer, Data Researcher]

- **Target File:** `music_preference_survey_data_master_cleaned_v2.csv` -> `music_preference_survey_data_master_cleaned_v3.csv`
- **Data Shape Change:** _ rows * 3 columns -> _ rows * 3 columns
- **Purpose:** [Complete Quality Sweep - Manual Context Review]

### Steps Executed:

1. **[Complete Quality Sweep]** Processed remaining rows to remove invalid data and correct information:

    a. [Removal] _ rows deleted because the submitted song, artist and primary feeling information lacks sufficient written context to correct.

    b. [Removal] _ rows deleted because the submitted song and artist information is a duplication of previously corrected song and artist information.

    c. [Removal] _ rows deleted because the submitted song and artist information is connected to insufficient data in Youtube Music.

    d. [Correction] Corrected information in [song_name], [artist_name] and [primary_feeling] columns for _ remaining rows in the sequence.