import streamlit as st

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import pandas as pd
from selenium.webdriver.common.keys import Keys
import datetime
start_time = time.time()

file_path = 'Keywords.csv'
df = pd.read_csv(file_path)
keys = df.iloc[:, 0].tolist()

dte = datetime.date.today()
date = str(dte.strftime("%B %d, %Y"))
print("Today's date is:", date)
print("\n\n")
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for element presence
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "your_xpath_here")))




st.set_page_config(page_title="Umer", page_icon="🧊")

st.write("# NEWS BOT")
st.write("Processing .... !!!!")

# Para graph Summary of 300 words.
def summary(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize variables to keep track of word count and the truncated output
    word_count = 0
    truncated_output = []

    # Iterate through the words and add them to the truncated output until reaching 500 words
    for word in words:
        # Only count non-empty words (exclude spaces)
        if word.strip():  # Check if the word is not empty after stripping spaces
            if word_count + 1 <= 100:
                truncated_output.append(word)
                word_count += 1
            else:
                break

    # Join the words in the truncated output to create the final result
    result = ' '.join(truncated_output)

    # Add '...' if the string was truncated
    if word_count < len(words):
        result += '...'

    # Print the result
    return result    # S #  #


# Checking Keyword with the paragraph
def check_keywords_in_paragraph(keywords, paragraph):
    translator = str.maketrans('', '', string.punctuation)
    paragraph_words = paragraph.lower().translate(translator).split()
    keywords_lower = [word.lower() for word in keywords]
    matched_keywords = set(paragraph_words) & set(keywords_lower)

    if len(matched_keywords) >= 3:
        return 1
    else:
        return 0





def teams_upload(links, heading, para):
    # Initialize the WebDriver with Edge
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    # options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)
    driver.maximize_window()

    # Open the Website
    driver.get("https://web.yammer.com/main/groups/eyJfdHlwZSI6Ikdyb3VwIiwiaWQiOiI2MjIyNDU1NjAzMiJ9")
    driver.implicitly_wait(10)

    # Email
    email_input = driver.find_element("id", "i0116")
    email_input.send_keys("hafsa.ahmad@cppapk.onmicrosoft.com")
    time.sleep(1)

    next_button = driver.find_element("id", "idSIButton9")
    next_button.click()

    time.sleep(1)

    pass_input = driver.find_element("id", "i0118")
    pass_input.send_keys("corNetto123*")

    time.sleep(1)

    sign_button = driver.find_element("id", "idSIButton9")
    sign_button.click()
    time.sleep(1)


    no_button = driver.find_element("id", "idBtn_Back")
    no_button.click()

    time.sleep(3)

    for li, he, pa in zip(links, heading, para):
        try:
            driver.implicitly_wait(10)
            #discussion_button = driver.find_element("xpath", "//*         [@id='root']/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/div[2]/button")
            discussion_button = driver.find_element("xpath", '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[1]/button')
            #discussion_button = driver.find_element("xpath", '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[1]/button')

            discussion_button.click()
            time.sleep(2)

        except Exception as e:
            print("Disscussion Not Found")
            while(1):
                time.sleep(10)

        # Posting

        #editor = driver.find_element("xpath", "//*[@id='root']/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div")

        editor = driver.find_element("xpath", "// *[ @ id = 'root']/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div")
        editor.send_keys(li)
        editor.send_keys(Keys.CONTROL, 'a')
        editor.send_keys(Keys.CONTROL, 'x')
        editor.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        editor.send_keys(Keys.CONTROL, 'a')
        editor.send_keys(Keys.CONTROL, 'x')

        # Heading Post

        editor.send_keys(he)
        editor.send_keys(Keys.CONTROL, 'a')
        editor.send_keys(Keys.CONTROL, 'b')
        #editor.click()
        editor.send_keys(Keys.RIGHT)
        editor.send_keys(Keys.ENTER)
        editor.send_keys(Keys.ENTER)

        # Paragraph Posting

        editor.send_keys(Keys.CONTROL, 'b')
        editor.send_keys(pa)
        editor.send_keys(Keys.ENTER)

        time.sleep(2)
        editor.send_keys(Keys.CONTROL, 'b')
        editor.send_keys(Keys.CONTROL + Keys.ENTER)
        #post_button = driver.find_element("xpath", "//*[@id='root']/div/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/div/div/div[1]/button")
        #post_button.click()

    driver.quit()


# Function for Business Record paper
def business_recorder():
    def link_extract(href_val, number):
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_argument("--headless")  # Run in headless mode to improve performance
        driver = webdriver.Edge(options=options)

        driver.get(href_val)
        driver.implicitly_wait(10)
        news_elements = driver.find_elements(By.CLASS_NAME, 'news')
        print(f"length of news from page {number + 1}: ", len(news_elements))

        urls = []
        for news_element in news_elements:
            try:
                num_id = news_element.get_attribute('id')
                date = news_element.get_attribute('date')
                page = news_element.get_attribute('page')
                url = f"https://epaper.brecorder.com/" + date + '/' + page + '-page/' + num_id + '-news' + '.html'
                urls.append(url)

            except:
                continue

        para = []
        final_lst = []
        heading = []
        for k in urls:
            try:
                driver.get(k)
                time.sleep(1)  # Add a small delay to allow the page to load

                heading_ele = driver.find_element(By.CSS_SELECTOR, 'a.story__link.text-black')  # EXTRACT NEWS HEADING
                heading_text = heading_ele.text

                content = driver.find_elements(By.CLASS_NAME, 'story__content')[0]  # EXTRACT NEWS TEXT
                data = content.text
                flag = check_keywords_in_paragraph(keys, data)
                if flag:
                    final_lst.append(k)
                    para.append(summary(data))
                    heading.append(heading_text)

            except:
                continue
        return final_lst, para, heading

    # Initialize the WebDriver with Edge
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)

    # Open the Website
    driver.get("https://epaper.brecorder.com/")         # OPen the main website
    driver.implicitly_wait(10)

    href = []
    for i in range(1, 50):
        try:
            parent_element = driver.find_element(By.XPATH, f"/html/body/div[2]/div/div[2]/div[2]/div/div[{i}]")  # Find All the recent papers at the right side of the website
            div_elements = parent_element.find_element(By.TAG_NAME, "a")
            href.append(div_elements.get_attribute("href"))
        except:
            break

    print("Total Papers found: ", len(href))   # Total recent papers at the right side of the website

    links = []
    text_lst = []
    heading_lst = []
    for num, i in enumerate(href):
        try:
            data, text, heading = link_extract(i, num)       # Extract The Links RELATED LINKS OF EACH RECENT LINK , AND EXTARCT THERE TEXT.
            links.append(data)
            text_lst.append(text)
            heading_lst.append(heading)
        except:
            print(f"Unable to extract page {num + 1} ")



    heading_lst = [item for sublist in heading_lst if sublist for item in sublist]
    text_lst = [item for sublist in text_lst if sublist for item in sublist]
    result = [item for sublist in links if sublist for item in sublist]
    print(f"\n{len(heading_lst)} Related Papers Found: \n")
    driver.quit()
    return result, heading_lst, text_lst


