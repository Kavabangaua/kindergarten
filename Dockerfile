FROM alpine
RUN apk add --update python3 py-pip
RUN python3 -m venv webapp
ENV PATH="/webapp/bin:$PATH"
RUN pip3 install Flask
COPY . /app
WORKDIR /app
CMD ["python", "webapp.py"]