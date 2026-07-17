# Process Book

**Web Developer, Data Researcher, Scratch DJ, Rapper:** Matthew McAlarney

**Technologies:** Python, Pandas, yt-dlp, FFmpeg, WAV, Essentia Audio Analysis, PCA (Principal Component Analysis), Russell's Core Affect Framework

## Overview and Motivation

The **Song Sonics & Feelings** web application was constructed to examine the relationship between song sonics and the mapping of feelings to parametric neurophysiological foundations.

The motivation to develop **Song Sonics & Feelings** was to understand the connection between the sonic qualities of songs and the resulting primary feeling of respondents. Through processing sonic features and mathematically clustering songs within a neurophysiological framework, a *PCA* instance illustrates the level of consistency in which linear combinations of sonic values accurately predict the resulting primary feeling of respondents.

## Related Work

1. **Music Information Retrieval (MIR):** Implementing computational analysis to extract meaningful features from audio signals such as tempo, loudness, and spectral complexity.
2. **Russell's Core Affect Framework (2003):** A highly influential framework that maps feelings to one of four quadrants along two neurophysiological dimensions:
   * **Valence:** The horizontal axis representing the physiological level of positivity (pleasantness) or negativity (unpleasantness).
   * **Arousal:** The vertical axis representing the physiological level of energy, which ranges from low (sleepy/deactivated) to high (excited/activated).

## Research Questions

* How do scalar sonic features such as `bpm`, `danceability`, and `onset_rate` cluster songs together in a *PCA*?
* To what extent do linear combinations of song sonics accurately predict the classification of the respondent's primary feeling through *Russell's Core Affect Framework*?
* Why do some songs such as *My Sacrifice* by *Creed* mathematically cluster in one quadrant according to *PCA* coordinates, yet evoke primary feelings mapping to a different quadrant through *Russell's Core Affect Framework*?

## Data Collection, Cleaning, and Processing Summary

As detailed in *data_methodology_log.md*, the *Song Preference & Feeling Survey* was administered to a targeted 250 full-time employees in the United States through SurveyMonkey from May 28th, 2026 to June 5th, 2026. The *Song Preference & Feeling Survey* required each respondent to answer two questions: (1) What is your favorite song? Please enter (1) the song name and (2) the corresponding artist name. Please use correct spelling. (2) What is the primary feeling that your favorite song creates within you? Please enter only one feeling and use correct spelling. A total of 275 survey responses from full-time employees were collected and stored in `survey_data_master_raw.csv`.

Since `survey_data_master_raw.csv` is a small dataset and contains open-response survey data that represents human thought and writing, steps are manually executed and executed through Python programs to build the succeeding CSV files:

- **V1:** `[Initial Quality Sweep, Manual Context Review, Establish structural base]` $\rightarrow$ `survey_data_master_structural_base.csv`
- **V2:** `[Dataset Truncation (Simple Random Sampling), Python Program Execution, Select representative subset of dataset]` $\rightarrow$ `survey_data_master_sampled.csv`
- **V3:** `[Complete Quality Sweep and Song URL Insertion, Manual Context Review, Remove invalid data and systematically correct information]` $\rightarrow$ `survey_data_master_corrected.csv`
- **V4:** `[Primary Feeling Mapping, Python Program Execution, Map each remaining primary feeling in the [primary_feeling] column to one of the four quadrants established in Russell's Core Affect Framework]` $\rightarrow$ `survey_data_master_primary_feelings_mapped.csv`
- **V5:** `[Song Downloading and WAV Conversion, Python Program Execution, Download each song in the [song_name] column through the corresponding URL in the [youtube_music_url] column and convert to WAV]` $\rightarrow$ `survey_data_master_song_download.csv`
- **V6:** `[Essentia Sonic Feature Extraction, Python Program Execution, Calculate and record 12 sonic scalar values for each of the 45 remaining data rows through accessing the WAV file referenced in the [wav_filename] column]` $\rightarrow$ `survey_data_master_sonic_feature_calculations.csv`
- **V7:** `[Sonic Feature Scalar Standardization, Python Program Execution, Standardize the 12 sonic scalar values for each of the 45 remaining data rows]` $\rightarrow$ `survey_data_master_sonic_feature_standardization.csv`
- **V8:** `[PCA Dimensionality Reduction, Python Program Execution, Compress 12 multi-dimensional standardized sonic features into 2 static spatial dimensions (pca_x and pca_y) for PCA rendering]` $\rightarrow$ `pca_matrix.json`

