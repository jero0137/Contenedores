cd /home/
apt update
apt install docker-compose -y
apt install git-core -y
git clone https://github.com/jero0137/Contenedores.git
docker build -t app1:v1 Contenedores/
docker run -d -p 8000:80 app1:v1 python3 app.py
