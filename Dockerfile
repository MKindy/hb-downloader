FROM python:3

VOLUME /data
WORKDIR /app

RUN git clone https://github.com/MayeulC/hb-downloader.git /app && \
    cd /app && \
    git checkout poc-trove && \
    python setup.py install

CMD python /app/hb-downloader.py download

