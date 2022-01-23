from booking.booking import Booking

# Command line command
# python3 /Users/joseservin/Automations/Bot/run.py

try:
    with Booking() as bot:
        #a = 2 /0 (testing except clause)
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.enter_destination(destination = input('Where do you want to go? '))
        bot.enter_dates(
            check_in= input('Enter check-in date: '), 
            check_out= input('Enter check-out date: '))
        bot.enter_adults(int(input('Enter number of adults: ')))
        bot.search()
        bot.apply_filtrations()
        #print(len(bot.report_results())) # should return 25
        bot.refresh() # work-around to let Bot pull data in correct order
        bot.report_results() 
    
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the Bot from the command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Driver path most likely in /usr/local/bin/chromedriver\n'
        )
    else:
        raise
