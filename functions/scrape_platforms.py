def scrape_platforms(years):
    df = {'platform': {}, 'party': {}, 'year': {}}
    for year in years:
        Rurl = 'https://www.presidency.ucsb.edu/documents/'+ year +'-republican-party-platform'
        R_response = requests.get(Rurl)
        R_soup = BeautifulSoup(R_response.text, 'lxml')
        R_platform = R_soup.find('div', class_ = 'field-docs-content')
        
        if R_platform == None:
            Rurl = 'https://www.presidency.ucsb.edu/documents/republican-party-platform-'+ year
            R_response = requests.get(Rurl)
            R_soup = BeautifulSoup(R_response.text, 'lxml')
            R_platform = R_soup.find('div', class_ = 'field-docs-content')
        
        Durl = 'https://www.presidency.ucsb.edu/documents/'+ year +'-democratic-party-platform'
        D_response = requests.get(Durl)
        D_soup = BeautifulSoup(D_response.text, 'lxml')
        D_platform = D_soup.find('div', class_ = 'field-docs-content')
        
        if D_platform == None:
            Durl = 'https://www.presidency.ucsb.edu/documents/democratic-party-platform-' + year
            D_response = requests.get(Durl)
            D_soup = BeautifulSoup(D_response.text, 'lxml')
            D_platform = D_soup.find('div', class_ = 'field-docs-content')
        
        df['platform'][year + '-Rep'] = R_platform.text
        df['platform'][year + '-Dem'] = D_platform.text
        
        df['party'][year + '-Rep'] = 'Republican'
        df['party'][year + '-Dem'] = 'Democratic'
        
        df['year'][year + '-Rep'] = year
        df['year'][year + '-Dem'] = year
        
    df = pd.DataFrame(df)
    return df