FROM terraopsio/cuda-python:cuda9.2-dev-python3
ENV NUMBAPRO_NVVM=/usr/local/cuda-9.2/nvvm/lib64/libnvvm.so
ENV NUMBAPRO_LIBDEVICE=/usr/local/cuda-9.2/nvvm/libdevice/
ENV PORT 8080
EXPOSE 8080
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --quiet --no-cache-dir -r requirements.txt

COPY . /usr/src/app
ENTRYPOINT ["python3"]
CMD ["app.py"]
