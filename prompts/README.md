# Filtered MoralChoice Dataset: "Do not break the law"

This directory contains a filtered and processed subset of the MoralChoice dataset, created for the ECE59500 Final Project.

## Original Source

* **Dataset:** MoralChoice Scenarios
* **Original File:** `moralchoice_high_ambiguity.csv`
* **Repository:** [https://github.com/ninodimontalcino/moralchoice](https://github.com/ninodimontalcino/moralchoice)

## Description

This dataset, **`moralchoice_high_ambiguity_law_prompts.csv`**, is a heavily processed subset of the original `moralchoice_high_ambiguity.csv` file.

It has been modified in two ways:

1.  **Row Filtering:** Contains **only** the rows from the original file where the `generation_rule` column is equal to **"Do not break the law"**.
2.  **Column Selection:** Contains **only** the following three columns from the original file. All other columns have been removed.

## Columns Included

1.  **context**: The context or scenario prompt.
2.  **action1**: The first action choice.
3.  **action2**: The second action choice.