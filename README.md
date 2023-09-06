# CipherScape v0.1 - Real-Time Stock Data Telegram Bot

CipherScape is a Telegram bot that provides real-time stock data. You can interact with it by sending various commands to get information about stocks. This README will guide you through the setup process and explain how to use the bot effectively.

## Prerequisites

Before you can use ElCruzoBot, make sure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/) (Python 3.6 or higher)
- [Telegram](https://telegram.org/) installed on your device
- An internet connection

## Getting Started

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/elcruzo/telegram-bot-1.git
   cd telegram-bot-1
   ```

2. Install the `Python Telegram Bot` Library using `pip`:

   ```bash
   pip install python-telegram-bot
   ```

3. Create a `token.txt` file in the same directory as your bot code and paste your Telegram Bot API token obtained from the [BotFather](https://core.telegram.org/bots#botfather) into this file.

   ```
   your_token_here
   ```

## Usage

To start interacting with CipherScape, follow these steps:

1. Open Telegram and search for your bot using the keywords you provided when creating it in the BotFather.

2. Start a chat with your bot by clicking the "Start" button.

3. You can use the following commands to interact with CipherScape:

   - `/start`: Get a welcome message from the bot.
   - `/help`: View a list of available commands and their descriptions.
   - `/content`: Learn about the videos and books available through ElCruzoBot.
   - `/contact`: Find out how to contact ElCruzo by email.

4. To fetch real-time stock data, use the `/stock` command followed by the stock symbol you want to inquire about. For example, to get the current price of Apple Inc. (AAPL), send `/stock AAPL` to the bot.

## Example

Here's an example of how to use the bot to fetch real-time stock data:

1. Send the command `/stock AAPL` to the bot.

2. The bot will respond with a message like:

   ```
   The current price of AAPL is $XXX.XX!
   ```

## Contributions

Contributions are welcome! If you have ideas for improving CipherScape or want to report issues, please create a GitHub issue or submit a pull request.

## Support

If you encounter any issues or have questions about using ElCruzoBot, feel free to contact me by [email](mailto:ayomideadekoya266@gmail.com)

## License

This project is licensed under the [MIT License](LICENSE).

Enjoy using CipherScape to stay updated on real-time stock data!
