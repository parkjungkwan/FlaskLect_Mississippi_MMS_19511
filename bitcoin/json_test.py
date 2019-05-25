import pandas as pd
html_data = pd.read_html("https://www.gov.uk/performance/g-cloud/cumulative-sales-by-company-size")
# html_data[0]
print(html_data)
print('-------------------------')
print(html_data[0])