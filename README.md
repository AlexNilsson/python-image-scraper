# gscraper
A google image search scraper to automatically search and download images from the web

## Install
```
pip install gscraper
```

## Format
```python
from gscraper import scrapeImages

scrapeImages(search_queries='nicolas cage', limit=5, sub_dir_name='<query-string>', output_directory='downloads', delay=0 )
'''
search_queries:     Comma separated <String> or <List>
limit:              <Int> 0-100
folder_name:        <String> or '<query-string>'
output_directory:   <String>
delay:              <Int> Seconds, delay between download queries

'''

```

## Examples
```python
from gscraper import scrapeImages

scrapeImages( search_queries='query', limit=3 )
'''
downloads/
| query/
| | image-1
| | image-2
| | image-3
'''
scrapeImages( search_queries='query', limit=1, sub_dir_name='output' )
'''
downloads/
| output/
| | image-1
'''

scrapeImages( search_queries=['one','two'], limit=2, output_directory='numbers' )
'''
numbers/
| one/
| | image-1
| | image-2
| two/
| | image-1
| | image-2
'''

scrapeImages( search_queries=['one','two'], limit=2, sub_dir_name='output' )
'''
numbers/
| output/
| | image-1
| | image-2
| | image-3
| | image-4
'''
```
