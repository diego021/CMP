sudo find . -iname '*.pyc' -delete
sudo docker-compose rm -f
sudo docker-compose down
sudo docker-compose build --no-cache
sudo docker-compose up
