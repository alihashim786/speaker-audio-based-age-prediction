# Contributing to Audio-Based Speaker Age Prediction

First off, thank you for considering contributing to this project! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inclusive environment. By participating, you are expected to uphold this code.

### Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## How Can I Contribute?

### Reporting Bugs 🐛

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

**Bug Report Template:**
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Run '....'
3. See error

**Expected behavior**
What you expected to happen.

**Environment:**
- OS: [e.g. Windows 10, Ubuntu 20.04]
- Python Version: [e.g. 3.8.10]
- Package Versions: [run `pip list`]

**Additional context**
Add any other context about the problem.
```

### Suggesting Enhancements 💡

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the proposed functionality
- Explain why this enhancement would be useful
- List any alternative solutions you've considered

### Contributing Code 🔧

1. **Fork the Repository**
   ```bash
   # Click the 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/audio-age-prediction.git
   cd audio-age-prediction
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. **Make Your Changes**
   - Write clear, commented code
   - Follow the style guidelines below
   - Add tests if applicable

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   # or
   git commit -m "fix: resolve issue with audio loading"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template

## Development Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Steps

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Development Dependencies**
   ```bash
   pip install pytest black flake8 mypy
   ```

4. **Run Tests** (when available)
   ```bash
   pytest tests/
   ```

## Pull Request Process

1. **Update Documentation**
   - Update README.md with details of changes if applicable
   - Update any relevant docstrings

2. **Follow Commit Convention**
   ```
   feat: new feature
   fix: bug fix
   docs: documentation changes
   style: formatting, missing semicolons, etc
   refactor: code restructuring
   test: adding tests
   chore: maintenance tasks
   ```

3. **PR Description Template**
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update

   ## Testing
   Describe the tests you ran

   ## Checklist
   - [ ] My code follows the style guidelines
   - [ ] I have commented my code
   - [ ] I have updated the documentation
   - [ ] My changes generate no new warnings
   - [ ] I have added tests that prove my fix/feature works
   ```

4. **Review Process**
   - At least one maintainer review required
   - All CI checks must pass
   - No merge conflicts

## Style Guidelines

### Python Code Style

Follow PEP 8 guidelines:

```python
# Good
def extract_audio_features(audio_path: str, sample_rate: int = 22050) -> np.ndarray:
    """
    Extract MFCC and spectral features from audio file.
    
    Args:
        audio_path: Path to audio file
        sample_rate: Sampling rate for audio processing
        
    Returns:
        Feature vector as numpy array
    """
    # Implementation
    pass

# Use meaningful variable names
mfcc_features = librosa.feature.mfcc(y=audio, sr=sample_rate)

# Add comments for complex logic
# Normalize features to zero mean and unit variance
scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)
```

### Jupyter Notebook Guidelines

1. **Clear Cell Organization**
   - One logical operation per cell
   - Use markdown cells for explanations

2. **Cell Comments**
   ```python
   # Cell 1: Load Dependencies
   # Cell 2: Load and Explore Data
   # Cell 3: Feature Extraction
   ```

3. **Output Management**
   - Clear outputs before committing (except important visualizations)
   - Use `%%time` for performance-critical cells

### Documentation Style

- Use clear, concise language
- Include code examples where helpful
- Keep line length to 80-100 characters
- Use proper markdown formatting

### Commit Message Guidelines

```
<type>(<scope>): <subject>

<body>

<footer>
```

Example:
```
feat(feature-extraction): add support for mel-spectrogram

Added mel-spectrogram extraction to complement MFCC features.
This provides additional time-frequency information for the model.

Closes #42
```

## Testing Guidelines

### Unit Tests
```python
import pytest
from audio_processor import extract_features

def test_feature_extraction():
    """Test that feature extraction returns correct shape."""
    features = extract_features('test_audio.mp3')
    assert features.shape == (20,)  # 13 MFCC + 7 Spectral Contrast
```

### Integration Tests
- Test end-to-end workflows
- Verify model training pipeline
- Check data preprocessing steps

## Community

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Email**: muhammadalihashim514@gmail.com
- **LinkedIn**: [Muhammad Ali Hashim](https://www.linkedin.com/in/alihashimraza)

### Recognition

Contributors will be recognized in:
- README.md Contributors section
- Release notes
- Project documentation

## Questions?

Don't hesitate to ask questions! You can:
1. Open an issue with the "question" label
2. Reach out via email
3. Connect on LinkedIn

---

Thank you for contributing to make this project better! 🚀

**Happy Coding!** 💻
