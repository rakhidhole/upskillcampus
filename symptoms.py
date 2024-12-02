import requests
from bs4 import BeautifulSoup

def search_google(query):
  """
  Searches Google for the given query and returns the results.

  Args:
    query: The search query.

  Returns:
    A list of search results.
  """

  url = f"https://www.google.com/search?q={query}"
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
  }
  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, 'html.parser')
  results = soup.find_all('div', class_='g')

  return results

def get_apple_black_rot_symptoms():
  """
  Searches Google for Apple Black Rot symptoms and returns the results.
  """

  query = 'Apple Black Rot Symptoms'
  results = search_google(query)

  return results

if __name__ == '__main__':
  results = get_apple_black_rot_symptoms()
  print('HIII')

  for result in results:
    print(result.find('h3').text)
    print(result.find('a')['href'])
    print('--------------------')