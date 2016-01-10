# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import dateutil.parser
import lxml.html
import scraperwiki

# Read in a page
html = scraperwiki.scrape("http://heather.cs.ucdavis.edu/~matloff/256/Blog.html")

# Find something on the page using css selectors
root = lxml.html.fromstring(html)
for item in root.cssselect("h2"):
    content = []
    current_item = item.getnext()
    while current_item is not None and current_item.tag != "h2":
        content.append(lxml.etree.tostring(current_item))
        current_item = current_item.getnext()

    data = {
      'title': item.text,
      'content': "".join(content),
      'link': "http://heather.cs.ucdavis.edu/~matloff/256/Blog.html",
      'date': dateutil.parser.parse(item.text)
    }
    # Write out to the sqlite database using scraperwiki library
    scraperwiki.sqlite.save(unique_keys=['title'], data=data)

# An arbitrary query against the database
#scraperwiki.sql.select("* from data where 'name'='peter'")
