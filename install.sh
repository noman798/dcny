PREFIX=$(cd "$(dirname "$0")"; pwd)
cd $PREFIX
pip install -r requirements.txt
cd lib/f42
python setup.py install
