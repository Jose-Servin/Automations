from DealSearch.DealSearch import Carmax

#inst = Carmax()
#inst.landing_page()

#Introducing context manager
with Carmax() as bot:
    bot.landing_page()
    bot.current_store()
    bot.search_store_button()