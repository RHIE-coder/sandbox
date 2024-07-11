function main()
{
    case "$1" in
        "up")
            echo "Run docker container"
            docker compose -f ../docker-compose/exporter.compose.yml up -d
            echo
            ;;
        "down")
            echo "Docker container shutdown"
            docker compose -f ../docker-compose/exporter.compose.yml down
            echo
            ;;
        *)
            echo "nothing to do - please, check args"
            ;;
    esac
}

main "$@"