## Design Evolution

The core visual tool is the **Exploratory PCA Scatter Plot**. 

* **Early Concept:** The initial design aimed to plot raw sonic features against one another, which quickly became cluttered due to the high dimensionality (12 distinct features).
* **Dimensionality Reduction:** Implementing **Principal Component Analysis (PCA)** allowed us to reduce those 12 dimensions down to 2 main coordinates ($PC1$ and $PC2$) while retaining the maximum variance in the data.
* **Integrating Psychology:** To make the math intuitive, $PC1$ was mapped to represent the horizontal axis of **Valence** (negative feelings on the left, positive on the right), and $PC2$ was mapped to represent the vertical axis of **Arousal** (low energy at the bottom, high energy at the top).
* **Color-Coding:** Data points are color-coded into four distinct quadrants based on Russell’s Core Affect Framework:
  * 🟨 **Quadrant 1:** High Arousal + Positive Valence
  * 🟥 **Quadrant 2:** High Arousal + Negative Valence
  * 🟦 **Quadrant 3:** Low Arousal + Negative Valence
  * 🟩 **Quadrant 4:** Low Arousal + Positive Valence

## Implementation

The application is built as a highly interactive, responsive web experience deployed on Vercel. 
* **Frontend:** Interactive scatter plot utilizing modern web standards.
* **Interactivity:** A comprehensive, hover-enabled tooltip allows users to explore individual data points, revealing detailed sonic attributes, coordinates, and song metadata.
* **Math Layer:** The alignment of Principal Components to the coordinate plane allows a direct spatial overlay of mathematical song similarities on top of emotional quadrants.

## Analysis and Findings

The exploratory visualizer successfully demonstrates that songs with similar sonic properties group together. However, a fascinating cognitive gap was identified:

> **The Sonic vs. Emotional Disconnect**
> A subset of songs is associated with a Primary Feeling mapping to a Core Affect Quadrant that differs from its mathematical spatial cluster in the Exploratory PCA. 
> 
> *Example:* **My Sacrifice** by Creed is emotionally associated with **Core Affect Quadrant 1** (High Arousal + Positive Valence), yet its mathematical sonic profile causes it to cluster in **Quadrant 3** (Low Arousal + Negative Valence). 

This highlights that human emotional response to music is not purely a product of raw physical sonics; lyricism, nostalgia, cultural context, and personal memory play massive roles in how we process a song's "feeling."

## Limitations

* **Sample Size & Diversity:** The current dataset represents a curated subset of songs and user responses.
* **Linear Assumptions:** PCA is a linear dimensionality reduction technique; it may miss complex, non-linear relationships between certain sonic elements.
* **Subjectivity of Feelings:** Emotional mapping relies on self-reported "Primary Feelings" which vary heavily across different respondent demographics.

## Future Work

* **Expanding the Dataset:** Incorporating a broader catalog of genres, tempos, and global music styles.
* **Non-linear Embeddings:** Experimenting with t-SNE or UMAP to see if non-linear dimensionality reduction yields more emotionally cohesive spatial clusters.
* **Interactive Surveying:** Allowing live users to input their own emotional responses to songs and dynamically updating the database to see how emotional consensus shifts.

## References

* Russell, J. A. (1980). *A circumplex model of affect.* Journal of Personality and Social Psychology.
* Bogdanov, D., et al. (2013). *Essentia: An audio analysis library for music information retrieval.* ISMIR.
* Project Web App: [Song Sonics & Feelings](https://music-preferences-and-feelings.vercel.app/exploratory-pca)