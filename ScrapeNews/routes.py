from ScrapeNews import app
from flask import render_template,request, redirect, jsonify
from newspaper import Article
import newspaper
from ScrapeNews.models import UpToDateNews
from ScrapeNews.models import db
from newspaper import Config
import json, jsonpickle
newss=[]
s=[]

# @app.route('/searchnews', methods=['POST','GET'])
# def appearSearchBox():
#     isAppear=True
#     return render_template('newsApp.html', isAppear=isAppear)

# @app.route('/searchednews', methods=['POST','GET'])
# def search():
#     text = request.args.get('news')
#     newss=ScrapeNews.query.filter(ScrapeNews.newsTitle.startswith(text)).all()
#     for new in newss:
#         if text in new.newsTitle:
#             s.push(new)
    
#     return render_template('searchedNews.html', news=s)

@app.route('/', methods=['POST','GET'])
def index():
    Title=""
    config = Config()
    config.request_timeout = 60
    if request.method == 'POST':
        db.create_all()
        samaaArticles = newspaper.build('https://www.parhlo.com/viral/', config=config)
        for articles in samaaArticles.articles[0:10]:
            articles.download()
            articles.parse()
            Title = articles.title
            Text = articles.text
            Image = articles.top_image
            Url = articles.url
            newArticle= UpToDateNews(newsTitle=Title, newsText=Text,newsImage=Image, newsUrl=Url)
            db.session.add(newArticle)
            db.session.commit()

        samaaArticles = newspaper.build('https://www.samaaenglish.tv/', config=config)
        for articles in samaaArticles.articles[0:10]:
            articles.download()
            articles.parse()
            Title = articles.title
            Text = articles.text
            Image = articles.top_image
            Url = articles.url
            newArticle= UpToDateNews(newsTitle=Title, newsText=Text,newsImage=Image, newsUrl=Url)
            db.session.add(newArticle)
            db.session.commit()

        geoArticles = newspaper.build('https://www.geo.tv/latest-news')
        for articles in geoArticles.articles[0:10]:
            articles.download()
            articles.parse()
            Title = articles.title
            Text = articles.text
            Image = articles.top_image
            Url = articles.url
            newArticle= UpToDateNews(newsTitle=Title,newsText=Text, newsImage=Image, newsUrl=Url)
            db.session.add(newArticle)
            db.session.commit()

        expressArticles = newspaper.build('https://www.express.pk/', config=config)
        for articles in expressArticles.articles[0:10]:
            articles.download()
            articles.parse()
            Title = articles.title
            Text = articles.text
            Image = articles.top_image
            Url = articles.url
            newArticle= UpToDateNews(newsTitle=Title,newsText=Text, newsImage=Image, newsUrl=Url)

            db.session.add(newArticle)
            db.session.commit()

        expressArticles = newspaper.build('https://dunyanews.tv/', config=config)
        for articles in expressArticles.articles[0:10]:
            articles.download()
            articles.parse()
            Title = articles.title
            Text = articles.text
            Image = articles.top_image
            Url = articles.url
            newArticle= UpToDateNews(newsTitle=Title,newsText=Text, newsImage=Image, newsUrl=Url)

            db.session.add(newArticle)
            db.session.commit()

        expressArticles = newspaper.build('https://arynews.tv/')
        for articles in expressArticles.articles[0:10]:
            articles.download()
            articles.parse()
            Title = articles.title
            Text = articles.text
            Image = articles.top_image
            Url = articles.url
            newArticle= UpToDateNews(newsTitle=Title,newsText=Text, newsImage=Image, newsUrl=Url)

            db.session.add(newArticle)
            db.session.commit()
        return redirect('/')

    # except:
    #     return render_template('error.html')
    task = UpToDateNews.query.order_by(UpToDateNews.date_created).all()
    return render_template('newsApp.html', tasks=task)
    # return jsonpickle.encode(task)


@app.route('/getallnews', methods=['GET'])
def getallnews():
    try:
        # jsonify(UpToDateNews.query.order_by(UpToDateNews.date_created).all())
        newss=UpToDateNews.query.order_by(UpToDateNews.date_created).all()
        # return render_template("market.html", newss=newss)
        # return jsonify({"data":newss})
        res_list = list(enumerate(newss))
        return jsonpickle.encode(newss)

        # return json.dumps(newss)
    except:
        return "There was a problem scraping your scrapped data"


@app.route('/delete/<int:id>')
def delete(id):
    new_to_delete = UpToDateNews.query.get_or_404(id)

    try:
        db.session.delete(new_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting your scrapped data"

@app.route('/deleteall/')
def deleteall():
    try:
        db.session.query(UpToDateNews).delete()
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting your scrapped data"

@app.route('/market')
def market():
    items = [
        {'id':1, 'name':'Mobile Phone', 'price':'$500', 'item_code':'##############'},
        {'id':2, 'name':'Spoons', 'price':'$50', 'item_code':'##############'},
        {'id':3, 'name':'Soap', 'price':'$40', 'item_code':'##############'},
        {'id':4, 'name':'Brush', 'price':'$30', 'item_code':'##############'},
    ]
    return render_template('market.html', item_name=items)