from bs4 import BeautifulSoup

html_doc = """
    <html>
        <head>
            <title>Web Scraping Example</title>
        </head>
        <body>
            <h1>Welcome</h1>
            <p>web scraping example test </p>
            <ul>
                <li>python</li>
                <li>java</li>
                <li>javascript</li>
            </ul>
            <p class="test">lorem lorem lorem lorem lorem lorem</p>
        
        </body>
    <html>
 """

soup = BeautifulSoup(html_doc, 'lxml')

p = soup.find('p')
li = soup.find("li")
print p.text
print li.text
