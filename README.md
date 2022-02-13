# JSURLExtractor
Extract URLs of .js files from http/s URL.

**Usage:**
---------------
`
python jsurlextractor.py <url.com> -<options>
`
**Example:**
1. Print js urls on screen.

`
python jsurlextractor.py https://evernote.com
`
2. Save the js urls into output file
`
python jsurlextractor.py https://evernote.com -o filename.txt
`
3. Check the status of js urls
`
python jsurlextractor.py https://evernote.com -s
`


Future work:
--
1. Pickup http/s urls from a list and extract .js URLs from each main domain URL.

