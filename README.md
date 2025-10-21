# Study Buddy API

A Flask-based API that generates comprehensive study guides using OpenAI's GPT model. The API can process uploaded files (PDF, DOCX, PPTX, TXT) and create personalized study materials.

## Features

- **File Upload Support**: Upload PDF, DOCX, PPTX, and TXT files
- **Template-based Generation**: Uses a structured prompt template for consistent output
- **Study Guide Generation**: Creates comprehensive study materials with:
  - Key concepts and important terms
  - Example questions
  - Practice exams (optional)
- **JSON Output**: Returns structured JSON data

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install flask openai python-docx PyPDF2 python-pptx requests
```

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

Make sure to update the OpenAI API key in `study_buddy_server.py`:

```python
client = OpenAI(api_key="your-api-key-here")
```

## Testing

Run the test script to verify the API is working:

```bash
python test_api.py
```

## File Structure

```
├── study_buddy_server.py    # Main Flask application
├── video_prompt_template.txt # Prompt template for study guide generation
├── test_api.py              # Test script
├── open_ai_api_test.py      # Original test script
└── README.md               # This file
```

## Notes

- The server runs in debug mode by default
- Maximum file upload size is 16MB
- All file processing is done in memory with temporary files
- The API uses OpenAI's GPT-5-mini model for generation
