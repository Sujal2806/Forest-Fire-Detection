# Use a stable PyTorch image with CPU support
FROM pytorch/pytorch:latest

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install system dependencies (for OpenCV/PIL etc.)
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install project dependencies
RUN pip install --default-timeout=100 --retries=10 --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
