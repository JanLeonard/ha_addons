ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    py3-flask \
	sqlite 

	
# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

# Copy data for add-on

RUN mkdir -p /app
RUN mkdir -p /app/static
RUN mkdir -p /app/templates


COPY app/templates/*.html /app/templates/
COPY app/*.* /app/

RUN chmod a+x /app/run.sh

CMD [ "/app/run.sh" ]