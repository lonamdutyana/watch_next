# Movie Recommendation Script

## Overview
This Python script, `watch_next.py`, reads descriptions of different movies from a file named `movies.txt` and returns the title of the most similar movie based on a given description. The script is Dockerized for easy deployment.

## Usage
1. **Install Dependencies**: Before running the Docker container, make sure you have the required dependencies installed. You can do this by installing the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Docker Container**: Start by building and running the Docker container:
    ```bash
    docker build -t movie_recommendation .
    docker run -it movie_recommendation
    ```

3. **Input your Movie Description**: Inside the Docker container, you'll be prompted to enter a description of the movie. Type in your description and press Enter.

4. **Get Movie Recommendation**: The script will analyze the given description and return the title of the most similar movie found in the `movies.txt` file.

## Contributing
Contributions are welcome! If you have ideas to improve the script or encounter any issues, feel free to fork the repository, make your changes, and submit a pull request.

