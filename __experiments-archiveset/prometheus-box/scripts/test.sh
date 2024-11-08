function main()
{
    case "$1" in
        "run")
            echo "Run container to test"
            docker run -itd --name nginx-test nginx
            echo
            ;;
        "kill")
            echo "Kill container to test"
            docker rm -f nginx-test
            echo
            ;;
        *)
            echo "nothing to do - please, check args"
            ;;
    esac
}

main "$@"