FROM erlang:alpine

# Set working directory
RUN mkdir /buildroot
WORKDIR /buildroot

# Copy our Erlang test application
COPY ./ smalltalk_bot

# And build the release
WORKDIR smalltalk_bot
RUN rebar3 as prod release

# Build stage 1
FROM alpine

# Install some libs
RUN apk add --no-cache openssl && \
    apk add --no-cache ncurses-libs

ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

RUN pip install vaderSentiment
RUN pip install pyjokes
RUN pip install strsimpy
RUN pip install requests

# Install the released application
COPY --from=0 /buildroot/smalltalk_bot/_build/prod/rel/smalltalk_bot /smalltalk_bot

# Expose relevant ports
EXPOSE 8080

CMD ["/smalltalk_bot/bin/smalltalk_bot", "foreground"]
