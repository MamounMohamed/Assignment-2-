#base image
FROM python 
COPY . /project 
WORKDIR /project 
CMD python srcPro.py