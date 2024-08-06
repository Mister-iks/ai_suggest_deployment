# ai_suggest

`ai_suggest` is a command-line utility that provides command suggestions based on user queries. This project allows users to request Linux command suggestions from their terminal in a simple and quick manner.

## Features

- Suggests commands based on user queries.
- Easy installation via an `install.sh` script.

## Prerequisites

- Python 3.6 or higher
- Python `requests` module

## Installation

### Step 1: Download the Files

Clone the GitHub repository or download the `client.py`, `install.sh`, and `requirements.txt` files manually.

```bash
git clone https://github.com/Mister-iks/ai_suggest_deployment.git
cd ai_suggest_deployment
```

### Step 2: Run the Installation Script

The `install.sh` script installs the required Python packages, copies the `client.py` script to the `/usr/local/bin` directory, and creates an executable. Ensure that the shebang line in `client.py` matches your Python interpreter location (usually `#!/usr/bin/env python3`).

```bash
sudo ./install.sh
```

### Important Note

- **Shebang Line**: Make sure that the shebang line at the top of the `client.py` file points to the correct Python interpreter. If it is different from `#!/usr/bin/env python3`, adjust it accordingly. The `install.sh` script assumes that the shebang line is correct.

### Usage

After installation, you can use `ai_suggest` from any directory in your terminal.

#### Example Command

To get a command suggestion, use:

```bash
ai_suggest "list files in the current directory"
```

## Contribution

Contributions are welcome! If you want to contribute to the project, please submit pull requests or report issues via the GitHub repository.


Thank you for using `ai_suggest`!
If you have any questions or suggestions, feel free to open an issue on GitHub or contact me on Linkedin.
