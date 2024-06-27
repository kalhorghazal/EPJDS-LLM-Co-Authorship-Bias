# Co-Authorship Bias Paper

This repository contains the analysis code for the paper:

**Title:** "Exploring Biases in Large Language Models through Co-Authorship Analysis"

**Authors:** Ghazal Kalhor, Sonal Yadav, Naima Noor, Noura Alroomi, Shiza Ali and Afra Mashhadi

**DOI:** 

If you use our analysis code in your work, please cite our paper:

Kalhor, G., Yadav, S., Noor, N., Alroomi, N., Ali, S., & Mashhadi, A. (2024). Exploring Biases in Large Language Models through Co-Authorship Analysis. Submitted to *EPJ Data Science*.

# Directories

Our analysis scripts are classified into the following folders:

* **Data Collection**: This directory contains the Python script we used to collect authors' information, including co-author list, affliation, country, h-index, and citation count from Google Scholar using `scholarly` API. Moreover, it contains the code used for collecting co-authors' names, genders, countries, and affiliations for each author from OpenAI using its API.

* **Gender Detection**: This directory contains the Python script we used to detect the genders of authors and co-authors from both Google Scholar and OpenAI, using the `Namsor` API.

* **Ethnicity Detection**: This directory contains the R script we used to detect the ethnicity of authors and co-authors from both Google Scholar and OpenAI, using the R package `Rethnicity`.

* **Fairness Analysis**: This directory contains the Python scripts we used to calculate the number of matched co-authors' names for each author and fairness metrics, including demographic parity, predictive equality, conditional demographic parity, and conditional predictive equality.

* **Network Analysis**: This directory contains the Python codes we used to build the Google Scholar co-authorship network and the LLM-constructed co-authorship network. It also includes the script for comparing the structural features of the two networks.