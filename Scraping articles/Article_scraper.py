import newspaper
import csv

# List of URLs to process
urls = [
    # BBC links
    "https://www.bbc.co.uk/news/world-middle-east-67404110",
    "https://www.bbc.co.uk/news/world-middle-east-67306902",
    "https://www.bbc.co.uk/news/world-middle-east-67480680",
    "https://www.bbc.co.uk/news/live/world-middle-east-67339462",
    "https://www.bbc.co.uk/news/world-middle-east-67528844",
    "https://www.bbc.co.uk/news/world-middle-east-67332684",
    "https://www.bbc.co.uk/news/live/world-middle-east-67364296",
    "https://www.bbc.co.uk/news/world-africa-67257862",
    "https://www.bbc.co.uk/news/world-middle-east-67535965",
    "https://www.bbc.co.uk/news/world-middle-east-67373293",
    "https://www.bbc.co.uk/news/world-middle-east-67493713",
    "https://www.bbc.co.uk/news/world-middle-east-67327079",
    "https://www.bbc.co.uk/news/world-middle-east-67361128",
    "https://www.bbc.co.uk/news/world-middle-east-67347201",
    "https://www.bbc.co.uk/news/world-middle-east-67084141",
    "https://www.bbc.co.uk/news/world-middle-east-67401064",
    "https://www.bbc.co.uk/news/live/world-middle-east-67423274",
    "https://www.bbc.co.uk/news/live/world-middle-east-67324897",
    "https://www.bbc.co.uk/news/live/world-middle-east-67481139",
    "https://www.bbc.co.uk/news/world-67418110",
    "https://www.bbc.co.uk/news/world-middle-east-67518819",
    "https://www.bbc.co.uk/news/world-middle-east-67550483",
    "https://www.bbc.co.uk/news/world-middle-east-67302206",
    "https://www.bbc.co.uk/news/world-middle-east-67520263",
    "https://www.bbc.co.uk/news/world-middle-east-67575684",
    "https://www.bbc.co.uk/news/world-middle-east-67463162",
    "https://www.bbc.co.uk/news/world-middle-east-67320520",
    "https://www.bbc.co.uk/news/world-middle-east-67528844",
    "https://www.bbc.co.uk/news/live/world-middle-east-67281166",
    "https://www.bbc.co.uk/news/world-middle-east-67554394",
    "https://www.bbc.co.uk/news/live/world-middle-east-67527098",
    "https://www.bbc.co.uk/news/world-middle-east-67339008",
    "https://www.bbc.co.uk/news/world-asia-china-67237146",
    "https://www.bbc.co.uk/news/business-67497299",
    "https://www.bbc.co.uk/news/world-middle-east-67331176",
    "https://www.bbc.co.uk/news/world-middle-east-67530181",
    "https://www.bbc.co.uk/news/live/world-middle-east-67400490",
    "https://www.bbc.co.uk/news/world-middle-east-67372035",
    "https://www.bbc.co.uk/news/world-middle-east-67372661",
    "https://www.bbc.co.uk/news/world-middle-east-67390375",

    # The Guardian links
    "https://www.theguardian.com/world/2023/nov/03/israel-and-palestine-a-complete-guide-to-the-crisis",
    "https://www.theguardian.com/world/2023/nov/06/israel-and-hamas-at-war-what-we-know-on-day-31",
    "https://www.theguardian.com/world/2023/nov/04/israel-palestine-is-the-two-state-solution-the-answer-to-the-crisis",
    "https://www.theguardian.com/commentisfree/2023/nov/08/israel-hamas-war-palestine-military-solutions-political-problems",
    "https://www.theguardian.com/world/2023/nov/03/israel-and-hamas-at-war-what-we-know-on-day-28",
    "https://www.theguardian.com/commentisfree/2023/nov/03/war-israel-hamas-conflict-peace-extremists",
    "https://www.theguardian.com/world/2023/nov/11/how-gaza-war-split-families-friends-colleagues-britain",
    "https://www.theguardian.com/world/2023/nov/08/gaza-palestine-family-israel-airstrike-survivors",
    "https://www.theguardian.com/commentisfree/2023/nov/02/israel-as-dark-as-things-seem-war-in-gaza-could-end-up-restarting-peace-process",
    "https://www.theguardian.com/books/2023/nov/13/the-wildly-divergent-histories-of-israel-palestine-that-have-climbed-us-bestseller-lists",
    "https://www.theguardian.com/world/2023/nov/08/israel-hamas-what-we-know-on-day-33",
    "https://www.theguardian.com/world/2023/nov/10/israel-hamas-war-what-we-know-on-day-35",
    "https://www.theguardian.com/world/2023/nov/12/experts-guide-to-the-israel-palestine-conflict",
    "https://www.theguardian.com/world/2023/nov/02/israel-and-hamas-at-war-what-we-know-on-day-27",
    "https://www.theguardian.com/world/2023/nov/22/israel-hamas-war-opens-up-german-debate-over-meaning-of-never-again",
    "https://www.theguardian.com/world/2023/nov/21/israel-hamas-war-is-deadliest-conflict-on-record-for-reporters-says-watchdog",
    "https://www.theguardian.com/commentisfree/2023/nov/13/israel-palestine-racism-antisemitism",
    "https://www.theguardian.com/commentisfree/2023/nov/03/a-two-state-solution-is-the-only-way-that-the-israel-palestine-problem-can-be-solved",
    "https://www.theguardian.com/commentisfree/2023/nov/29/war-gaza-egyptians-palestine-israel-hamas-protest-marches",
    "https://www.theguardian.com/world/2023/nov/04/israel-and-hamas-at-war-what-we-know-on-day-29",
    "https://www.theguardian.com/world/2023/nov/28/seeing-both-sides-in-the-middle-east-conflict-is-a-prerequisite-for-peace",
    "https://www.theguardian.com/world/2023/nov/13/israel-hamas-war-what-we-know-on-day-39",
    "https://www.theguardian.com/world/2023/nov/16/israel-under-pressure-as-us-questions-gaza-strategy-and-postwar-plans",
    "https://www.theguardian.com/world/live/2023/nov/20/israel-hamas-war-live-updates-hostages-al-shifa-hospital-gaza-hamas-attack",
    "https://www.theguardian.com/us-news/2023/nov/08/israel-cannot-reoccupy-gaza-at-end-of-conflict-says-antony-blinken",
    "https://www.theguardian.com/world/2023/nov/07/netanyahu-israel-consider-tactical-pauses-gaza",
    "https://www.theguardian.com/world/2023/nov/05/pressure-grows-for-gaza-ceasefire-as-israel-hamas-conflict-enters-fifth-week",
    "https://www.theguardian.com/us-news/2023/nov/09/columbia-university-israel-palestine-gaza-hamas-protest",
    "https://www.theguardian.com/politics/2023/nov/03/failed-to-be-a-critical-friend-uk-accused-of-taking-eye-off-israel-palestine-crisis",
    "https://www.theguardian.com/australia-news/2023/nov/14/more-australians-support-providing-assistance-to-palestinians-than-israel-in-gaza-conflict-essential-poll-finds",
    "https://www.theguardian.com/australia-news/2023/nov/16/australia-must-stop-giving-leeway-to-israels-continued-assault-on-gaza-un-expert-says",
    "https://www.theguardian.com/film/2023/nov/12/israelism-documentary-american-jewish-israel-palestine-conflict",
    "https://www.theguardian.com/world/live/2023/nov/05/israel-hamas-war-live-dozens-killed-in-strike-on-gaza-refugee-camp-say-palestinians-protests-around-world-demand-ceasefire?filterKeyEvents=false&page=with%3Ablock-654785de8f08d1827a66c833",
    "https://www.theguardian.com/world/live/2023/nov/06/israel-hamas-war-live-updates-jordan-airdrops-medical-supplies-gaza-blinken-turkey-push-contain-conflict?filterKeyEvents=false&page=with%3Ablock-6548eb6f8f08af73b5ca99ef",
    "https://www.theguardian.com/commentisfree/2023/nov/02/gaza-israel-war-middle-east-united-states-russia-china-iran",
    "https://www.theguardian.com/commentisfree/2023/nov/20/leftwing-jew-show-support-israelis-and-palestinians",
    "https://www.theguardian.com/commentisfree/2023/nov/01/the-guardian-view-on-gaza-after-the-war-there-must-be-a-plan-for-the-future-of-palestinians",
    "https://www.theguardian.com/world/live/2023/nov/13/israel-hamas-war-live-updates-al-shifa-hospital-who-us-strikes-syria-palestine?page=with%3Ablock-655223458f08ea44fe1a95de",
    "https://www.theguardian.com/world/2023/nov/30/israel-hamas-war-ceasefire-extension-one-day-details-gaza-hostages-palestine",
    "https://www.theguardian.com/australia-news/2023/nov/04/penny-wong-israel-must-listen-to-calls-for-restraint-from-its-friends-or-it-risks-gaza-conflict-spreading",
    "https://www.theguardian.com/world/live/2023/nov/11/israel-hamas-war-live-staff-report-catastrophic-situation-in-main-gaza-hospital-aid-agency-says-as-fighting-intensifies?filterKeyEvents=false&page=with%3Ablock-654f24798f08c3ba45a5111f",
   
    #The Telegraph links
    "https://www.telegraph.co.uk/news/2023/11/04/israel-hamas-palestine-war-friendships-relationships-strain/",
    "https://www.telegraph.co.uk/news/2023/11/27/hating-israel-will-not-free-palestine/",
    "https://www.telegraph.co.uk/news/2023/11/23/bbc-own-reporters-accuse-it-of-favouritism-towards-israel/",
    "https://www.telegraph.co.uk/news/2023/11/19/bbc-diplomatic-correspondent-pro-palestinian-bias/",
    "https://www.telegraph.co.uk/news/2023/11/25/bbc-biased-towards-israel-you-must-be-joking/",
    "https://www.telegraph.co.uk/news/2023/11/03/bbc-question-time-audience-israel-gaza-final-solution/",
    "https://www.telegraph.co.uk/news/2023/11/07/people-dont-seem-to-care-about-the-massacre-of-jews/",
    "https://www.telegraph.co.uk/news/2023/11/09/protesters-pro-palestine-march-not-sure-hamas-invade-israel/",
    "https://www.telegraph.co.uk/news/2023/11/17/irans-betrayal-leaves-hamas-with-nowhere-to-go/",
    "https://www.telegraph.co.uk/news/2023/11/09/layla-moran-palestinian-mp-lib-dem-israel-gaza/",
    "https://www.telegraph.co.uk/news/2023/11/29/bbc-asian-network-stars-social-media-posts-israel-hamas-war/",
    "https://www.telegraph.co.uk/news/2023/11/11/hamas-leader-pronounced-masterminded-gaza-attacks/",
    "https://www.telegraph.co.uk/news/2023/11/10/iran-irgc-israel-hamas-gaza-saudi-arab-muslim-brotherhood/",
    "https://www.telegraph.co.uk/news/2023/11/18/exeter-professor-admires-courage-hamas/",
    "https://www.telegraph.co.uk/news/2023/11/24/bbc-rejects-complaints-reporting-israel-hamas-war/",
    "https://www.telegraph.co.uk/news/2023/11/26/i-warned-the-bbc-it-was-spreading-hamas-propaganda-it-refus/",
    "https://www.telegraph.co.uk/news/2023/11/04/jew-hating-hypocrisy-protesters-strongest-case-for-israel/",
    "https://www.telegraph.co.uk/news/2023/11/07/gaza-war-israel-left-wing-antisemitism/",
    "https://www.telegraph.co.uk/news/2023/11/01/leaving-guardian-over-hamas-coverage/",
    "https://www.telegraph.co.uk/news/2023/11/06/former-hamas-chief-behind-pro-palestine-armistice-day-march/",
    "https://www.telegraph.co.uk/news/2023/11/29/the-uns-silence-on-the-rape-of-israeli-women-makes-a-mocker/",
    "https://www.telegraph.co.uk/news/2023/11/07/bbc-hamas-kirsty-young-palestine-israel-gaza-terrorist/",
    "https://www.telegraph.co.uk/news/2023/11/15/bbc-apologises-newsreader-claims-idf-targeting-medics-gaza/",
    "https://www.telegraph.co.uk/news/2023/11/11/protesters-extreme-anti-semitic-signs-pro-palestinian-march/",
    "https://www.telegraph.co.uk/news/2023/11/07/israel-running-out-of-time-before-biden-damns-it-to-defeat/",
    "https://www.telegraph.co.uk/news/2023/11/14/pro-palestine-protests-uk-gaza-ceasefire-israel-hamas-war/",
    "https://www.telegraph.co.uk/news/2023/11/02/arab-leaders-dont-care-about-the-palestinians/",
    "https://www.telegraph.co.uk/news/2023/11/04/israel-palestine-protest-london-march-today-live/",
    "https://www.telegraph.co.uk/news/2023/11/02/ireland-has-shamed-itself-again-over-israel/",
    "https://www.telegraph.co.uk/news/2023/11/11/sadiq-khan-advisers-israel-settler-colonialism-genocide/",
    "https://www.telegraph.co.uk/news/2023/11/06/bbc-must-publish-israel-bias-report-suppressed-for-10-years/",
    "https://www.telegraph.co.uk/news/2023/11/18/proscribe-call-palestinian-return-centre-hamas-link-claim/",
    "https://www.telegraph.co.uk/news/2023/11/29/israel-hamas-bbcs-reputation-will-be-hard-to-repair/",
    "https://www.telegraph.co.uk/news/2023/11/24/eric-salama-comic-relief-crisis-chairman-quits-gaza-israel/",
    "https://www.telegraph.co.uk/news/2023/11/09/queers-for-palestine-must-have-a-death-wish/",
    "https://www.telegraph.co.uk/news/2023/11/18/corbyn-mcdonnell-palestine-march-hamas-activist-hmidan/",
    "https://www.telegraph.co.uk/news/2023/11/10/jonathan-hall-kc-interview-terrorism-cenotaph/",
    "https://www.telegraph.co.uk/news/2023/11/25/london-palestine-march-met-warning-hate-speech/",
    "https://www.telegraph.co.uk/news/2023/11/16/britain-new-capital-anti-israel-hate/",
    "https://www.telegraph.co.uk/news/2023/11/24/police-leaflets-palestinian-protests-london-chants-arrests"]

# CSV file to save the output
output_file = "news_articles.csv"

# Open the CSV file for writing
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(["Article", "News_Source", "Title", "Published_Date", "Authors", "Keywords", "Summary", "Text"])


for index, url in enumerate(urls, start=1):
    try:
        article = newspaper.Article(url=url, language='en')
        article.download()
        article.parse()
        article.nlp()

        source = url.split("//")[-1].split("/")[0]

        article_data = [
            f"Article {index}",
            source,
            article.title,
            str(article.publish_date),
            ", ".join(article.authors),
            ", ".join(article.keywords),
            article.summary,
            article.text
        ]
        
        with open(output_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(article_data)
    
    except Exception as e:
        print(f"Error processing article {index} ({url}): {e}")

 
        # Write article data to the CSV file
        writer.writerow(article_data)

print(f"Article data has been written to '{output_file}'.")