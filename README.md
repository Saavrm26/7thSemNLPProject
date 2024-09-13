Create environment
```sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Start elastic search and kibana
```shell
docker network create elastic
docker run -d --net elastic --name elasticsearch -m 1GB -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false"  elasticsearch:8.15.1
docker container run --name kibana --net elastic -p 5601:5601 kibana:8.15.1
```
