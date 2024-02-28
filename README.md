# Movie Recommendation Script

## Overview
This Python script, `watch_next.py`, reads descriptions of different movies from a file named `movies.txt` and returns the title of the most similar movie based on a given description. The script is Dockerized for easy deployment.

## Usage
1. **Prepare the Movie Descriptions File**: Create a file named `movies.txt` and add each movie description on a separate line.

2. **Build the Docker Image**: Open your terminal or command prompt and navigate to the directory containing the Dockerfile and the script. Then, run the following command to build the Docker image:
    ```bash
    docker build -t movie_recommendation .
    ```

3. **Run the Docker Container**: Once the Docker image is built, you can run the Docker container using the following command:
    ```bash
    docker run -it movie_recommendation
    ```

4. **Input your Movie Description**: Inside the Docker container, you'll be prompted to enter a description of the movie. Type in your description and press Enter.

5. **Get Movie Recommendation**: The script will analyze the given description and return the title of the most similar movie found in the `movies.txt` file.

## Contributing
Contributions are welcome! If you have ideas to improve the script or encounter any issues, feel free to fork the repository, make your changes, and submit a pull request.


[requirements.txt](https://github.com/lonamdutyana/watch_next/files/14439622/requirements.txt)alabaster==0.7.16
annotated-types==0.6.0
asgiref==3.7.2
Babel==2.14.0
black==23.12.0
blis==0.7.11
catalogue==2.0.10
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
cloudpathlib==0.16.0
colorama==0.4.6
confection==0.1.4
cymem==2.0.8
distlib==0.3.8
docutils==0.20.1
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.7.1/en_core_web_md-3.7.1-py3-none-any.whl#sha256=6a0f857a2b4d219c6fa17d455f82430b365bf53171a2d919b9376e5dc9be032e
en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl#sha256=86cc141f63942d4b2c5fcee06630fd6f904788d2f0ab005cce45aadb8fb73889
filelock==3.13.1
idna==3.6
imagesize==1.4.1
Jinja2==3.1.3
langcodes==3.3.0
MarkupSafe==2.1.5
murmurhash==1.0.10
mypy-extensions==1.0.0
numpy==1.26.4
packaging==23.2
pathspec==0.12.1
platformdirs==4.1.0
preshed==3.0.9
pydantic==2.6.1
pydantic_core==2.16.2
Pygments==2.17.2
requests==2.31.0
smart-open==6.4.0
snowballstemmer==2.2.0
spacey==0.1.1
spacy==3.7.4
spacy-legacy==3.0.12
spacy-loggers==1.0.5
Sphinx==7.2.6
sphinx-rtd-theme==2.0.0
sphinxcontrib-applehelp==1.0.8
sphinxcontrib-devhelp==1.0.6
sphinxcontrib-htmlhelp==2.0.5
sphinxcontrib-jquery==4.1
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.7
sphinxcontrib-serializinghtml==1.1.10
sqlparse==0.4.4
srsly==2.4.8
thinc==8.2.3
tqdm==4.66.2
typer==0.9.0
typing_extensions==4.9.0
tzdata==2023.4
urllib3==2.2.1
wasabi==1.1.2
weasel==0.3.4
