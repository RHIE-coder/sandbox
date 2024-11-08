#!/bin/bash
function loadVar()
{
    export env_file=".env"
    export template_file="./template/docker-compose.template.yml"
    export config_file="./config/filebeat.docker.yml"
    export compose_file="docker-compose.yml"
}

function ensure_envfile()
{
    if [ ! -f "$env_file" ]; then
        echo "[ERROR] $env_file does not exist."
        exit 1
    fi

    source "$env_file"
}

function ensure_templatefile()
{
    if [ ! -f "$template_file" ]; then
        echo "[ERROR] $template_file does not exist"
        exit 1
    fi

}

function ensure_configfile()
{
    if [ ! -f "$config_file" ]; then
        echo "[ERROR] $template_file does not exist"
        exit 1
    fi

}

function ensure_composefile()
{
    if [ ! -f "$compose_file" ]; then
        echo "[ERROR] $compose_file does not exist / need to create first(' build ' command)"
        exit 1
    fi

}

function inject_container_logs()
{
    target_container_name_patterns=("$@")
    if [ ${#target_container_name_patterns[@]} -eq 0 ]; then
        if [[ "$BUILD_ARGS" == "" ]]; then
            echo "[ERROR] No container name patterns specified."
            exit 1
        fi
        read -a target_container_name_patterns <<< "$BUILD_ARGS"
    fi
    if [[ "${target_container_name_patterns[0]}" == "--all" || "${target_container_name_patterns[0]}" == "-a" ]]; then
        cp "$template_file" "$compose_file"
        echo "$template_file file copied directly to $compose_file"
        return
    fi

    container_info=$(docker ps --format '{{.ID}} {{.Names}}' --no-trunc)

    filtered_containers=()
    for pattern in "${target_container_name_patterns[@]}"; do
        matched=false
        while IFS= read -r line; do
            container_id=$(echo "$line" | awk '{print $1}')
            container_name=$(echo "$line" | awk '{print $2}')
            if [[ "$container_name" == "$pattern" ]]; then
                filtered_containers+=("$container_id $container_name")
                matched=true
                break
            fi
        done <<< "$container_info"
        
        if [ "$matched" = false ]; then
            echo "[ERROR] Container with pattern '$pattern' not found."
            exit 1
        fi
    done

    for container in "${filtered_containers[@]}"; do
        echo "Targeting..."
        echo " > $container"
    done

    if [ ${#filtered_containers[@]} -eq 0 ]; then
        echo "[ERROR] No containers matching the specified patterns found."
        exit 1
    fi

    volume_config_text=""

    for container in "${filtered_containers[@]}"; do
        container_id=$(echo "$container" | awk '{print $1}')
        volume_config_text+="      - /var/lib/docker/containers/$container_id:/var/lib/docker/containers/$container_id:ro\n"
    done

    sed -e '/- \/var\/lib\/docker\/containers\/\*\/\*.log/ {
        r /dev/stdin
        d
    }' "$template_file" <<< "$(echo -e "$volume_config_text")" > $compose_file

    echo "Updated YAML file saved as $compose_file"
}

function display_help()
{
    echo "-------------------------------------"
    echo 
    echo "  Usage: $0 { inject | up | logs | down | info | clean | help }"
    echo
    echo "    build:   build compose file that container log volumes have been injected"
    echo "              - [EXAMPLE] $0 build nginx kibana elasticsearch"
    echo
    echo "    up:      run docker container detached by using compose file"
    echo "              - [EXAMPLE] $0 up"
    echo
    echo "    logs:    show container logging"
    echo "              - [EXAMPLE] $0 logs"
    echo
    echo "    down:    docker container shutdown"
    echo "              - [EXAMPLE] $0 down <arguments> [OR] $0 down --all [OR] down -a"
    echo
    echo "    info:    show filebeat agent-id" 
    echo "              - [EXAMPLE] $0 info"
    echo
    echo "    clean:   delete compose file"
    echo "              - [EXAMPLE] $0 clean"
    echo
    echo "    help:    print usage"
    echo "              - [EXAMPLE] $0 help"
    echo
    echo "-------------------------------------"
}

function main()
{
    loadVar
    ensure_envfile
    ensure_templatefile
    ensure_configfile
    case "$1" in
        "build")
            echo "Start injecting container logs"
            echo
            shift # 커멘드 제거
            inject_container_logs "$@"
            ;;
        "up")
            echo "Run docker container"
            ensure_composefile
            docker compose up -d
            echo
            ;;
        "logs")
            echo "Printing log..."
            docker logs -f $CONTAINER_NAME
            ;;
        "down")
            echo "Docker container shutdown"
            ensure_composefile
            docker compose down
            echo
            ;;
        "info")
            echo "Show filebeat agent info"
            docker exec filebeat cat data/meta.json
            ;;
        "clean")
            echo "Remove $compose_file"
            rm -r $compose_file
            ;;
        "help")
            display_help
            ;;
        *)
            display_help
            ;;
    esac
}

main "$@"