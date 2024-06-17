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
     ```bash
     python3 -m venv venv
     ```
   - For **Windows (Command Prompt)**:
     ```cmd
     python -m venv venv
     ```
   - For **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     ```

3. **Activate the virtual environment**:
   - For **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - For **Windows (Command Prompt)**:
     ```cmd
     venv\Scripts\activate
     ```
   - For **Windows (PowerShell)**:
     ```powershell
     .\venv\Scripts\Activate
     ```

   You should see the command prompt change to indicate the virtual environment is active. To deactivate, simply run:
   ```bash
   deactivate
   ```
4. **Install required packages**
    ```
    bash
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
    bash
    export FLASK_APP=server.py
    ```
    - For Windows (Command Prompt):
    ```
    bash
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
    You are free to use any testing framework you prefer. The key is to demonstrate the tests you are using. Additionally, include the following tools to enhance your testing:

    - pytest: A framework that makes it easy to write simple and scalable test cases.
    - Coverage: A tool to show how well the code is tested.
    
    To install pytest and coverage, you can add them to your requirements.txt file or install them directly:
    ```pip install pytest coverage```

    Run your tests using:
    ```pytest tests/```

    Measure test coverage using:
    ``` coverage run -m pytest tests/
        coverage report
        coverage xml
    ```
    Run performance tests using Locust:
    ```
        locust --headless -u 10 -r 1 --run-time 1m -L DEBUG --only-summary --csv=locust_result
    ```

## 6. Analyzing Result
    If you want to visualize the results more easily, you can use the following scripts: 

    - For coverage :
    ```
        python analyze_coverage.py
    ```
    - For Locust :
    ```
        python analyze_locust_result.py
    ```
By following these steps, you should be able to set up, run, and test the Gudlift registration application effectively.


