
# 1. Use an Official Python Runtime as a Parent Image
FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

# 2. Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1        

# 3. Set Work Directory
WORKDIR /app

# 4. Install System Dependencies and sudo
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        sudo \
        passwd \
    && rm -rf /var/lib/apt/lists/*

# 5. Create a Non-Root User and Group with sudo Privileges
RUN addgroup --system appgroup \
    && adduser --system --ingroup appgroup --disabled-password appuser \
    && echo "appuser:test" | chpasswd \
    && echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 6. Install Python Dependencies
# Copy only `requirements.txt` first to leverage Docker's caching mechanism.
COPY requirements.txt .

# Upgrade pip and Install Dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 7. Copy the Rest of the Application Code
COPY . .

# 8. Change Ownership of the Application Directory
RUN chown -R appuser:appgroup /app

# 9. Expose the Port That the App Runs On
EXPOSE 8000

# 10. Install Playwright (if needed)
RUN playwright install

# 11. Define the Default Command to Run the Application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# 12. Switch to the Non-Root User
USER appuser
