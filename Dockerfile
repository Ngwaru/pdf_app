FROM python:3.11
SHELL ["/bin/bash", "-c"]
ADD app.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]