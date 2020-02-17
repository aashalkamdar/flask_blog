from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
	page = request.args.get('page',1,type=int)#1 is the default page, int is set cause if someone passes anything else then error
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=5)
	return render_template('home.html',posts = posts)

@main.route('/about')
def about():
	return render_template('about.html',title = 'About')


