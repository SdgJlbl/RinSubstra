# this base image works in both CPU and GPU enabled environments
FROM ghcr.io/substra/substra-tools:0.20.0-nvidiacuda11.8.0-base-ubuntu22.04-python3.9

# install dependencies
RUN apt-get update \
 && apt-get -y install r-base
RUN pip3 install sh

# add your algorithm script to docker image
ADD test.R .
ADD python_wrapper.py .

# define how script is run
ENTRYPOINT ["python3", "python_wrapper.py", "--function-name", "run_script"]