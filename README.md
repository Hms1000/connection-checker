# Connection Checker

This is a Python script to check internet connectivity on various devices including VMs, PCs, and containers.

The script uses **ping requests** (ICMP packets) to test network connectivity. It generates logs, which are essential for cybersecurity and troubleshooting.

The tool has been Dockerized and is planned to be integrated into a CI/CD pipeline.

## Purpose

This tool helps users:

- Verify if their internet connection is active.
- Troubleshoot network issues on containers, VMs, and other environments.

---

## Requirements

- Python 3 must be installed to run the script.
- The script runs on a command-line interface (CLI).

---

## Dependencies

 Dependencies will be added to the `requirements.txt` as the script is involves in future


---

## Usage

Run the script from the command line as follows:

```bash

python3 connection-checker.py --target <ip_address_or_url> --packet <int> --output <json_file>
   ```
Where:

- --target <ip_address_or_url>: The IP address or URL to test connectivity against.

- --packet <int>: Number of ping packets to send during the test.

- --output <json_file>: Filename to save the output in JSON format.

To simplify, you can run the script with default arguments:

```bash

python3 connection-checker.py
   ```

## Screenshot

- Here is a screenshot of the tool in action:

- ![Connection Checker Screenshot](images/connection-checker.png)

## Docker
- The script is Dockerized for easy deployment and integration with CI/CD pipelines.

## Logging
- The script produces logs that are helpful for cybersecurity analysis and troubleshooting network issues.

