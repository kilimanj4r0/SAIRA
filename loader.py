from llama_index import download_loader

BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")


def load_documents():
    loader = BeautifulSoupWebReader()
    return loader.load_data(urls=[
        'http://campuslife.innopolis.ru/main',
        'http://campuslife.innopolis.ru/handbook2023',
        'http://campuslife.innopolis.ru/clubs',
        'http://campuslife.innopolis.ru/tech_clubs',
        'http://campuslife.innopolis.ru/sport_clubs',
        'http://campuslife.innopolis.ru/hobby_clubs',
        'http://campuslife.innopolis.ru/art_clubs'
        'http://campuslife.innopolis.ru/opportunities',
        'http://campuslife.innopolis.ru/faq',
        'http://campuslife.innopolis.ru/contacts'
    ])
