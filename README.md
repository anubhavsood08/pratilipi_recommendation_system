# 📖 Pratilipi Story Recommendation System

🚀 **A machine learning-based recommendation system to predict stories a user is likely to read based on past interactions.**  

---

## 📌 Table of Contents
- [📖 Project Overview](#-project-overview)
- [📂 Dataset Description](#-dataset-description)
- [📊 Data Analysis](#-data-analysis)
- [🛠 Technologies Used](#-technologies-used)
- [💡 Model Used](#-model-used)
- [📌 How to Run the Project](#-how-to-run-the-project)
- [🌍 Running the Streamlit App](#-running-the-streamlit-app)
- [📊 Model Evaluation](#-model-evaluation)
- [🚀 Future Improvements](#-future-improvements)

---

## 📖 Project Overview
The **Pratilipi Story Recommendation System** suggests **5 stories** a user is likely to read based on their **reading history**.  
The project applies **Collaborative Filtering (SVD Algorithm)** to build a personalized recommendation system.

✅ **Goal:** Predict at least **5 stories** each user will read in the future.  
✅ **Train-Test Split:** Used **first 75% of data** for training, remaining **25% for testing**.  
✅ **Output:** A **recommendations.csv** file containing top 5 stories for each user.

---

## 📂 Dataset Description

### **1️⃣ User Interaction Data (`user_interaction.csv`)**
Contains details of user interactions with stories.

| Column Name | Description |
|-------------|------------|
| **user_id** | Unique identifier for users |
| **pratilipi_id** | Unique identifier for stories |
| **read_percentage** | Percentage of the story read (0-100) |
| **updated_at** | Timestamp of interaction |

### **2️⃣ Story Metadata (`metadata.csv`)**
Contains meta-information about the stories.

| Column Name | Description |
|-------------|------------|
| **author_id** | Unique ID of the author |
| **pratilipi_id** | Unique ID of the story |
| **category_name** | Story category (e.g., Romance, Mystery) |
| **reading_time** | Estimated reading time in seconds |
| **updated_at** | Timestamp when metadata was updated |
| **published_at** | Timestamp when the story was published |

---

## 📊 Data Analysis

### 🔍 Key Insights from Data Analysis
1️⃣ **Most users read only a small percentage of stories.**  
2️⃣ **Some stories are much more popular than others.**  
3️⃣ **The "Romance" category is the most read genre.**  
4️⃣ **Users who read more stories tend to read higher percentages.**  

---

## 🛠 Technologies Used

| **Library/Tool** | **Usage** |
|-----------------|---------|
| **Python** | Main programming language |
| **Pandas** | Data handling & processing |
| **NumPy** | Numerical computations |
| **Surprise (SVD)** | Collaborative Filtering Model |
| **Matplotlib & Seaborn** | Data visualization |
| **Streamlit** | Web app for user interaction |

---

## 💡 Model Used
We used **Collaborative Filtering (SVD - Singular Value Decomposition)** from the **Surprise** library.  
- **Matrix Factorization** technique to find hidden patterns in user-story interactions.  
- **Optimized hyperparameters** using GridSearchCV.  
- **Filtered out low-quality data (users with very low read percentages).**  

---

## 📌 How to Run the Project

### 1️⃣ Install Dependencies
First, install required Python libraries.
```sh
pip install -r requirements.txt

## 📌 Train the Model & Generate Recommendations  
Run the following script to **train the recommendation model** and **generate recommendations**.

```sh
python train_model.py
