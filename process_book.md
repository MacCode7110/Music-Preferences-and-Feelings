# Process Book

**Web Developer, Data Researcher, Scratch DJ, Rapper:** Matthew McAlarney

**Technologies:** Python, Pandas, yt-dlp, FFmpeg, WAV, Essentia Audio Analysis, PCA (Principal Component Analysis), Russell's Core Affect Framework

---

## Overview and Motivation

The **Song Sonics & Feelings** web application was constructed to examine the relationship between song sonics and the mapping of feelings to parametric neurophysiological foundations.

The motivation to develop **Song Sonics & Feelings** was to understand the connection between the sonic qualities of songs and the resulting primary feeling of respondents. Through processing sonic features and mathematically clustering songs within a neurophysiological framework, a *PCA* instance illustrates the level of consistency in which linear combinations of sonic values accurately predict the resulting primary feeling of respondents.

---

## Related Work

1. **Music Information Retrieval (MIR):** Implementing computational analysis to extract meaningful features from audio signals such as tempo, loudness, and spectral complexity.
2. **Russell's Core Affect Framework (2003):** A highly influential framework that maps feelings to one of four quadrants along two neurophysiological dimensions:
   * **Valence:** The horizontal axis representing the physiological level of positivity (pleasantness) or negativity (unpleasantness).
   * **Arousal:** The vertical axis representing the physiological level of energy, which ranges from low (sleepy/deactivated) to high (excited/activated).

---

## Research Questions

* How do scalar sonic features such as `bpm`, `danceability`, and `onset_rate` cluster songs together in a *PCA*?
* To what extent do linear combinations of song sonics accurately predict the classification of the respondent's primary feeling through *Russell's Core Affect Framework*?
* Why do some songs such as *My Sacrifice* by *Creed* mathematically cluster in one quadrant according to *PCA* coordinates, yet evoke primary feelings mapping to a different quadrant through *Russell's Core Affect Framework*?

---

## Data Collection, Cleaning, and Processing Summary

As detailed in *data_methodology_log.md*, the *Song Preference & Feeling Survey* was administered to a targeted 250 full-time employees in the United States through SurveyMonkey from May 28th, 2026 to June 5th, 2026. The *Song Preference & Feeling Survey* required each respondent to answer two questions: (1) What is your favorite song? Please enter (1) the song name and (2) the corresponding artist name. Please use correct spelling. (2) What is the primary feeling that your favorite song creates within you? Please enter only one feeling and use correct spelling. A total of 275 survey responses from full-time employees were collected and stored in `survey_data_master_raw.csv`.

Since `survey_data_master_raw.csv` is a small dataset and contains open-response survey data that represents human thought and writing, steps are manually executed and executed through Python programs to build the succeeding CSV files:

* **V1:** `[Initial Quality Sweep, Manual Context Review, Establish structural base]` $\rightarrow$ `survey_data_master_structural_base.csv`
* **V2:** `[Dataset Truncation (Simple Random Sampling), Python Program Execution, Select representative subset of dataset]` $\rightarrow$ `survey_data_master_sampled.csv`
* **V3:** `[Complete Quality Sweep and Song URL Insertion, Manual Context Review, Remove invalid data and systematically correct information]` $\rightarrow$ `survey_data_master_corrected.csv`
* **V4:** `[Primary Feeling Mapping, Python Program Execution, Map each remaining primary feeling in the [primary_feeling] column to one of the four quadrants established in Russell's Core Affect Framework]` $\rightarrow$ `survey_data_master_primary_feelings_mapped.csv`
* **V5:** `[Song Downloading and WAV Conversion, Python Program Execution, Download each song in the [song_name] column through the corresponding URL in the [youtube_music_url] column and convert to WAV]` $\rightarrow$ `survey_data_master_song_download.csv`
* **V6:** `[Essentia Sonic Feature Extraction, Python Program Execution, Calculate and record 12 sonic scalar values for each of the 45 remaining data rows through accessing the WAV file referenced in the [wav_filename] column]` $\rightarrow$ `survey_data_master_sonic_feature_calculations.csv`
* **V7:** `[Sonic Feature Scalar Standardization, Python Program Execution, Standardize the 12 sonic scalar values for each of the 45 remaining data rows]` $\rightarrow$ `survey_data_master_sonic_feature_standardization.csv`
* **V8:** `[PCA Dimensionality Reduction, Python Program Execution, Compress 12 multi-dimensional standardized sonic features into 2 static spatial dimensions (pca_x and pca_y) for PCA rendering]` $\rightarrow$ `pca_matrix.json`

