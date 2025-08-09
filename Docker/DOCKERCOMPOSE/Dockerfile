FROM python:3.11-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN pip install --no-cache-dir -r requirements.txt   
EXPOSE 5000
CMD [ "flask", "run" ]



# Added "--no-cache-dir"  to the pip install command to keep your image smaller, but optional.