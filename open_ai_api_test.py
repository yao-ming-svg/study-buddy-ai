import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set console encoding to UTF-8
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

# Local variables for the template
subject = "Physics"
topic = "Projectile Motion"
notes_or_uploaded_materials = "Lecture 6 – Projectile Motion by Prof. Matthew Jones (uploaded)"
true_or_false = "true"

# Read the template content
with open("video_prompt_template.txt", "r", encoding="utf-8") as file:
    template_content = file.read()

# Replace the template variables with local variables
prompt = template_content.replace("{{subject}}", subject)
prompt = prompt.replace("{{topic}}", topic)
prompt = prompt.replace("{{notes_or_uploaded_materials}}", notes_or_uploaded_materials)
prompt = prompt.replace("{{true_or_false}}", true_or_false)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

# Write output to file to avoid console encoding issues
with open("output.json", "w", encoding="utf-8") as f:
    f.write(response.output_text)

print(response.output_text)