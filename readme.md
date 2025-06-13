apt update
apt install ffmpeg

#runpod setups
cd workspace
git clone
cd whisper
python -m venv venv
source venv/bin/activate

pip install -r req.txt

python app.py