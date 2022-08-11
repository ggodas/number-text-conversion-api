docker build -f tests.dockerfile -t api-tests .
docker run -d --name api-tests api-tests
docker exec -it api-tests poetry run pytest . "${@}"
docker stop api-tests
docker rm api-tests
