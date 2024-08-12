# Spotify Watchtime Automation Bot

### Overview

This Python script is designed to automate Spotify account creation and play tracks to simulate watchtime using Selenium WebDriver. The bot opens multiple browser windows, each logging into a different Spotify account, and plays a specific album or track. The number of browser windows and iterations is customizable based on user input.

### Features

- **Automated Account Creation:** Randomly generates email addresses, passwords, and personal details to create new Spotify accounts.
- **Incognito Mode:** Runs the browser in incognito mode to avoid storing any session data.
- **Multi-Threaded Execution:** Opens multiple browser windows in parallel, allowing for simultaneous account creation and track play.
- **Randomized Details:** Uses randomization for user details to ensure variability in account creation.
- **Customizable Execution:** Users can specify the number of iterations (how many times the process should run) and the number of browser windows to open per iteration.

### Dependencies

- **Python 3.x**
- **Selenium**
- **Pandas**
- **Faker**
- **chromedriver_autoinstaller**

### Installation

1. **Install Python 3.x:** Ensure that Python 3.x is installed on your system.
2. **Install Required Libraries:** Run the following command to install the necessary Python libraries:
    ```bash
    pip install selenium pandas faker chromedriver-autoinstaller
    ```
3. **Clone the Repository:** Download or clone this repository to your local machine.

### Usage

1. **Run the Script:**
    ```bash
    python spotify_watchtime_bot.py
    ```
2. **Input Parameters:** When prompted, enter the number of iterations and the number of browser windows to open for each iteration.

### How It Works

1. **Initialization:** The script initializes the Chrome WebDriver in incognito mode using the `chromedriver_autoinstaller`.
2. **Account Creation:** For each browser window, the bot generates a random email, password, and personal details (like name and date of birth) using the `Faker` library.
3. **Track Play:** After account creation, the bot navigates to a specific Spotify album and begins playing tracks to simulate watchtime.
4. **Multi-Threading:** The bot uses Python's `threading` module to handle multiple browser windows simultaneously, improving efficiency and speed.
5. **Closing the Browser:** After the specified duration, the browser windows close automatically.

### Customization

- **Album URL:** The URL of the Spotify album or track can be changed by modifying the `url` variable in the script.
- **Playback Duration:** Adjust the `time.sleep` value towards the end of the `selenium_task` function to change the playback duration.

### Notes

- This bot is designed for educational purposes. Use responsibly and ensure compliance with Spotify's terms of service.
- Selenium WebDriver requires a compatible version of ChromeDriver; `chromedriver_autoinstaller` ensures that the correct version is automatically installed.

### License

This project is open-source and licensed under the MIT License.

### Disclaimer

Automating account creation or using bots to manipulate services such as Spotify may violate terms of service. This script is provided for educational purposes only, and the author assumes no liability for any misuse.
