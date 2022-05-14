FROM ubuntu 
WORKDIR /
RUN apt clean
RUN apt autoclean
RUN apt-get update
RUN apt-get install git-core -y
RUN git clone https://github.com/jero0137/Contenedores.git
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install dash
RUN pip3 install pandas
RUN pip3 install openpyxl 
RUN mv Contenedores/app.py /
RUN mv COntenedores/data.xlsx /
EXPOSE 80
