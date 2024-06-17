import subprocess
import pytest


@pytest.mark.performance
def test_locust_performance():
    # Start the Flask application in a separate process
    flask_process = subprocess.Popen(["flask", "run"])

    try:
        # Run Locust in headless mode with specified number of users and spawn rate
        result = subprocess.run(
            [
                "locust",
                "-f",
                "locustfile.py",
                "--headless",
                "-u",
                "10",  # Number of users to simulate
                "-r",
                "1",  # Spawn rate (users per second)
                "--run-time",
                "1m",  # Run the test for 1 minute
                "--only-summary",
                "--html",
                "report.html",  # Generate HTML report
            ],
            capture_output=True,
            text=True,
        )

        # Print the result
        print(result.stdout)
        print(result.stderr)

        # Check if the test passed based on some criteria, e.g., no failed requests
        assert "Failed Requests" not in result.stdout

    finally:
        # Terminate the Flask application
        flask_process.terminate()
