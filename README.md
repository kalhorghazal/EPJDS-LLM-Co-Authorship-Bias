# EPJDS-LLM-Co-Authorship-Bias

This repository contains the data collection scripts and analysis code for the paper:

**Title:** "Measuring Biases in AI-Generated Co-Authorship Networks"

**Authors:** Ghazal Kalhor, Shiza Ali and Afra Mashhadi

**DOI:** https://doi.org/10.1140/epjds/s13688-025-00555-9

If you use our data collection scripts and analysis code in your work, please cite our paper:

Kalhor, G., Ali, S., & Mashhadi, A. Measuring biases in AI-generated co-authorship networks. *EPJ Data Sci*. 14, 38 (2025). https://doi.org/10.1140/epjds/s13688-025-00555-9

# Directories

Our scripts are classified into the following folders:

* **Data Collection**: This directory contains the Python scripts we used to collect authors' information, including co-author list, affliation, country, h-index, and citation count from Google Scholar and DBLP. Moreover, it contains the code used for collecting co-authors' names for each author from GPT-3.5 Turbo and Mixtral 8x7B.

* **Gender Detection**: This directory contains the Python script we used to detect the genders of authors and co-authors for both baseline and LLM data, using the `Namsor` API.

* **Ethnicity Detection**: This directory contains the R script we used to detect the ethnicity of authors and co-authors for both baseline and LLM data, using the R package `Rethnicity`.

* **Fairness Analysis**: This directory contains the Python scripts we used to calculate the number of matched co-authors' names for each author and fairness metrics, including demographic parity, predictive equality, conditional demographic parity, and conditional predictive equality.

* **Network Analysis**: This directory contains the Python codes we used to build the baseline and LLM-constructed co-authorship networks. It also includes the script for comparing the structural features of these networks.
