# Prerequisite

## [Filebeat 테스트 환경 설치]
 - docker 기반 테스트 환경 
 - 사전에 docker 설치가 되어있어야 함
 - 8버전은 보안 설정이 default로 되어 있어서 7버전 이용
 - 테스트용이지 운영용이 아님

### - Elasticsearch

#### 이미지 불러오기

```sh
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.11
```

#### 컨테이너 실행

Elasticsearch는 클러스터링으로 여러 node를 가동해 fault-tolerance를 마련함.

그러나 운영 환경에서나 필요하지 테스트 및 개발 환경에서는 필요없으므로 single-node로 구성

```sh
docker run --name elasticsearch --net elastic -d \
-p 9200:9200 -p 9300:9300 \
-e "discovery.type=single-node" \
docker.elastic.co/elasticsearch/elasticsearch:7.17.11
```

### - Kibana

#### 이미지 불러오기

```sh
docker pull docker.elastic.co/kibana/kibana:7.17.11
```

#### 컨테이너 실행

```sh
docker run --name kibana --net elastic -d \
-p 5601:5601 \
-e "ELASTICSEARCH_HOSTS=http://elasticsearch:9200" \
docker.elastic.co/kibana/kibana:7.17.11
```
----

# Getting Started

## [Filebeat 이미지 받기]

```sh
docker pull docker.elastic.co/beats/filebeat:7.17.11
```