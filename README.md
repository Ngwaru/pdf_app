📄 PDF App
PDF App is a lightweight Python-based web application designed to merge multiple PDF files into a single document. It provides a simple interface for uploading PDFs and combines them seamlessly using Flask and PyPDF2. The project also includes a Jupyter notebook for experimenting with PDF merging and a Docker setup for containerized deployment.

🚀 Features
- Merge PDFs: Upload multiple PDF files and merge them into one.
- Web Interface: Simple Flask-powered UI for easy interaction.
- Notebook Support: Includes PdfMerge.ipynb for interactive testing.
- Dockerized: Ready-to-run Dockerfile for container deployment.

🛠️ Installation
Prerequisites
- Python 3.8+
- pip
- Docker (optional)
Clone the Repository
git clone https://github.com/Ngwaru/pdf_app.git
cd pdf_app


Install Dependencies
pip install -r requirements.txt



🧪 Usage

Run Locally
python app.py


Visit http://localhost:5000 in your browser to access the app.
Run with Docker
docker build -t pdf_app .
docker run -p 5000:5000 pdf_app



📂 Project Structure
pdf_app/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── Dockerfile               # Docker configuration
├── PdfMerge.ipynb           # Jupyter notebook for PDF merging
├── app.py                   # Flask application
├── requirements.txt         # Python dependencies


📚 Technologies Used
- Python
- Flask
- PyPDF2
- pdf2docx
- Docker
- Jupyter Notebook

🙌 Contributing
Feel free to fork the repository and submit pull requests. Issues and suggestions are welcome!

📄 License
This project is open-source. License details to be added.

