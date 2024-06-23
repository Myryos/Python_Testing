# Gudlift Registration

## 1. Why

This project serves as a proof of concept (POC) to demonstrate a lightweight version of our competition booking platform. The goal is to keep the implementation as simple as possible and use user feedback to iterate and improve the platform.

## 2. Getting Started

This project utilizes the following technologies:

- **Python v3.x+**
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**: Flask is chosen over Django because it allows for adding only the necessary components, making it a more lightweight framework.
- **[Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)**: This ensures that the correct packages are installed without interfering with the global Python environment on your machine. Make sure to have this installed globally before proceeding.

## 3. Installation

1. **Clone the repository** and navigate into the project directory.

2. **Set up a virtual environment**:
   - For **Linux/macOS**:
     ```
     python3 -m venv venv
     ```
   - For **Windows (Command Prompt)**:
     ```
     python -m venv venv
     ```
   - For **Windows (PowerShell)**:
     ```
     python -m venv venv
     ```

3. **Activate the virtual environment**:
   - For **Linux/macOS**:
     ```
     source venv/bin/activate
     ```
   - For **Windows (Command Prompt)**:
     ```
     venv\Scripts\activate
     ```
   - For **Windows (PowerShell)**:
     ```
     .\venv\Scripts\Activate
     ```

   You should see the command prompt change to indicate the virtual environment is active. To deactivate, simply run:
   ```
   deactivate
   ```
   This command works for all operating systems, including Windows, macOS, and Linux.

4. **Install required packages**
    ```
    pip install -r requirements.txt
    ```
    If you install new packages, update the requirements.txt file:
    ```
    pip freeze > requirements.txt
    ```
5. **Set the Flask application environment variable to server.py.**
    The method varies by operating system:
    - For Linux/MacOS :
    ```
    export FLASK_APP=server.py
    ```
    - For Windows (Command Prompt):
    ```
    set FLASK_APP=server.py
    ```
    - For Windows (PowerShell):
    ```
        $env:FLASK_APP = "server.py"
    ```
6. **Run the application**
    ``` flask run ```
    or
    ```python -m flask run```
    The app will provide an address you can open in your browser to access the application.

## 4. Current Setup
    The application currently uses JSON files instead of a database to manage data. The main files are:

   - competitions.json: Contains a list of competitions.
   - clubs.json: Contains a list of clubs with relevant information, including accepted email addresses for login.
   
## 5. Testing
    We are utilizing the following tools to enhance our testing:

    - Pytest: A framework that makes it easy to write simple and scalable test cases.
    - Coverage: A tool to show how well the code is tested.
    - Locust: An open-source load testing tool that allows you to define user behavior and performance tests using Python code.

    Run your tests using:
    ```pytest tests/```

    or 

    ``` python -m pytest tests/```

    Measure test coverage using:
    ``` 
        coverage run -m pytest tests/
        coverage report server.py
        coverage xml server.py
    ```
    Run performance tests using Locust:
      - Headless Mode
        For Headless Mode run the commands below :
        ``` cd tests ```
        then :
        ```
            locust --headless -u 10 -r 1 --run-time 1m -L DEBUG --only-summary --csv="reports/locust/locust_result"
        ```
        `--headless: Runs Locust in headless mode.
        `-u 10: Simulates 10 users.
        `-r 1: Spawns 1 user per second.
        `--run-time 1m: Runs the test for 1 minute.
        `--only-summary: Only shows a summary of the results.
        `--csv="reports/locust/locust_result": Generates an csv .

      - Interactive Mode:
        For Interactive Mode run :
        ``` locust ```
        - Open your browser and navigate to `http://localhost:8089`.
        - Configure the number of users and the spawn rate, then start the test.

## 6. Analyzing Result
    If you want to visualize the results more easily, you can use the following scripts: 

    - For coverage :
    ```
        python utils/analyze_coverage.py
    ```
    - For Locust :
    ```
        python utils/analyze_locust_result.py
    ```
By following these steps, you should be able to set up, run, and test the Gudlift registration application effectively.


