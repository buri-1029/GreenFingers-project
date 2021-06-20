from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

search_list = ["Acalypha reptans", "Adenium obesum", "Aeonium arboreum Zwartkop", "Alocasia amazonica", "Aloe barbadens", "Anthurium andraeanum", "Aspidistra elatior",
"Begonia semperflorens", "Calathea crocata", "Calathea insignis", "Calathea makoyana", "Camellia japonica", "Ceropegia woodii", "Chamaedorea elegans", "Clivia miniata", "Clusia rosea",
"Codiaeum variegatum", "Cupressus macrocarpa Wilma Goldcrest", "Cycas revoluta", "Cyclamen persicum", "Cymbidium spp", "Dendrobium phalaenopsis", "Dieffenbachia amoena Tropic snow",
"Dracaena deremensis Virens Compacta", "Dracaena fragrans Massangeana", "Dracaena marginata", "Dracaena reflexa Song of India", "Dracaena sanderiana", "Dracaena sanderiana Virens",
"Duranta reptans", "Epipremnum aureum", "Epipremnum aureum Lime", "Euonymus japonica", "Euphorbia pulcherrima", "Fatsia japonica", "Ficus elastica Tineke", "Ficus lyrata",
"Fittonia verschaffelti White Star", "Gardenia jasminoides", "Guzmania lingulata", "Haemaria discolor dawsoniana", "Hedera helix", "Hemionitis arifolia", "Heteropanax fragrans", "Hoya carnosa"]

for search in search_list:
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
print(search)
print(len(images))
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath(
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        path = f"./{search}/"
        urllib.request.urlretrieve(imgUrl, path + str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.close()