# Function for Reuters paper
def reuters():

    file_path = 'Keywords.csv'
    df = pd.read_csv(file_path)
    keys = df['Reuters'].tolist()
    keys = [x for x in keys if x == x]

    options = webdriver.EdgeOptions()
    options.use_chromium = True
    #options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)

    # login
    driver.get("https://www.reuters.com/account/sign-in/?redirect=https%3A%2F%2Fwww.reuters.com%2Fbusiness%2Fenergy%2F")  # OPen the main website
    driver.implicitly_wait(10)

    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys("washakh.ali@cppa.gov.pk")

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("Wash,akh@123")

    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    # Open the Website
    driver.get("https://www.reuters.com/business/energy/")  # Open the main website
    time.sleep(5)
    driver.implicitly_wait(10)

    urls = []

    # Main Heading
    element = driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/div/div[1]/div")  # Main Heading
    links = element.find_element(By.CSS_SELECTOR, 'a')
    href = links.get_attribute('href')
    urls.append(href)

    # Side Heading

    for i in range(1, 50):
        try:
            ul = driver.find_element(By.XPATH, f'//*[@id="main-content"]/div[2]/div/div[1]/div/ul/li[{i}]')
            element = ul.find_element(By.CSS_SELECTOR, '[data-testid="Heading"]')
            href = element.get_attribute('href')
            urls.append(href)
        except:
            break

    print(f"\nTotal {len(urls)} news Found")

    para_lst = []
    url_lst = []
    heading_lst = []

    for ul in urls:

        try:
            driver.get(ul)
            driver.implicitly_wait(10)

            # Heading
            heading = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/div[1]/div/header/div/div/h1')
            head = heading.text

            # Paragraph
            article = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/div[1]/div/div/div/div[2]')
            data = article.text[:-100]
            flag = check_keywords_in_paragraph(keys, data)
            if flag:
                url_lst.append(ul)
                para_lst.append(summary(data))
                heading_lst.append(head)
        except:
            continue

    return url_lst, heading_lst,  para_lst


