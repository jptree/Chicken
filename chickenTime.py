import re
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

locations = [
    'https://www.ubereats.com/store/mcdonalds-1069-n-court-st/Y4cUFbTpRIeZGs6s1Ro_8Q?utm_source=mcdonalds&utm_medium=brandpage&utm_campaign=ext-mcdonalds-USCA-storepage',
    'https://www.ubereats.com/store/mcdonalds-carnegie-%26-32nd-st/mfpYUTEzQRmD6tvMutJUBw?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNsZXZlbGFuZCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMV3RvNHk3dk1JZ1JRaGhpOTFYTEJPMCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MS40OTkzMiUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MS42OTQzNjA1JTdE&utm_campaign=ext-mcdonalds-USCA-storepage&utm_medium=brandpage&utm_source=mcdonalds',
    'https://www.ubereats.com/store/mcdonalds-main-%26-grant/ADvfv17tTuemPI-2vUskPQ?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNsZXZlbGFuZCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMV3RvNHk3dk1JZ1JRaGhpOTFYTEJPMCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MS40OTkzMiUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MS42OTQzNjA1JTdE&utm_campaign=ext-mcdonalds-USCA-storepage&utm_medium=brandpage&utm_source=mcdonalds',
    'https://www.ubereats.com/store/mcdonalds-mcmillan-%26-victory/IgtMgli6TsW8qPcD8kLDFg?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNsZXZlbGFuZCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMV3RvNHk3dk1JZ1JRaGhpOTFYTEJPMCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MS40OTkzMiUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MS42OTQzNjA1JTdE&utm_campaign=ext-mcdonalds-USCA-storepage&utm_medium=brandpage&utm_source=mcdonalds'
]

# def get_mcdonalds_chicken_prices(urls, driver):
#     popular_table_path = '//*[@id="main-content"]/div[4]/ul/li[1]/ul'
#                          # '//*[@id="main-content"]/div[5]/ul/li[1]/ul'
#     first_time = True
#     for url in urls:
#         driver.get(url)
#         if first_time:
#             input("Please close popup window and accept cookies... Press a key when finished...")
#             first_time = False
#
#         try:
#             table = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, popular_table_path))
#             )
#         except EC.NoSuchElementException:
#             driver.quit()
#
#         # table = driver.find_element_by_xpath(popular_table_path)
#         items = table.find_elements_by_tag_name('li')
#         for i in range(len(items)):
#             price_xpath = f'//*[@id="main-content"]/div[4]/ul/li[1]/ul/li[{i + 1}]/div/div/div/div[1]/div[2]/div[1]'
#             name_xpath = f'//*[@id="main-content"]/div[4]/ul/li[1]/ul/li[{i + 1}]/div/div/div/div[1]/div[1]/h4/div'
#             name = driver.find_element_by_xpath(name_xpath).text
#             price = driver.find_element_by_xpath(price_xpath).text
#             if 'nug' or 'chic' in name.lower():
#                 print(f'The {name} contains chicken and costs {price}!')




def get_mcdonalds_chicken_prices_regex(urls, driver):
    """
    I believe this is a scalable chicken price scraper for McDonald's. This could be improved, but the concept is here.
    This uses Regular Expressions to find the chicken related meals. This should be modified to acquire the individual
    items instead of the entire meal as that would factor in different input prices besides chicken.

    This could be improved if I found how the website queries data through an API. This would likely be the best source
    for data.

    The urls have to be valid. The retrieval of URLS could also be automated.

    :param urls: list of UberEats ordering URL's for any McDonald's location
    :param driver: chromewebdriver instance, pass webdriver.Chrome() as parameter
    :return: Currently returns nothing nor does anything else besides printing result
    """
    first_time = True
    for url in urls:
        driver.get(url)

        if first_time:
            input("Please close popup window and accept cookies... Press a key when finished...")
            first_time = False

        print(url)
        ul_list = driver.find_elements_by_tag_name('ul')
        for ul in ul_list:
            all_text = ul.text
            meals = re.findall(r"(Most Popular\n)([\s\S]+)(\nCombo Meals)", all_text)
            if meals:
                text = str(meals[0][1]).split('\n')
                for i in range(0, len(text), 4):
                    meal_name = text[i]
                    meal_price = text[i + 1]
                    if 'chicken' in meal_name.lower() or 'nugget' in meal_name.lower():
                        print(f'The {meal_name} contains chicken and costs {meal_price}!')

        print('\n')


