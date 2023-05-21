# Telegram nutrition bot

This is a Telegram bot built using the `aiogram` library. It calculates the daily calorie intake. All calculations are made according to the Harris-Benedict equation. Harris-Benedict principle is a method used to estimate an individual's basal metabolic rate (BMR). The estimated BMR value may be multiplied by a number that corresponds to the individual's activity level, the resulting number is the approximate daily kilocalorie intake to maintain current body weight. The Harris-Benedict equation may be used to assist weight loss.

Note that the Harris-Benedict formula cannot be apply to very obese people (the formula overestimates their actual caloric needs) and very muscular people (the formula underestimates their actual needs). The formula can be used to calculate calories for persons over 18 years of age. However, the calculations using the Harris-Benedict equation are an excellent starting point, its performance can form the basis of an effective and balanced diet, it allows you to assess your energy needs, to review and adjust the diet in order to ultimately achieve those parameters that everyone considers for to be as acceptable as possible.

## Prerequisites

- Python 3.6 or higher
- Required Python packages (specified in `requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Change into the project directory:

   ```bash
   cd your-repo
   ```

## Configuration

1. Obtain a bot token from the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

2. Open the `README.md` file and replace `'YOUR_BOT_TOKEN'` with your actual bot token in the following line:

   ```python
   bot = Bot(token='YOUR_BOT_TOKEN')
   ```

## Usage

1. Run the bot:

   ```bash
   python main.py
   ```

2. Open Telegram and start a conversation with your bot.

## Functionality

The bot provides the following commands and features:

- `/start` - Starts the conversation and prompts the user to select an action.
- `info` - Displays some information to the user.
- `calculate` - Initiates the calculation process. The user will be prompted to provide various inputs such as gender, goal, weight, height, age, and activity level.
- After entering all the required information, the bot will calculate and display the result.
- The user can choose to redo the calculation or perform other actions using the provided buttons.

## File Structure

The project structure is as follows:

```
├── bot.py                # Main bot script
├── keyboards
│   └── client_kb.py      # Keyboard layout definitions
├── other.py              # Utility functions and data
└── README.md             # Project README
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a pull request with your improvements or suggestions.

## Acknowledgments

This bot was created using the `aiogram` library.

If you have any questions or need further assistance, please contact Mykhailo Kafka mykhailokafka@gmail.com
