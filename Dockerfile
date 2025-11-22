# 1️⃣ # A Dockerfile is a text document that contains all the commands
# a user could call on the command line to assemble an image.
FROM python:3.13.9-buster

# 2️⃣# Our Debian with python is now installed.
# We create folder named build for our stuff.
RUN mkdir build
WORKDIR /build

# 3️⃣ # Now we just want to our WORKDIR to be /build
COPY . .

# 4️⃣ # FROM [path to files from the folder we run docker run]
# TO [current WORKDIR]
# We copy our files (files from .dockerignore are ignored)
# to the WORKDIR
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ # OK, now we pip install our requirements

EXPOSE 8000

# Instruction informs Docker that the container listens on port 8000
WORKDIR /build/app


# 7️⃣ Ejecutamos la API con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]