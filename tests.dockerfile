FROM python:3.9

RUN wget -O - http://packages.couchbase.com/ubuntu/couchbase.key | apt-key add - && \
    OS_CODENAME=`cat /etc/os-release | grep VERSION_CODENAME | cut -f2 -d=` && \
    echo "deb http://packages.couchbase.com/ubuntu ${OS_CODENAME} ${OS_CODENAME}/main" > /etc/apt/sources.list.d/couchbase.list && \
    apt-get update && apt-get install -y libcouchbase-dev build-essential

RUN pip install requests pytest tenacity passlib[bcrypt] couchbase "fastapi>=^0.79.0"

COPY ./src/app /home/app

ENV PYTHONPATH=/home/app

COPY ./src/app/tests/tests-start.sh /tests-start.sh

RUN chmod +x /tests-start.sh

# This will make the container wait, doing nothing, but alive
CMD ["bash", "-c", "while true; do sleep 1; done"]

# Afterwards you can exec a command /tests-start.sh in the live container, like:
# docker exec -it backend-tests /tests-start.sh
