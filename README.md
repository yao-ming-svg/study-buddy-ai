# Study Buddy AI Assistant

A Flask-based web application that generates comprehensive study guides using OpenAI's GPT model. The application can process uploaded files (PDF, DOCX, PPTX, TXT) and create personalized study materials with an intuitive web interface.

## Features

- **Modern Web Interface**: Clean, responsive design with drag-and-drop file upload
- **File Upload Support**: Upload PDF, DOCX, PPTX, and TXT files
- **Template-based Generation**: Uses a structured prompt template for consistent output
- **Study Guide Generation**: Creates comprehensive study materials with:
  - Key concepts and important terms
  - Example questions with detailed explanations
  - Practice exams (optional)
- **JSON Output**: Returns structured JSON data
- **Environment Variable Support**: Secure API key management

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yao-ming-svg/study-buddy-ai.git
cd study-buddy-ai
```

### 2. Set Up Environment

Create a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file:
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Edit the `.env` file and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Application
```bash
python study_buddy_server.py
```

The application will be available at `http://localhost:5000`

## Usage

### Starting the Server

```bash
python study_buddy_server.py
```

The server will start on `http://localhost:5000`

### Web Interface

Open your browser and navigate to `http://localhost:5000` to access the modern web interface.

**Features:**
- Clean, professional design with gradient background
- Intuitive form for inputting study guide parameters
- Drag-and-drop file upload with visual feedback
- Real-time loading indicators
- Organized display of study guide results
- Responsive design for mobile and desktop
- Interactive question display with answers and explanations

### API Endpoints

#### 1. Health Check
```bash
GET /health
```

#### 2. Generate Study Guide
```bash
POST /generate-study-guide
```

**Parameters:**
- `subject` (required): Class subject (e.g., "Physics", "Mathematics")
- `topic` (required): Current topic (e.g., "Projectile Motion", "Calculus")
- `include_practice_exam` (optional): Include practice exam (true/false, default: false)
- `files` (optional): Upload files (PDF, DOCX, PPTX, TXT)

### Example Usage

#### Using curl:

```bash
# Without files
curl -X POST http://localhost:5000/generate-study-guide \
  -F "subject=Physics" \
  -F "topic=Projectile Motion" \
  -F "include_practice_exam=true"

# With file upload
curl -X POST http://localhost:5000/generate-study-guide \
  -F "subject=Physics" \
  -F "topic=Projectile Motion" \
  -F "include_practice_exam=true" \
  -F "files=@lecture_notes.pdf"
```

#### Using Python requests:

```python
import requests

# Without files
data = {
    'subject': 'Physics',
    'topic': 'Projectile Motion',
    'include_practice_exam': 'true'
}
response = requests.post('http://localhost:5000/generate-study-guide', data=data)

# With files
files = {'files': open('lecture_notes.pdf', 'rb')}
data = {
    'subject': 'Physics',
    'topic': 'Projectile Motion',
    'include_practice_exam': 'true'
}
response = requests.post('http://localhost:5000/generate-study-guide', data=data, files=files)
```

### Response Format

The API returns a JSON response with the following structure:

```json
{
  "success": true,
  "study_guide": "...", // Complete study guide in JSON format
  "subject": "Physics",
  "topic": "Projectile Motion",
  "include_practice_exam": true,
  "files_processed": 1
}
```

## File Processing

The API can extract text from the following file types:

- **PDF**: Extracts text from all pages
- **DOCX**: Extracts text from all paragraphs
- **PPTX**: Extracts text from all slides
- **TXT**: Reads plain text files

## Configuration

The application uses environment variables for secure configuration. The API key is loaded from the `.env` file:

```python
# In study_buddy_server.py
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
FLASK_ENV=development
FLASK_DEBUG=True
```

**Important**: Never commit your `.env` file to version control. The `.gitignore` file is already configured to exclude it.

## Testing

Run the test script to verify the API is working:

```bash
python test_api.py
```

## File Structure

```
├── study_buddy_server.py    # Main Flask application
├── templates/
│   └── index.html          # Web interface template
├── video_prompt_template.txt # Prompt template for study guide generation
├── open_ai_api_test.py      # API test script
├── sample_output.json       # Example output format
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you've activated your virtual environment and installed dependencies:
   ```bash
   .\venv\Scripts\Activate.ps1  # Windows
   pip install -r requirements.txt
   ```

2. **API Key Error**: Ensure your `.env` file exists and contains a valid OpenAI API key:
   ```bash
   # Check if .env file exists
   ls .env  # Linux/Mac
   dir .env  # Windows
   ```

3. **Unicode Encoding Issues**: The application handles Unicode characters properly. If you encounter encoding issues, ensure your terminal supports UTF-8.

4. **Port Already in Use**: If port 5000 is busy, you can change it in `study_buddy_server.py`:
   ```python
   app.run(host='0.0.0.0', port=5001, debug=True)  # Change port to 5001
   ```

## Notes

- The server runs in debug mode by default
- Maximum file upload size is 16MB
- All file processing is done in memory with temporary files
- The API uses OpenAI's GPT-5-mini model for generation
- Environment variables are loaded automatically from `.env` file
- The application includes comprehensive error handling and logging
