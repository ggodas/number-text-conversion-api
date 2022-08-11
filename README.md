# Api number encoder

## Requirements
To test the follow api please ensure which you have the docker installed and running.

## Running the application tests
Before tor run the application unit tests, please check if you docker is installed and running
```sh
cd number-text-conversion-api
# just to ensure that the file has execution permission
chmod +x start_tests.sh
./start_tests.sh
```

## Running the api
```sh
cd number-text-conversion-api
# just to ensure that the file has execution permission
chmod +x build_app_docker.sh
# Build the docker image
./build_app_docker.sh

chmod +x start_app.sh
# Starting the service
./start_app.sh
```

Open your browser and paste the follow link to access the swagger
http://localhost:8000/docs

## Encoding a number
Put the access the follow link to encode a number
http://localhost:8000/api/encoder/12345678
```sh
{
    encoded_value: "vGFO**"
}
```
You can change the number encode others numbers

## Decoding a text
We can decode the results of above api using the follow api
http://localhost:8000/api/decoder/vGFO**
```sh
{
    decoded_value: 12345678
}
```