# Function for Mck Electric paper
def mck_electric():
    file_path = 'Keywords.csv'
    df = pd.read_csv(file_path)
    keys = df['Reuters'].tolist()
    keys = [x for x in keys if x == x]

    today = datetime.date.today()
    formatted_date = today.strftime("%m/%d/%Y")
    # Print the formatted date


    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)

    # OPen the main website
    driver.get("https://www.mckinsey.com/industries/electric-power-and-natural-gas/our-insights")
    driver.implicitly_wait(10)

    articles = driver.find_elements(By.XPATH, "//*[@id='skipToMain']/div[2]/div/div/div[3]/div/div/section/div")
    print(f"Total Artilces Found: {len(articles)}")

    links = []
    headings = []
    for i in articles:
        date = i.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        if str(date) == str(formatted_date):
            url = i.find_element(By.CLASS_NAME, "mdc-c-link-heading").get_attribute("href")
            heading = i.find_element(By.CLASS_NAME, "mdc-c-link-heading").text
            links.append(url)
            headings.append(heading)

    para_lst = []
    url_lst = []
    heading_lst = []

    for ul, h in zip(links, headings):
        driver.get(ul)
        driver.implicitly_wait(10)
        try:
            paragraph = driver.find_element(By.XPATH, "//*[@id='skipToMain']/div[2]/div[1]")
            text = paragraph.text
            index = text.index("Save")
            text = text[index + 4:-100]
            flag = check_keywords_in_paragraph(keys, text)
        except:
            try:
                paragraph = driver.find_element(By.XPATH, "//*[@id='skipToMain']/div/div/div/div[2]/div/div/div")
                text = paragraph.text
                text = text[50:-100]
                flag = check_keywords_in_paragraph(keys, text)
            except:
                print(f"Unable To fetch data of {h}")
                continue

        if flag:
            url_lst.append(ul)
            para_lst.append(summary(text))
            heading_lst.append(h)

    return url_lst, heading_lst, para_lst


# Function for Mck Oil paper
def mck_oil():
    file_path = 'Keywords.csv'
    df = pd.read_csv(file_path)
    keys = df['Reuters'].tolist()
    keys = [x for x in keys if x == x]

    today = datetime.date.today()
    formatted_date = today.strftime("%m/%d/%Y")
    # Print the formatted date


    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)

    # OPen the main website
    driver.get("https://www.mckinsey.com/industries/oil-and-gas/our-insights")
    driver.implicitly_wait(10)

    articles = driver.find_elements(By.XPATH, "//*[@id='skipToMain']/div[2]/div/div/div[3]/div/div/section/div")
    print(f"Total Artilces Found: {len(articles)}")

    links = []
    headings = []
    for i in articles:
        date = i.find_element(By.TAG_NAME, "time").get_attribute("datetime")
        if str(date) == str(formatted_date):
            url = i.find_element(By.CLASS_NAME, "mdc-c-link-heading").get_attribute("href")
            heading = i.find_element(By.CLASS_NAME, "mdc-c-link-heading").text
            links.append(url)
            headings.append(heading)

    para_lst = []
    url_lst = []
    heading_lst = []

    for ul, h in zip(links, headings):
        driver.get(ul)
        driver.implicitly_wait(10)
        try:
            paragraph = driver.find_element(By.XPATH, "//*[@id='skipToMain']/div[2]/div[1]")
            text = paragraph.text
            index = text.index("Save")
            text = text[index+4:-100]
            flag = check_keywords_in_paragraph(keys, text)
        except:
            try:
                paragraph = driver.find_element(By.XPATH, "//*[@id='skipToMain']/div/div/div/div[2]/div/div/div")
                text = paragraph.text
                text = text[50:-100]
                flag = check_keywords_in_paragraph(keys, text)
            except:
                print(f"Unable To fetch data of {h}")
                continue

        if flag:
            url_lst.append(ul)
            para_lst.append(summary(text))
            heading_lst.append(h)

    return url_lst,heading_lst,  para_lst


