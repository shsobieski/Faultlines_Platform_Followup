def scrape_SotU():
    urls = ['https://www.presidency.ucsb.edu/documents/address-the-state-the-union-delivered-before-joint-session-the-congress-0',
            'https://www.presidency.ucsb.edu/documents/address-the-state-the-union-delivered-before-joint-session-the-congress',
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-reporting-the-state-the-union-1',
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-reporting-the-state-the-union',
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-reporting-the-state-the-union-0',
            'https://www.presidency.ucsb.edu/documents/the-state-the-union-address-delivered-before-joint-session-the-congress-1', 
            'https://www.presidency.ucsb.edu/documents/the-state-the-union-address-delivered-before-joint-session-the-congress-0', 
            'https://www.presidency.ucsb.edu/documents/the-state-the-union-address-delivered-before-joint-session-the-congress', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-reporting-the-state-the-union-2',
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-3', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-4', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-5', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-congress-the-state-the-union', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-congress-the-state-the-union-1', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-congress-the-state-the-union-0', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-2', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-1', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-0', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-12', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-11', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-10', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-9', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-8', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-6', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-7', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-22', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-23', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-24', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-14', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-13', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-18', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-17', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-16', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-15', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-congress-the-state-the-union-2', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-21', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-20', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-19', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-25', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-26', 
            'https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-27']
    df = {'president': {}, 'year': {}, 'party': {}, 'speech': {}}
    for url in urls:
        url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        speech = soup.find('div', class_ = 'field-docs-content').text 
        year = soup.find('span', class_ = 'date-display-single').text[-4:]
        president = soup.find('h3', class_ = 'diet-title').text
        df['speech'][president + '-' + year] = speech
        df['year'][president + '-' + year] = year
        df['president'][president + '-' + year] = president
        if president == 'Jimmy Carter' or president == 'William J. Clinton' or president == 'Barack Obama':
            df['party'][president + '-' + year] = 'Democratic'
        else:
            df['party'][president + '-' + year] = 'Republican'
    return pd.DataFrame(df)