if __name__ == "__main__":
    driver = webdriver.Chrome()
    get_mcdonalds_chicken_prices_regex(locations, driver)

    """
    OUTPUT:
    
    Please close popup window and accept cookies... Press a key when finished...
    https://www.ubereats.com/store/mcdonalds-1069-n-court-st/Y4cUFbTpRIeZGs6s1Ro_8Q?utm_source=mcdonalds&utm_medium=brandpage&utm_campaign=ext-mcdonalds-USCA-storepage
    The Crispy Chicken Sandwich Meal contains chicken and costs $7.13!
    The Spicy Chicken Sandwich Meal contains chicken and costs $7.23!
    The 10 Piece McNuggets contains chicken and costs $5.15!
    The 10 Piece McNuggets Meal contains chicken and costs $8.63!
    The 40 McNuggets contains chicken and costs $13.20!
    The 4 Piece Chicken McNugget - Happy Meal contains chicken and costs $4.79!
    
    
    https://www.ubereats.com/store/mcdonalds-carnegie-%26-32nd-st/mfpYUTEzQRmD6tvMutJUBw?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNsZXZlbGFuZCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMV3RvNHk3dk1JZ1JRaGhpOTFYTEJPMCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MS40OTkzMiUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MS42OTQzNjA1JTdE&utm_campaign=ext-mcdonalds-USCA-storepage&utm_medium=brandpage&utm_source=mcdonalds
    The Crispy Chicken Sandwich Meal contains chicken and costs $7.69!
    The Spicy Chicken Sandwich Meal contains chicken and costs $7.69!
    The 10 Piece McNuggets contains chicken and costs $4.79!
    The 10 Piece McNuggets Meal contains chicken and costs $7.79!
    The 40 McNuggets contains chicken and costs $11.58!
    The 4 Piece Chicken McNugget - Happy Meal contains chicken and costs $4.29!
    
    
    https://www.ubereats.com/store/mcdonalds-main-%26-grant/ADvfv17tTuemPI-2vUskPQ?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNsZXZlbGFuZCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMV3RvNHk3dk1JZ1JRaGhpOTFYTEJPMCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MS40OTkzMiUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MS42OTQzNjA1JTdE&utm_campaign=ext-mcdonalds-USCA-storepage&utm_medium=brandpage&utm_source=mcdonalds
    The Crispy Chicken Sandwich Meal contains chicken and costs $7.80!
    The Spicy Chicken Sandwich Meal contains chicken and costs $8.75!
    The 10 Piece McNuggets contains chicken and costs $4.99!
    The 10 Piece McNuggets Meal contains chicken and costs $8.74!
    The 40 McNuggets contains chicken and costs $12.74!
    The 4 Piece Chicken McNugget - Happy Meal contains chicken and costs $4.01!
    
    
    https://www.ubereats.com/store/mcdonalds-mcmillan-%26-victory/IgtMgli6TsW8qPcD8kLDFg?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkNsZXZlbGFuZCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpMV3RvNHk3dk1JZ1JRaGhpOTFYTEJPMCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0E0MS40OTkzMiUyQyUyMmxvbmdpdHVkZSUyMiUzQS04MS42OTQzNjA1JTdE&utm_campaign=ext-mcdonalds-USCA-storepage&utm_medium=brandpage&utm_source=mcdonalds
    The Crispy Chicken Sandwich Meal contains chicken and costs $9.75!
    The Spicy Chicken Sandwich Meal contains chicken and costs $10.10!
    The 10 Piece McNuggets contains chicken and costs $4.99!
    The 10 Piece McNuggets Meal contains chicken and costs $8.99!
    The 40 McNuggets contains chicken and costs $12.99!
    The 4 Piece Chicken McNugget - Happy Meal contains chicken and costs $4.99!
    
    
    
    Process finished with exit code 0

    """