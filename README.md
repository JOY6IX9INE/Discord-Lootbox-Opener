# Discord Lootbox Opener

## Overview

This Python script allows users to automate the process of opening lootboxes in Discord. It leverages the Discord API to send requests for opening lootboxes and processes the responses to determine the outcome. The script is designed to continuously open lootboxes until stopped by the user.

## Features

- **Automatic Lootbox Opening**: The script continuously sends requests to the Discord API to open lootboxes.
- **Response Processing**: It parses the responses from the API to determine the outcome of each lootbox opening.
- **Error Handling**: The script handles rate limiting and unknown errors gracefully, providing informative messages to the user.
- **Colorful Console Output**: ANSI color codes are used to provide colorful and visually appealing console output.

## Prerequisites

- Python 3.x
- [tls_client](https://github.com/DiscordHackWeek/tls_client) library

## Usage

1. Install Python 3.x on your system if you haven't already.
2. Install the `tls_client` library by running `pip install tls_client`.
3. Clone this repository to your local machine.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the script by executing the command `python lootbox_opener.py`.
6. Sit back and watch as the script automatically opens lootboxes in Discord.

## Configuration

- Modify the `headers` dictionary in the script to include your Discord authorization token and any other necessary headers.
- Customize the conditions in the script to match the lootbox items you expect to receive.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the creators and maintainers of the `tls_client` library.
- This project was inspired by the desire to automate mundane tasks in Discord.
