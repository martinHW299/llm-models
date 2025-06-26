# 🍽️ Nutrition Analysis from Food Images using AI vs. Human Specialist

## 📘 Overview

This project compares the accuracy of two large language models (LLMs) — **GPT-4** and **Gemini Pro** — in estimating nutritional values from real food images, against a **human nutritionist** specialist serving as the ground truth.

The LLMs were tasked with analyzing the same set of images and returning:
- A brief description of the plate
- Total estimations for:
  - Weight (g)
  - Calories (kcal)
  - Proteins (g)
  - Carbohydrates (g)
  - Fats (g)

The nutritionist manually analyzed each image by breaking it down into ingredients and estimating the macro nutritional values for each, which were then summed up per plate.

## 🧪 Objective

The goal is to assess how closely LLMs can match expert human judgment on food nutritional analysis by comparing key macro values across models and ground truth.

## 📊 Methods

- Data Aggregation & Cleaning
- Per-image macro comparison
- Metrics:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
- Visual Analysis (boxplots, bar charts)
- Optional statistical testing (e.g., paired t-tests)

## 📈 Metrics Evaluated

| Macro     | Models Compared |
|-----------|-----------------|
| Weight    | GPT-4 vs GT, Gemini vs GT |
| Calories  | GPT-4 vs GT, Gemini vs GT |
| Proteins  | GPT-4 vs GT, Gemini vs GT |
| Carbs     | GPT-4 vs GT, Gemini vs GT |
| Fats      | GPT-4 vs GT, Gemini vs GT |

## ✅ Outcome

At the end of the project, we aim to determine:
- Which model (if any) is more reliable for estimating nutritional values from real-world food imagery
- Areas where LLMs consistently over- or under-estimate
- How close the best model performs compared to the human ground truth