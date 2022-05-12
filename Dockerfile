FROM ubuntu 
RUN apt update
WORKDIR /
RUN git clone https://github.com/jero0137/Contenedores.git
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install dash
RUN pip3 install pandas
RUN pip3 install openpyxl
COPY data.xlsx /
COPY app.py / 
EXPOSE 80
