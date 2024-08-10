import click
import httpx
from scrapy.selector import Selector


@click.command()
@click.option('--city', default="komsomolsk-na-amure", help="City to get weather for")
def weather(city):
  
  url = f'https://pogoda.mail.ru/prognoz/{city}/'
  with httpx.Client() as client:
    resp = client.get(url, timeout=None)
    resp.raise_for_status()
    
  selector = Selector(text=resp.text)
  t = selector.xpath('//div[@class="information__content__temperature"]/text()').getall()[1].strip()
  s = selector.xpath('//div[@class="information__content__temperature"]/span/@title').extract()[0]
  
  click.echo(f"City: {city}, T°: {t}, \nsource: pogoda.mail.ru")
  click.echo(s)
  

if __name__ == '__main__':
  weather()