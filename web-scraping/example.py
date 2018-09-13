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
                <li>Python</li>
                <li id="aLink">Java</li>
                <li><a href="https://developer.mozilla.org/bm/docs/Web/JavaScript">Javascript</li>
                <li><a href="http://www.cplusplus.com/doc/tutorial/">C++<</a></li>
                <li>C#</li>
                <a href="http://one_line_command_rocks.com/android">Command Rocks </a>
            </ul>
            <p class="test">i will display on your terminal with this:
                variable name = soup.find('p',class_='test')  #dont forget the _ on class or else will display invalid syntax
                            THANKS 
                lorem lorem lorem lorem lorem
            </p>
            <p class="test">I am just a second paragraph mate?</p>
        
        </body>
    <html>
 """

soup = BeautifulSoup(html_doc, 'lxml')

p = soup.find('p')
# output = Python [the first list element]
li = soup.find("li")
# find all    a tags
a_tag = soup.find_all('a')
# find class  this command will return the 1rst p element with the class test
p_class = soup.find('p', class_='test')
# finding all test classes
p_class_all = soup.find_all('p', class_="test")
# finding link with the ID of aLink
li_id = soup.find_all('li', {'id': 'aLink'})


###########TERMINAL OUTPUT###################
print "First p text i found: " + p.text
print "First li element i found: " + li.text
print li_id
print a_tag
# print the length of the a tags
#print len(a_tag)
# print the element with the given class
print p_class
print p_class_all
#print len(p_class_all)
