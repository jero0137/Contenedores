git clone https://github.com/jero0137/Contenedores.git
sudo docker build -t app1:v1 
sudo docker run -d -p 80:80 app1:v1 python3 app.py
