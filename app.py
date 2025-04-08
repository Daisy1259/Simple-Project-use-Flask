from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import os

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# 定义文章模型
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 添加创建时间字段
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Article {self.title}>'


# 创建数据库表并插入初始数据
with app.app_context():
    db.create_all()
    # 检查数据库中是否已有文章数据
    if Article.query.count() == 0:
        initial_articles = [
            {'title': 'Python Flask入门', 'content': '本文将带您从入门到实战，深入了解Flask。'},
            {'title': 'Flask扩展介绍', 'content': '本文将介绍Flask的一些常用扩展。'}
        ]
        for article in initial_articles:
            new_article = Article(title=article['title'], content=article['content'])
            db.session.add(new_article)
        db.session.commit()


@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)


@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)


@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    content = request.form['content']
    new_article = Article(title=title, content=content)
    db.session.add(new_article)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:article_id>', methods=['POST'])
def delete(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:article_id>', methods=['GET', 'POST'])
def edit(article_id):
    article = Article.query.get_or_404(article_id)
    if request.method == 'POST':
        try:
            article.title = request.form['title']
            article.content = request.form['content']
            db.session.commit()
            return redirect(url_for('article', article_id=article_id))
        except Exception as e:
            print(f"更新文章时出错：{e}")
            db.session.rollback()
    return render_template('edit.html', article=article)


if __name__ == '__main__':
    app.run(debug=True)
