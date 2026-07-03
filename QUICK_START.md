# ⚡ Quick Start Guide

Get up and running with the Audio-Based Speaker Age Prediction System in under 10 minutes!

---

## 🏃 Speed Run (5 minutes)

### Prerequisites Check
```bash
python --version  # Should be 3.8+
git --version     # Should be installed
```

### Installation (3 commands)
```bash
# 1. Clone the repository
git clone https://github.com/alihashim786/audio-based-age-prediction.git
cd audio-based-age-prediction

# 2. Create & activate virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the Project (1 command)
```bash
jupyter notebook i220554_i220583.ipynb
```

**That's it! 🎉**

---

## 📖 Quick Feature Extraction Example

```python
import librosa
import numpy as np

# Load audio file
audio_path = "sample.mp3"
y, sr = librosa.load(audio_path)

# Extract MFCC features (13 coefficients)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfcc_mean = np.mean(mfccs, axis=1)

# Extract Spectral Contrast (7 features)
spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
spectral_mean = np.mean(spectral_contrast, axis=1)

# Combine features
features = np.concatenate([mfcc_mean, spectral_mean])
print(f"Feature vector shape: {features.shape}")  # (20,)
```

---

## 🎯 Common Use Cases

### Use Case 1: Extract Features from Single Audio
```python
from audio_processor import extract_features

features = extract_features('my_audio.mp3')
print(f"Extracted {len(features)} features")
```

### Use Case 2: Process Multiple Audio Files
```python
import glob

audio_files = glob.glob('audio_folder/*.mp3')
for audio_file in audio_files:
    features = extract_features(audio_file)
    # Process features...
```

### Use Case 3: Train Your Own Model
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load preprocessed data
data = pd.read_csv('preprocessed_features.csv')
X = data.drop('age', axis=1)
y = data['age']

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train
model = RandomForestClassifier(n_estimators=100)
model.fit(X_scaled, y)

# Predict
prediction = model.predict(X_scaled[:1])
print(f"Predicted age: {prediction[0]}")
```

---

## 🔧 Troubleshooting Quick Fixes

### Issue: ModuleNotFoundError
```bash
pip install librosa soundfile
```

### Issue: Audio file won't load
```bash
# Install ffmpeg
# Windows: Download from ffmpeg.org
# Ubuntu: sudo apt install ffmpeg
# Mac: brew install ffmpeg
```

### Issue: Out of memory
```python
# Process in smaller batches
batch_size = 100
for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    # process batch
```

---

## 📚 Next Steps

1. **Explore the Data**: Open `i220554_i220583.ipynb`
2. **Read Documentation**: Check out `README.md`
3. **Try Enhanced Version**: See `Another Attempt/i220554_i220583_2ND_ATTEMPT.ipynb`
4. **Contribute**: Read `CONTRIBUTING.md`

---

## 🆘 Need Help?

- **Documentation**: [`SETUP_GUIDE.md`](SETUP_GUIDE.md) for detailed setup
- **Issues**: [GitHub Issues](https://github.com/alihashim786/audio-based-age-prediction/issues)
- **Email**: muhammadalihashim514@gmail.com
- **LinkedIn**: [Muhammad Ali Hashim](https://www.linkedin.com/in/alihashimraza)

---

## ⭐ Quick Commands Reference

```bash
# Start Jupyter Notebook
jupyter notebook

# Run specific notebook
jupyter notebook i220554_i220583.ipynb

# Convert notebook to Python script
jupyter nbconvert --to script notebook.ipynb

# Install specific package
pip install librosa

# Update all packages
pip install -r requirements.txt --upgrade

# Check installed packages
pip list

# Deactivate virtual environment
deactivate
```

---

## 🎉 You're Ready!

You've successfully set up the Audio-Based Speaker Age Prediction System. Now you can:
- ✅ Extract audio features
- ✅ Train ML models
- ✅ Make predictions
- ✅ Experiment and learn

**Happy Coding! 🚀**

---

<div align="center">

**Questions? Open an [issue](https://github.com/alihashim786/audio-based-age-prediction/issues) or reach out!**

[Back to README](README.md) • [Full Setup Guide](SETUP_GUIDE.md) • [Contributing](CONTRIBUTING.md)

</div>
