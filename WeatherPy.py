import requests

exit_statement = True
while exit_statement:

    location = (input('Please enter your city or zip code: '))
    # Location is entered by user
    api_key = 'd8e9087864e810b7b8e99d42a56ff3dc'

    if location is int:
        try:
            response = requests.get(
                    f'http://api.openweathermap.org/data/2.5/weather?zip={location}&units=imperial&appid={api_key}')
        except requests.ConnectionError:
            print('Connection Error')
            continue

    else:
        try:
            response = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')
        except requests.ConnectionError:
            print('Connection Error')
            continue

    # Differentiating between zip input and city input
    try:
        data = response.json()  # Raw JSON data from API

        weather = data['weather']
        weather_dict = weather[0]
        description = (weather_dict['description']).title()
    # Weather description data from dict in data

        main_dict = data['main']
        temp = (main_dict['temp'])
        feels_like = (main_dict['feels_like'])
    # Temp and feels-like information from 'main' dict in data

        clouds_dict = data['clouds']
        clouds_percentage = clouds_dict['all']

        if clouds_percentage >= 10 < 50:
            clouds = 'Partly Cloudy'
        elif clouds_percentage >= 50:
            clouds = 'Mostly Cloudy'
        else:
            clouds = 'Clear Skies'
    # Defining cloud cover by %

        wind_dict = data['wind']
        wind_speed = wind_dict['speed']

        if wind_speed >= 5 < 20:
            wind = 'Breezy'
        elif wind_speed >= 20:
            wind = 'Windy'
        else:
            wind = 'Calm'
    # Defining wind speed by mph

    except KeyError:
        print('Input Error! Try Again:\n')
        continue

    print(response)
    #  ^ un-comment to output raw JSON data
    print(f"\nHere's the weather in {location}:\n")
    print(f'\nIt is currently {temp} degrees fahrenheit,')
    print(f'Feels Like: {feels_like}')
    print(f'{description}')
    print(f'Cloud Cover: {clouds}')
    print(f'Wind Speed: {wind}, {wind_speed} mph\n')

    choice = input("If you would like to enter another location, press Y \nIf you would like to quit, press N: \n"
                   ).upper()
    if choice == "Y":
        exit_statement = True
        continue
    elif choice == "N":
        exit_statement = False
        break