# Function for PIDE paper
def pide():
    file_path = 'Keywords.csv'
    df = pd.read_csv(file_path)
    keys = df['Reuters'].tolist()
    keys = [x for x in keys if x == x]

    today = datetime.date.today()
    formatted_date = str(today.strftime("%B %d, %Y"))
    # Print the formatted date
    print("Today's date is:", formatted_date)

    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)

    # OPen the main website
    driver.get("https://pide.org.pk/")
    driver.implicitly_wait(10)

    urls = []
    titles = []

    for i in range(1, 7):
        articles = driver.find_elements(By.XPATH, f"//*[@id='ppp']/div/div/div/div[{i}]")[0]
        try:
            date = articles.find_element(By.XPATH, f"//*[@id='ppp']/div/div/div/div[{i}]/div/div/div/div/div[3]/div/div[2]/div/div/div/div[2]").text
        except:
            try:
                date = articles.find_element(By.XPATH, f"//*[@id='ppp']/div/div/div/div[{i}]/div/div/div/div/div[3]/div/div/div/div/div/div[2]").text
            except:
                continue

        link = articles.find_element(By.TAG_NAME, "a").get_attribute("href")
        title = articles.find_element(By.CLASS_NAME, "jet-listing-dynamic-field__content").text

        if date == formatted_date:
            urls.append(link)
            titles.append(title)

    url_lst = []
    para_lst = []
    heading_lst = []

    for j, t in zip(urls, titles):
        driver.get(j)
        driver.implicitly_wait(10)

        para = driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div").text
        flag = check_keywords_in_paragraph(keys, para)
        if flag:
            url_lst.append(j)
            para_lst.append(summary(para))
            heading_lst.append(t)


    return url_lst,  heading_lst, para_lst



# Function for IEEFA paper
def ieefa():
    file_path = 'Keywords.csv'
    df = pd.read_csv(file_path)
    keys = df['Reuters'].tolist()
    keys = [x for x in keys if x == x]

    today = datetime.date.today()
    formatted_date = str(today.strftime("%B %d, %Y"))
    # Print the formatted date


    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)


    # OPen the main website
    driver.get("https://ieefa.org/newsroom?keys=&content_type%5B0%5D=3&content_type%5B1%5D=3")
    driver.implicitly_wait(10)

    articles = driver.find_elements(By.XPATH, "//*[@id='All']/div[2]/div[2]")[0]
    classes = articles.find_elements(By.CLASS_NAME, "card-row")

    print(f"Total Artilces Found: {len(classes)}")

    hrefs = []


    for i in range(1, 8):
        try:
            for j in range(1, 4):
                link = articles.find_elements(By.XPATH, f"//*[@id='All']/div[2]/div[2]/div[{i}]/a[{j}]")[0]
                date = link.find_element(By.CLASS_NAME, "tags").text
                if date == formatted_date:
                    link = link.get_attribute("href")
                    hrefs.append(link)
        except:
            break

    para_lst = []
    url_lst = []
    heading_lst = []

    for u in hrefs:
        driver.get(u)
        # Heading
        title = driver.find_element(By.TAG_NAME, "h1").text

        # Paragraph


        try:
            key_takeaways_section = driver.find_element(By.CLASS_NAME, 'takeawayblock')
            key_takeaways_paragraphs = key_takeaways_section.find_element(By.XPATH, './following-sibling::div')
            para = key_takeaways_paragraphs.find_element(By.TAG_NAME, "p").text
            flag = check_keywords_in_paragraph(keys, para)

        except:
            try:
                para = driver.find_element(By.CLASS_NAME, "rtb").text
                flag = check_keywords_in_paragraph(keys, para)

            except:
                para = ''
                flag = None
                print("ParaGraph was unable to Access note found ")

        if flag:
            url_lst.append(u)
            para_lst.append(summary(para))
            heading_lst.append(title)

    return url_lst, heading_lst, para_lst


