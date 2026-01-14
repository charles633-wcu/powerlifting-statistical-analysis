# Powerlifting Performance Analysis  
**Statistical Analysis of Bodyweight, Wilks Scores, and Competition Lifts**

## Overview

This project analyzes competitive powerlifting performance using data from the **Open Powerlifting Database**. The goal is to understand how **bodyweight relates to strength performance**, how performance differs **across sexes and weight classes**, and how well **bodyweight predicts performance** in each of the three competition lifts: squat, bench press, and deadlift.

Rather than focusing on prediction, this analysis emphasizes **statistical inference**, effect sizes, and interpretability using classical statistical techniques commonly taught in data science and applied statistics courses.

---

## Dataset

- **Source:** Open Powerlifting Database  
- **Population:** Adult (18+) raw (unequipped) competitors  
- **Units:** Kilograms (kg)  
- **Scope:** Standard open weight classes  

### Preprocessing Steps
- Removed attempt-level variables not used for official results
- Filtered to raw (unequipped) competitions
- Removed implausible values (e.g., non-positive bodyweight or totals)
- Restricted to adult competitors
- Retained valid low totals to reflect novice/lightweight performances
- Standardized numeric variables for consistency

The cleaned dataset is saved as:
data/openpowerlifting_cleaned.csv


---

## Research Questions

1. **Wilks Scores by Sex**  
   Is there a statistically significant difference in Wilks scores between male and female competitors?

2. **Total Weight by Weight Class**  
   Does total weight lifted differ across competition weight classes?

3. **Bodyweight and Lift Performance**  
   Is competitor bodyweight correlated with performance in the squat, bench press, and deadlift?

4. **Regression Analysis**  
   How does lift performance change, on average, with increasing bodyweight?

---

## Methods

The following statistical techniques were used:

- **Welch’s Independent-Samples t-Test**  
  Used to compare Wilks scores between male and female competitors, providing robustness to unequal variances.

- **Welch’s One-Way ANOVA**  
  Used to compare total weight lifted across bodyweight classes when homogeneity of variance was violated.

- **Pearson Correlation Analysis**  
  Used to quantify the strength and direction of linear relationships between bodyweight and lift performance.

- **Simple Linear Regression**  
  Used to estimate the expected change in lift performance per 1 kg increase in bodyweight for each competition lift.

Assumptions (normality, variance, linearity) were evaluated using diagnostic plots and statistical tests, with interpretation informed by the large sample size.

---

## Key Findings

- **Sex Differences:**  
  Male competitors exhibited significantly higher Wilks scores than female competitors, with a moderate-to-large effect size, indicating a meaningful difference in relative strength.

- **Weight Classes:**  
  Total weight lifted increased systematically across weight classes, supporting the use of bodyweight categories as meaningful performance groupings.

- **Correlation:**  
  Bodyweight was moderately to strongly correlated with performance in all three lifts, with slightly stronger associations for squat and bench press.

- **Regression:**  
  Bodyweight was a statistically significant predictor of performance:
  - Squat: ~1.8 kg increase per 1 kg bodyweight
  - Bench Press: ~1.3 kg per kg
  - Deadlift: ~1.7 kg per kg  

  Squat and deadlift performance were more strongly influenced by bodyweight than bench press, although bodyweight alone does not fully explain performance variability.

---

## Limitations

- Training history, competitive experience, and technique were not available
- Some competitors lacked age information
- Weight classes were not equally represented
- Large sample size increases statistical power, requiring careful interpretation of practical significance

---


---

## Tools & Libraries

- Python
- pandas
- NumPy
- SciPy
- statsmodels
- matplotlib
- Jupyter Notebook

---

## How to Run

1. Clone the repository
2. Install dependencies
3. Open `analysis.ipynb` in Jupyter
4. Run all cells to reproduce results and figures

---

## Author

**Charles Wang**   
West Chester University

---

## Notes

This project was completed as part of a data science/statistics coursework assignment and is intended to demonstrate applied statistical reasoning, reproducible analysis, and professional data communication.


