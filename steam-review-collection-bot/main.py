from service.steam_scraper import get_reviews_steam

get_reviews_steam('positivereviews', 'english', 50, 'review_data_Cyberpunk_2077.json')

get_reviews_steam('negativereviews', 'english', 50, 'review_data_Cyberpunk_2077.json')