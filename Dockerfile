FROM continuumio/anaconda3:4.4.0
COPY requirements-pip.txt /tmp/requirements-pip.txt
COPY requirements-conda.txt /tmp/requirements-conda.txt
WORKDIR usr/app/
RUN pip install --upgrade pip
RUN python3 -m pip install --ignore-installed  -r /tmp/requirements-pip.txt
RUN conda install  --file /tmp/requirements-conda.txt
CMD python main.py
