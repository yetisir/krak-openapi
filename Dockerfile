FROM openapitools/openapi-generator-cli:v4.3.0

RUN apk --update add git less openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

COPY openapi.yml .

