conda config --add channels conda-forge
conda config --set channel_priority strict
conda install --file requirements-conda.txt
pip install -r requirements-pip.txt