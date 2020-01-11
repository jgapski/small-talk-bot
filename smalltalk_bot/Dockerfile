FROM erlang:alpine

# Set working directory
RUN mkdir /buildroot
WORKDIR /buildroot

# Copy our Erlang test application
COPY ./ smalltalk_bot

# And build the release
WORKDIR smalltalk_bot
RUN rebar3 as prod release

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install vaderSentiment
RUN pip install pyjokes
RUN pip install strsimpy

# Build stage 1
FROM alpine

# Install some libs
RUN apk add --no-cache openssl && \
    apk add --no-cache ncurses-libs

# Install the released application
COPY --from=0 /buildroot/smalltalk_bot/_build/prod/rel/smalltalk_bot /smalltalk_bot

# Expose relevant ports
EXPOSE 8080

CMD ["/smalltalk_bot/bin/smalltalk_bot", "foreground"]
