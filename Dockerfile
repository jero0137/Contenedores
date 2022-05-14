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
RUN pip install flask
RUN cd Contenedores/
EXPOSE 80
