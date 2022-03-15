# Voice Transformation


## Requirement

    * Python 3.7 with pip.
    * Anaconda or Miniconda
    * Virtual Microhpone [Vb-Audio](https://vb-audio.com/Cable/index.htm/)
    * bash 

## Installation

If you're on `Linux`, `Windows` or `Mac`, then setting up should be easy! Simply run the appropriate setup script and it will guide you through the whole process.

#### Linux and Mac

Make `./setup.sh` executable ... (or run it with an appropriate interpreter) ...

```bash
chmod 755 ./setup.sh
```

Execute it: 
```bash
./setup.sh
```

#### Windows

Execute it: 
```bash
.\setup.sh
```

## Manual Install 

Use the package manager [conda](https://www.anaconda.com/) and [pip](https://pip.pypa.io/en/stable/) to install dependency.

Add `conda-forge` channel to conda

```bash
conda config --add channels conda-forge

conda config --set channel_priority strict
```

Install dependancy:

```bash
conda install --file requirements-conda.txt

pip install -r requirements.txt
```

## Usage

```bash
python main_UI.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
