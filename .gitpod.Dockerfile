# This is the Dockerfile used by Gitpod to create the development environment.

FROM gitpod/workspace-full:latest

# Install Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /workspace/
RUN pip install -r /workspace/requirements.txt

# Install Black
RUN pip install black
