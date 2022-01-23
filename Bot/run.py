from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.enter_destination(destination='Houston')
    bot.enter_dates(check_in='2022-01-23', check_out='2022-01-29')
    bot.enter_adults(5)
    bot.search()
    bot.apply_filtrations()