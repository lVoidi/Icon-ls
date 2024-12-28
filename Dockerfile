FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ~/.local/share/fonts

RUN wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/DejaVuSansMono.zip \
    && unzip DejaVuSansMono.zip -d ~/.local/share/fonts \
    && rm DejaVuSansMono.zip

RUN fc-cache -fv

WORKDIR /app

COPY ls.py .
COPY test_ls.py .

ENTRYPOINT ["python3", "/app/ls.py"] 