---

## Design Evolution //

* To 


* **Color-Coding:** Data points are color-coded into four distinct quadrants based on Russell’s Core Affect Framework:
  * 🟨 **Quadrant 1:** High Arousal + Positive Valence
  * 🟥 **Quadrant 2:** High Arousal + Negative Valence
  * 🟦 **Quadrant 3:** Low Arousal + Negative Valence
  * 🟩 **Quadrant 4:** Low Arousal + Positive Valence

---

## Implementation Details //

The application is built as a highly interactive, responsive web experience deployed on Vercel. 
* **Frontend:** Interactive scatter plot utilizing modern web standards.
* **Interactivity:** A comprehensive, hover-enabled tooltip allows users to explore individual data points, revealing detailed sonic attributes, coordinates, and song metadata.
* **Math Layer:** The alignment of Principal Components to the coordinate plane allows a direct spatial overlay of mathematical song similarities on top of emotional quadrants.

---

## Findings

Although the PCA is implemented to spatially locate songs within a quadrant established in Russell’s Core Affect Framework as a result of linear combinations of scaled sonic values, there is a particular subset of songs associated with a Primary Feeling that maps to a different Core Affect Quadrant. Specifically, approximately 64.4% of the songs presented in Exploratory PCA: Mapping Song Sonics & Feelings are associated with a Primary Feeling that maps to a different Core Affect Quadrant. As a greater number of presented songs belong to this subset, the PCA demonstrates that the underlying mathematics used to process sonic values do not always accurately predict the Primary Feeling of a respondent in response to a song. The PCA preparation phases exclude comprehension of human factors such as unique emotional reactivity and cultural influence. When listening to a song, individuals experience a Primary Feeling as a function of not only absorbed sonic qualities, but also unique emotional reactivity, and cultural influence. Subsequently, all three factors require evaluation to understand why individuals experience a Primary Feeling in response to a song. Exploratory PCA: Mapping Song Sonics & Feelings illustrates a plethora of songs that mathematically cluster to one quadrant within Russell’s Core Affect Framework, yet are associated with a Primary Feeling mapping to a different Core Affect Quadrant.

Approximately 10.3% of the subset mathematically cluster to spatial Quadrant 1 of Exploratory PCA: Mapping Song Sonics & Feelings, yet are associated with a Primary Feeling that maps to a different Core Affect Quadrant. Within the selected 10.3% of the subset, Calm Down by Rema, Yes I’m A Mess by AJR, and Aloha Ke Akua by Nahko And Medicine For The People are associated with a Primary Feeling mapping to Quadrant 4. Quadrant 1 and Quadrant 4 are neighbors as they each represent high arousal and positive valence, and low arousal and positive valence. Calm Down by Rema is associated with a Primary Feeling of Calm, Yes I’m A Mess by AJR is associated with a Primary Feeling of Validated, and Aloha Ke Akua by Nahko And Medicine For The People is associated with a Primary Feeling of Hopeful. Considering the PC2 range of the songs, the maximum PC2 coordinate is approximately 1.504, and the minimum PC2 coordinate is approximately 0.057. The three songs mathematically locate to the bottom half of Quadrant 1. As a result, the three songs are within reasonable proximity of Quadrant 4. While the cleaning and processing phases to prepare PCA data exclude understanding of why respondents experienced a Primary Feeling, the PC2 range and coordinate locations may suggest that the sonic values of each song predict certain feelings that are similar to the Primary Feeling of the corresponding respondent when measured through valence and arousal. As for the remaining songs in the subset associated with a Primary Feeling that maps to a different Core Affect Quadrant, approximately 44.8% of the subset mathematically cluster to spatial Quadrant 2, approximately 20.7% of the subset mathematically cluster to spatial Quadrant 3, and approximately 24.1% of the subset mathematically cluster to spatial Quadrant 4.

