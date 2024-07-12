# weather-app


# Weather App

Welcome to my first Tkinter (GUI) project! This weather app was created to display weather information for any city entered by the user. The app uses various APIs and libraries to fetch and display weather data, including temperature, humidity, pressure, wind speed, and a brief description of the weather condition.

## Project Overview

This project is a basic weather application created using Python and the Tkinter library. It fetches weather data using the WeatherAPI and displays it in a user-friendly GUI. The project was developed as a learning exercise and includes some fun elements like random anime images for an engaging user experience.

## Features

- Display current weather conditions for any city.
- Display 7-day weather forecast.
- Display local time and timezone for the entered city.
- Randomly display one of three anime characters with a fun quote(i included this for fun).

## Screenshots

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)


## Images Used

- The weather icons are sourced from [OpenWeather](https://openweathermap.org/).
- Other images are taken from various online sources, including Pinterest.
- Special thanks to all image contributors!

## How to Use

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed:
    ```sh
    pip install tkinter geopy timezonefinder requests pytz pillow
    ```
3. Replace `your_api_key` in the script with your actual WeatherAPI key.
4. Run the `weather_app.py` script:
    ```sh
    python weather_app.py
    ```
5. Enter the name of a city in the search field and press the search button to get the weather information.

## Possible Improvements

- **Error Handling:** Currently, the app does not handle errors for invalid city names. You can improve the app by adding error handling to prompt the user to enter a valid city name if the entered name is invalid.
- **API Key Management:** Ensure you replace the placeholder `your_api_key` with your actual API key for the WeatherAPI service.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for checking out my first Tkinter project! I hope you find it useful and fun. Special thanks to the contributors of the images used in this project.

