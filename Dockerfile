FROM ghcr.io/ashwinstr/ux-jutsu:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/ashwinstr/UX-jutsu /root/userge
RUN mkdir /root/userge/.bin
WORKDIR /root/userge

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ashwinstr/UX-jutsu/alpha/requirements.txt

CMD ["python3","-m","userge"]

# command to run on container start
CMD [ "bash", "./run" ]
