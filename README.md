# V.I.S.I.O.N

## Virtual Intelligent System for Integration, Optimization, and Networking

### 🏆 Hackathon Achievement

This project was developed for the **Google Cloud x AI Tinkerers Toronto Hackathon - September 2025**

- 🥈 **Runner Up**
- 🎉 **Crowd Favorite**

### About the Project

V.I.S.I.O.N is an intelligent video analysis system that leverages Google Cloud AI services to analyze video content from YouTube links. The system provides:

- **Video Content Analysis**: Deep understanding of both visual and audio content
- **AI-Powered Insights**: Extracts meaningful information from videos using advanced AI models
- **Custom Prompts**: Allows users to specify what they want to analyze in videos
- **File Management**: Automatically organizes project outputs in structured folders
- **Interactive Interface**: User-friendly Streamlit web application

### Features

- 📹 YouTube video analysis with custom prompts
- 🔍 Visual and audio content extraction
- 📝 Automated transcript generation
- 🗂️ Intelligent file organization
- 🤖 Powered by Google Cloud AI Platform and Gemini models

---

## Setup Instructions

### Installation Steps

1. **Create Environment**
2. **Enter Environment**
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**

   ```bash
   choco install ffmpeg
   ```

---

## Usage

### Running the Application

```bash
# Web Interface
streamlit run app.py

# ADK Web Interface
adk web
```

### Using V.I.S.I.O.N

1. Start the application using one of the commands above
2. Create a new session in the web interface
3. **Paste your YouTube video link here**: [YouTube URL]
4. Describe what you want to analyze from the video
5. Let V.I.S.I.O.N process and provide insights

---

## Project Structure

```text
VISION/
├── agent.py              # Main AI agent configuration
├── app.py                # Streamlit web application
├── tools/                # Analysis tools
│   ├── fileEditor.py     # File management utilities
│   └── videoAnalyzer.py  # Video processing and analysis
└── custom_utils/         # Utility functions
    └── prompts/          # AI prompt templates
```