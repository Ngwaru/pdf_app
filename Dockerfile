FROM python:3.11
ADD app.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ['streamlit', 'run', 'app.py']