Considering the complete set of songs presented in the PCA, approximately 68.8% of the songs are associated with a Primary Feeling mapping to Core Affect Quadrant 1. As Quadrant 1 represents high arousal and positive valence, a compelling question emerges as well. Do most survey respondents select a favorite song as a function of experiencing high arousal and positive valence?

---

## Pipeline Limitations

* The survey population is completely bounded to full-time employees in the United States. This constraint creates a sampling selection bias, which structurally omits demographics with different music preferences such as full-time students, part-time students, part-time employees, and retired individuals. Consequently, all data points rendered in the PCA reflect the music preferences of a subset of the full-time employee demographic in the United States rather than a general demographic in the United States.
* The `yt-dlp` Python library is utilized to download and extract compressed audio from YouTube Music. Subsequently, `yt-dlp` uses FFmpeg to transform the compressed audio into an uncompressed WAV file. There is some probability that the subset of selected songs are associated with WAV files containing different levels of distortion. When distortion is present in an uncompressed WAV file, there is also some probability that high-frequency overtones (harmonic distortion), Harmonic-to-Noise Ratio (HNR), and compression of dynamic range manipulate the digital audio signal. As a result, data clustering in the PCA may partially reflect manipulated sonic qualities that do not accurately represent the authentic sonic qualities of some songs.
* By utilizing untampered WAV files through standard recording LPs, standard recording EPs, and singles, the Essentia sonic feature extraction process introduces a systematic production bias. Since standard recording LPs, standard recording EPs, and singles frequently experience differing mastering procedures and structural modifications, the resulting Essentia sonic features represent differences in release format and engineering output as well as the sonic qualities of the songs. Consequently, data clustering in the PCA may partially group songs based on release format and engineering output rather than similar sonic qualities.
* There is some probability that a subset of the selected songs from the full-time employee respondent pool are not accessible in YouTube Music as a result of regional licensing restrictions. Although YouTube Music functions globally, distribution contracts function regionally, which means that the extent of official release accessibility relies on the location of the user. Consequently, data clustering in the PCA may not present songs that are only accessible in YouTube Music to a subset of regions.
* When YouTube Music offers certain standard recording LPs, standard recording EPs, and singles containing songs that also have been altered for secondary initiatives, there is some probability that the audio streamed through this particular subset of standard recording LPs, standard recording EPs, and singles is sourced from altered modifications of the songs. The acquisition of songs from standard recording LPs, standard recording EPs, and singles in YouTube Music also creates a systematic production bias. Consequently, data clustering in the PCA may partially group songs based on engineering output rather than similar sonic qualities.
* When YouTube Music offers certain standard recording LPs, standard recording EPs, and singles, there is some probability that duplicates of these official releases are also accessible. YouTube Music provides duplicates of standard recording LPs, standard recording EPs, and singles when the distributor resends the official release with updated information. There is also some probability that at least one of the duplicates is structurally incorrect and contains songs altered for secondary initiatives. Consequently, data clustering in the PCA may partially group songs based on engineering output rather than similar sonic qualities.

---

## Future Work //

* **Expanding the Dataset:** Incorporating a broader catalog of genres, tempos, and global music styles.
* **Non-linear Embeddings:** Experimenting with t-SNE or UMAP to see if non-linear dimensionality reduction yields more emotionally cohesive spatial clusters.
* **Interactive Surveying:** Allowing live users to input their own emotional responses to songs and dynamically updating the database to see how emotional consensus shifts.

---

## References

* Russell, J. A. (2003). Core affect and the psychological construction of emotion. Psychological Review.
* Bogdanov, D., et al. (2013). *Essentia: An audio analysis library for music information retrieval.* ISMIR.