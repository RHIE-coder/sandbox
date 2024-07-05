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

그러나 운영 환경에서나 필요하지 테스트 및 개발 환경에서는 필요없으므로 single-node로 구성.

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

## [Usage]

### - Overview

```sh
-------------------------------------

  Usage: ./run.sh { inject | up | logs | down | info | clean | help }

    build:   build compose file that container log volumes have been injected
              - [EXAMPLE] ./run.sh build nginx kibana elasticsearch

    up:      run docker container detached by using compose file
              - [EXAMPLE] ./run.sh up

    logs:    show container logging
              - [EXAMPLE] ./run.sh logs

    down:    docker container shutdown
              - [EXAMPLE] ./run.sh down <arguments> [OR] ./run.sh down --all [OR] down -a

    info:    show filebeat agent-id
              - [EXAMPLE] ./run.sh info

    clean:   delete compose file
              - [EXAMPLE] ./run.sh clean

    help:    print usage
              - [EXAMPLE] ./run.sh help

-------------------------------------
```

### - Running

#### 1. build

현재 가동중인 컨테이너 이름을 인수로 받음.

받게 되면 해당 컨테이너 이름에 해당하는 컨테이너 로그 볼륨들만 가져옴.

만일 전달 받은 컨테이너 이름이 아무것도 없거나 존재하지 않은 컨테이너이면 에러.

```sh
# .env 파일의 BUILD_ARGS에 명시했다면
./run.sh build

# 컨테이너 이름들 직접 넘겨주기 
./run.sh build eth-pos-dev-validator-1 eth-pos-dev-beacon-chain-1 eth-pos-dev-geth-1

# 모든 컨테이너 로그 볼륨들 가져오기
./run.sh build --all
./run.sh build -a
```

#### 2. docker compose up

```sh
./run.sh up
```

> 가동 중인 filebeat에 할당된 uuid 형식의 agent-id가 궁금하다면
> ```sh
> ./run.sh info
> ```

#### 3. docker logs -f <container_name>

```sh
./run.sh logs
```

#### 4. docker compose down

```sh
./run.sh down
```

#### 5. build된 compose 파일지우기

build로 생성된 docker compose 파일 지우기

```sh
./run.sh clean
```

---

# About

## [`.env`]

### - Required

`filebeat`가 동작하는데 필요한 환경변수들

 - `config/filebeat.docker.yml`에 명시됨

```sh
# Example
AGENT_FIELD_ID=client-1
AGENT_NAME=chain
TEMPLATE_NAME=chain-template
TEMPLATE_PATTERN=chain-*
ELASTICSEARCH_HOST=192.168.9.5:9200
```

container 이름 설정

```sh
# Example
CONTAINER_NAME=filebeat
```

### - Optional

`run.sh build` 실행 인자를 안주면 들어가게 되는 인자

```sh
# Example
BUILD_ARGS="eth-pos-dev-validator-1 eth-pos-dev-beacon-chain-1 eth-pos-dev-geth-1"
```

## [Filebeat Registry]

filebeat가 어느 지점까지 읽었는지 기록하는 기록하는 중요한 데이터

실행 시 `.registry`에 저장됨

## [Log 수집 조건 변경]

`config/filebeat.docker.yml`에 들어가서 `processors` 부분을 수정하면 됨

 - [Define processors](https://www.elastic.co/guide/en/beats/filebeat/current/defining-processors.html)

## [커스텀 Agent ID 설정]

환경변수 `AGENT_FIELD_ID`를 수정

## [적용중인 index pattern]

```yaml
index: ${AGENT_NAME}-%{+yyyy.MM.dd}
```
> [주의]
> index pattern은 template에 정의된 pattern의 정규식에 포함되어야 함
> `AGENT_NAME=chain`일 때 index pattern은 `chain-%{+yyyy.MM.dd}`
> 정의된 `TEMPLATE_PATTERN=chain-*`에 포함되므로 정상 동작
> ```


## [프로젝트 구성]

본 프로젝트는 `template/docker-compose.template.yml`의 기반으로 docker compose 파일이 생성되고 `config/filebeat.docker.yml`의 설정에 따라 filebeat가 동작함