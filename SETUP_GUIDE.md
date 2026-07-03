# 📚 Complete Setup Guide

This guide will walk you through setting up the Audio-Based Speaker Age Prediction system on your local machine.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation Steps](#installation-steps)
- [Dataset Setup](#dataset-setup)
- [Running the Project](#running-the-project)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, Ubuntu 18.04+, macOS 10.14+
- **RAM**: 4GB (8GB recommended for large datasets)
- **Storage**: 10GB free space
- **Python**: 3.8 or higher
- **Internet**: Required for downloading dependencies

### Recommended Specifications
- **RAM**: 16GB
- **Storage**: 20GB+ SSD
- **CPU**: Multi-core processor for faster processing
- **GPU**: Optional, but beneficial for deep learning models

---

## Installation Steps

### Step 1: Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **Important**: Check "Add Python to PATH"
4. Verify installation:
   ```bash
   python --version
   ```

#### macOS
```bash
# Using Homebrew
brew install python@3.9

# Verify
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3.9 python3-pip python3-venv

# Verify
python3 --version
```

### Step 2: Clone the Repository

```bash
# Using HTTPS
git clone https://github.com/alihashim786/audio-age-prediction.git

# Or using SSH
git clone git@github.com:alihashim786/audio-age-prediction.git

# Navigate to project directory
cd audio-age-prediction
```

### Step 3: Create Virtual Environment

#### Why Use Virtual Environment?
- Isolates project dependencies
- Prevents conflicts with other projects
- Easy to reproduce environment

#### Create and Activate

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# You should see (venv) in your command prompt
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# You should see (venv) in your terminal
```

### Step 4: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# This may take 5-10 minutes depending on your internet speed
```

#### Verify Installation
```bash
pip list
```

You should see packages like:
- librosa
- numpy
- pandas
- scikit-learn
- matplotlib

### Step 5: Install Jupyter Notebook (if not included)

```bash
pip install jupyter notebook

# Verify
jupyter --version
```

---

## Dataset Setup

### Option 1: Using Existing Dataset (Recommended)

The repository includes dataset metadata files. Audio files are large and not included in the repo.

#### If You Have the Audio Files:

1. **Organize Training Data**
   ```
   audio-age-prediction/
   ├── cv-valid-train/
   │   ├── sample-000000.mp3
   │   ├── sample-000001.mp3
   │   └── ... (15,004 files)
   ```

2. **Organize Test Data**
   ```
   audio-age-prediction/
   ├── cv-valid-test/
   │   ├── sample-000000.mp3
   │   ├── sample-000001.mp3
   │   └── ... (4,000 files)
   ```

### Option 2: Download Common Voice Dataset

If you don't have the audio files:

1. Visit [Common Voice by Mozilla](https://commonvoice.mozilla.org/en/datasets)
2. Download the dataset for your language
3. Extract relevant audio files matching the CSV metadata
4. Place files in appropriate directories

### Option 3: Use Sample Data

For testing purposes, you can work with a subset:

```bash
# Create sample directories
mkdir -p cv-valid-train cv-valid-test

# Use first 100 samples for quick testing
# (You'll need to modify the code to work with smaller dataset)
```

---

## Running the Project

### Method 1: Using Jupyter Notebook (Recommended)

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   
2. **Open in Browser**
   - Jupyter will open in your default browser
   - Navigate to `i220554_i220583.ipynb`
   
3. **Run Cells**
   - Click on a cell
   - Press `Shift + Enter` to run
   - Or use "Run All" from the menu

4. **For Enhanced Version**
   - Navigate to `Another Attempt (extracted more features)/`
   - Open `i220554_i220583_2ND_ATTEMPT.ipynb`

### Method 2: Using JupyterLab (Modern Interface)

```bash
# Install JupyterLab
pip install jupyterlab

# Start JupyterLab
jupyter lab
```

### Method 3: Using Python Scripts

If you convert notebooks to scripts:

```bash
# Convert notebook to Python script
jupyter nbconvert --to script i220554_i220583.ipynb

# Run the script
python i220554_i220583.py
```

---

## Project Workflow

### 1. Feature Extraction

```python
# This step processes audio files and extracts features
# Expected time: 30-60 minutes for full dataset
# Output: extracted_features.csv
```

### 2. Data Preprocessing

```python
# Normalizes features using StandardScaler
# Expected time: 1-2 minutes
# Output: preprocessed_features.csv
```

### 3. Model Training

```python
# Trains machine learning model
# Expected time: 5-15 minutes
# Output: Trained model (pkl/joblib file)
```

### 4. Prediction

```python
# Makes predictions on test data
# Expected time: 2-5 minutes
# Output: Predictions CSV
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: librosa ImportError
```
ModuleNotFoundError: No module named 'librosa'
```

**Solution:**
```bash
pip install librosa soundfile

# If still fails, install dependencies separately:
pip install numba==0.56.4
pip install librosa
```

#### Issue 2: Audio File Loading Error
```
LibsndfileError: Error opening file
```

**Solutions:**
1. Install additional audio backends:
   ```bash
   pip install audioread
   
   # Windows: Install ffmpeg
   # Download from ffmpeg.org and add to PATH
   
   # Ubuntu/Debian:
   sudo apt install ffmpeg
   
   # macOS:
   brew install ffmpeg
   ```

#### Issue 3: Memory Error
```
MemoryError: Unable to allocate array
```

**Solutions:**
1. Process data in smaller batches
2. Reduce n_mfcc parameters
3. Close other applications
4. Increase system swap/page file

#### Issue 4: Jupyter Kernel Crashes
```
Kernel died, restarting...
```

**Solutions:**
```bash
# Reinstall ipykernel
pip install --upgrade ipykernel

# Create new kernel
python -m ipykernel install --user --name=audio-env
```

#### Issue 5: Slow Performance

**Solutions:**
1. Use smaller dataset for testing
2. Reduce audio sample rate
3. Use fewer MFCC coefficients
4. Enable multiprocessing:
   ```python
   from joblib import Parallel, delayed
   ```

#### Issue 6: CSV File Not Found
```
FileNotFoundError: cv-valid-test.csv
```

**Solution:**
```bash
# Verify you're in the correct directory
pwd  # or cd on Windows

# Check if files exist
ls *.csv  # or dir *.csv on Windows
```

---

## FAQ

### Q1: How long does the entire process take?
**A:** On a typical machine:
- Feature extraction: 30-60 minutes
- Preprocessing: 1-2 minutes
- Training: 5-15 minutes
- Total: ~45-75 minutes

### Q2: Can I use GPU for faster processing?
**A:** The current implementation uses CPU. For GPU acceleration:
```bash
pip install tensorflow  # or pytorch
# Modify code to use GPU-accelerated libraries
```

### Q3: How much disk space do I need?
**A:**
- Audio files: ~8-10 GB
- Dependencies: ~2 GB
- Extracted features: ~500 MB
- Total: ~12-15 GB

### Q4: Can I run this on Google Colab?
**A:** Yes! Upload the notebook to Colab:
```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Upload dataset to Drive
# Run cells normally
```

### Q5: How do I update the project?
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Q6: Can I use my own audio files?
**A:** Yes! Ensure your files:
- Are in MP3 format
- Have consistent structure
- Include metadata CSV with required columns

### Q7: Model accuracy is low. What can I do?
**Try:**
1. Increase training data
2. Add more features
3. Try different ML algorithms
4. Tune hyperparameters
5. Improve data quality

---

## Performance Optimization Tips

### 1. Parallel Processing
```python
from joblib import Parallel, delayed
import multiprocessing

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(
    delayed(process_audio)(file) for file in audio_files
)
```

### 2. Batch Processing
```python
batch_size = 100
for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    process_batch(batch)
```

### 3. Caching
```python
import joblib

# Save processed features
joblib.dump(features, 'features_cache.pkl')

# Load cached features
features = joblib.load('features_cache.pkl')
```

---

## Next Steps

After successful setup:

1. **Explore the Data**
   - Check dataset statistics
   - Visualize feature distributions
   - Analyze age group balance

2. **Experiment**
   - Try different feature combinations
   - Test various ML models
   - Tune hyperparameters

3. **Improve**
   - Add more features
   - Implement cross-validation
   - Create ensemble models

4. **Deploy**
   - Create a simple API
   - Build a web interface
   - Package as a library

---

## Getting Help

If you encounter issues not covered here:

1. **Check GitHub Issues**: [Project Issues](https://github.com/alihashim786/audio-age-prediction/issues)
2. **Email**: muhammadalihashim514@gmail.com
3. **LinkedIn**: [Muhammad Ali Hashim](https://www.linkedin.com/in/alihashimraza)

---

## Additional Resources

- [Librosa Documentation](https://librosa.org/doc/latest/index.html)
- [Scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
- [MFCC Explanation](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
- [Audio Signal Processing](https://www.coursera.org/learn/audio-signal-processing)

---

**Happy Coding! 🎉**

If this guide helped you, please ⭐ the repository!
