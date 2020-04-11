import discord
import datetime
from selenium import webdriver
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('?hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        elif message.content.startswith('?today'):
            day = datetime.datetime.now()
            await message.channel.send('Today is: {}'.format(day.strftime("%A")))

        elif message.content.startswith('?USDtoBRL'):
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            driver = webdriver.Chrome(options=option)
            driver.get("https://www.google.com/search?q=dolar+hoje&oq=dolar+hoje&aqs=chrome..69i57j35i39j0l5j5.1328j0j7&sourceid=chrome&ie=UTF-8")
            for price in driver.find_elements_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'):
                msg = await message.channel.send('Searching')
                await msg.edit(content="Searching.")
                await msg.edit(content="Searching..")
                await msg.edit(content="Searching...")
                await message.channel.send('Dolar price in BRL: {}'.format(price.text))
            driver.quit()

        elif message.content.startswith('?bitcoin'):
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            driver = webdriver.Chrome(options=option)
            driver.get("https://www.google.com/search?sxsrf=ALeKk01bwR-8YMjfWKnRl7VCwB6uBK2Wyw%3A1586561446267&ei=pgGRXsjuD7OW0Aadx47QDQ&q=bitcoin&oq=bitcoin&gs_lcp=CgZwc3ktYWIQAzICCAAyBAgAEEMyAggAMgcIABCDARBDMgcIABCDARBDMgcIABCDARBDMgQIABBDMgIIADICCAAyAggAOgQIABBHOgUIABCDAToECCMQJ0omCBcSIjBnMTI2ZzExOWcxMjRnMTI3ZzEyOWcxMzVnMTQ1ZzEwLTlKGAgYEhQwZzFnMWcxZzFnMWcxZzFnMTAtMVCvqH1YxrN9YL21fWgAcAF4AIABjQGIAegGkgEDMC43mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjI2az7gd_oAhUzC9QKHZ2jA9oQ4dUDCAw&uact=5")
            for price in driver.find_elements_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'):
                msg = await message.channel.send('Searching.')
                await msg.edit(content="Searching.")
                await msg.edit(content="Searching..")
                await msg.edit(content="Searching...")
                await message.channel.send('Bitcoin price in BRL: {}'.format(price.text))
            driver.quit()

client = MyClient()
client.run('Njk4Mjk3ODk0MTEyODU0MDI2.XpDzWw.Va7kQyDxBNC5cI1ADwNbK_TpRpU')