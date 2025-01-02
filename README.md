# Whisper-Python

## Description
A Python API Wrapper that runs OpenAI's Whisper model for speech recognition and transcription in a portable and very simple way.

## Features
- OpenAI's Whisper Features(Transcription and Translate)
- Wrapper REST API using FastAPI

## Prerequisites
- Python 3.7+
- FFmpeg
- PyTorch
- OpenAI Whisper

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/whisper-python.git
cd whisper-python
```
2. create a virtual-environment
```bash
python3 -m venv whisper-python
```
3. change to venv
```bash
source whisper-python/bin/activate
```
4. install required dependecies
```
pip install -r requirements.txt
```
5. install ffmpeg(Linux Example)
```
apt-get install ffmpeg
```
6. run python test file or start a fastAPI server
```bash
#dev
fastapi dev api.py
#prod
fastapi run api.py
```

## Usage

Example in [Teste python file](./teste.py)

### API example

Just call `transcribe` API running on port `:8000` using a multi-part request.
```bash
curl --location 'http://localhost:8000/transcribe' \
--form 'file=@"/example/file.{ogg|mp3}"'
```