def spdi(url):

    today = datetime.date.today()
    formatted_date = str(today.strftime("%d %b,%Y"))
    print("Today's date is:", formatted_date)
    print("\n\n")
    formatted_date = '10 Oct,2023'

    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")  # Run in headless mode to improve performance
    driver = webdriver.Edge(options=options)

    # OPen the main website
    driver.get(url)
    driver.implicitly_wait(10)

    url_lst = []
    para_lst = []
    heading_lst = []

    for i in range(1, 100):
        try:
            news = driver.find_elements(By.XPATH, f"//*[@id='table-data']/div[{i}]")[0]
            date = news.find_element(By.CLASS_NAME, "col").text
            if date == formatted_date:
                href = (news.find_element(By.TAG_NAME, "a").get_attribute("href"))
                driver.get(href)
                driver.implicitly_wait(10)
                article = ''
                para = driver.find_elements(By.XPATH, "//div[@class='container-fluid chinastudycenter']//p")
                for p_tag in para:
                    article += p_tag.text + ' '

                flag = check_keywords_in_paragraph(keys, article)
                if flag:
                    url_lst.append(href)
                    para_lst.append(article)
                    heading_lst.append(driver.find_element(By.TAG_NAME, "h3").text)
        except:
            break

        return url_lst, heading_lst, para_lst






count = 0


print('###############################################################################################################')
print('#########################################   Business Recorder   ###############################################')
print('###############################################################################################################')
print("\n\n")
link, headings, para_text = business_recorder()

if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of Business Recorder Successfully..\n\n\n")
else:
    print("No Related Links were Found in Business Recorder.\n\n\n")


print('###############################################################################################################')
print('#############################################   Reuters   #####################################################')
print('###############################################################################################################')
print("\n\n")
link, headings, para_text = reuters()
if len(link) != 0:
    print(f"Posting {len(link)} News...")
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of Reuters Successfully..\n\n\n")
else:
    print("No Related Links were Found in Reuters.\n\n\n")


print('###############################################################################################################')
print('########################################   Mckinsey & Company   ###############################################')
print('###############################################################################################################')
print("\n\n")
link, headings, para_text = mck_electric()
if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of Mckinsey Electric  Successfully..\n\n\n")
else:
    print("No Related Links were Found in Mckinsey Electric.\n\n\n")


link, headings, para_text = mck_oil()
if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of Mckinsey Oil Successfully..\n\n\n")
else:
    print("No Related Links were Found in Mckinsey Oil.\n\n\n")


print('###############################################################################################################')
print('#############################################   IEEFA   #######################################################')
print('###############################################################################################################')
print("\n\n")
link, headings, para_text = ieefa()
if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of IEEFA Successfully..\n\n\n")
else:
    print("No Related Links were Found in IEEFA.\n\n\n")


print('###############################################################################################################')
print('#############################################   PIDE  #########################################################')
print('###############################################################################################################')
print("\n\n")
link, headings, para_text = pide()
if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of PIDE Successfully..\n\n\n")
else:
    print("No Related Links were Found in PIDE.\n\n\n")




print('###############################################################################################################')
print('##########################################   SDPI BLOGS  ######################################################')
print('###############################################################################################################')
print("\n\n")

link, headings, para_text = spdi('https://sdpi.org/blogs')
if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of SDPI BLOGS Successfully..\n\n\n")
else:
    print("No Related Links were Found in SDPI BLOGS.\n\n\n")


print('###############################################################################################################')
print('##########################################   SDPI NEWS  #######################################################')
print('###############################################################################################################')
print("\n\n")

link, headings, para_text = spdi('https://sdpi.org/news')
if len(link) != 0:
    teams_upload(link, headings, para_text)
    count = count + len(link)
    print("Posted All Related Links of SDPI NEWS Successfully..\n\n\n")
else:
    print("No Related Links were Found in SDPI NEWS.\n\n\n")


print(f"Total News Posted = {count}")
print("All News Posted Successfully!!!")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Program took {round(elapsed_time/60  ,3)} Minutes to run.")