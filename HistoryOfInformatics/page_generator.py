import common
import json

sections = ['HOME','SOFTWARE','HARDWARE','INTERNET','GAMES','HCI']

def create_article(section,article):
    jsonSend = {}
    article_data = common.getArticleForURL(section, article)
    article_data['navElement'] = ''
    for element in sections:
        if section == element.lower():
            article_data['navElement'] += common.jinjaSubstitution({'sectonNameSelected':element.lower()+' selected', 'sectionName':element, 'sectonNameHref':element.lower()},'navbarList')
        else:
            article_data['navElement'] += common.jinjaSubstitution({'sectonNameSelected':element.lower(), 'sectionName':element, 'sectonNameHref':element.lower()},'navbarList')
    jsonSend['body'] = common.jinjaSubstitution(article_data,'navbarMain')

    jsonSend['body'] += common.jinjaSubstitution(article_data,'topicPage')

    jsonSend['title'] = article_data['title']

    jsonSend['section'] = section

    return json.dumps(jsonSend)

def hci(section):
    jsonSend = {}
    article_data = common.getSectionIndexPage(section)
    article_data['navElement'] = ''
    for element in sections:
        if section == element.lower():
            article_data['navElement'] += common.jinjaSubstitution({'sectonNameSelected':element.lower()+' selected', 'sectionName':element, 'sectonNameHref':element.lower()},'navbarList')
        else:
            article_data['navElement'] += common.jinjaSubstitution({'sectonNameSelected':element.lower(), 'sectionName':element, 'sectonNameHref':element.lower()},'navbarList')
    
    jsonSend['body'] = common.jinjaSubstitution(article_data,'navbarMain')

    jsonSend['body'] += common.jinjaSubstitution(article_data,'topicPage')

    jsonSend['title'] = section

    jsonSend['section'] = section
    return json.dumps(jsonSend)

def create_section(section):
    articles = common.allArticlesFromTable(section)
    jsonSend = {}
    jsonSend['entries'] = ''
    for article in articles:
        jsonSend['entries'] += common.jinjaSubstitution(article,'timelineEntry')

    article_data = common.getSectionIndexPage(section)
    article_data['navElement'] = ''
    for element in sections:
        if section == element.lower():
            article_data['navElement'] += common.jinjaSubstitution({'sectonNameSelected':element.lower()+' selected', 'sectionName':element, 'sectonNameHref':element.lower()},'navbarList')
        else:
            article_data['navElement'] += common.jinjaSubstitution({'sectonNameSelected':element.lower(), 'sectionName':element, 'sectonNameHref':element.lower()},'navbarList')

    jsonSend['body'] = common.jinjaSubstitution(article_data,'navbarMain')
    jsonSend['body'] += common.jinjaSubstitution({'sectionTitle':section.upper(),'timelineEntries':jsonSend['entries']},'timelinePage')
    jsonSend['title'] = section
    jsonSend['section'] = section



    return json.dumps(jsonSend)