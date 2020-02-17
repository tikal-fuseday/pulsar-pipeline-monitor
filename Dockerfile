FROM ubuntu:18.04

WORKDIR /  
# Install Python
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 
#   && apt-get install sudo && sudo apt-get install -y nodejs

RUN pip install --upgrade pip -r pipeline-monitor-backend/requirements.txt

# Install NodeJS
RUN apt-get install sudo && sudo apt-get install -y nodejs && sudo apt-get install -y npm && npm install

COPY . .

# WORKDIR frontend

# RUN npm run serve

CMD ["./runAll.sh"]
# CMD ["python3",  "pipeline-monitor-backend/app.py" ]


# Build
# docker build -t flask-tutorial:latest .

# Run
# docker run -d -p 5000:5000 flask-tutorial

# export LC_ALL=C.UTF-8
# export LANG=C.UTF-8