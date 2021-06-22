from . import main
from ..requests import get_quote
import os
import secrets
from PIL import Image
from flask import  render_template,redirect,url_for,request,flash,abort
from flask_login import login_required,current_user
from .. import db
from .forms import UpdateForm,PostForm,CommentsForm
from ..models import Post,Comment

@main.route("/")
@main.route("/index")
def index():
    quote = get_quote()
    

    posts = Post.query.order_by(Post.date_posted.desc())
    
    return render_template('index.html', posts=posts, quote=quote)
   
@main.route('/about')
def about():
    return render_template('about.html',title='about')


def save_picture(form_picture):
    #returns filename and extension itself
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('app/static/photos',picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)


    i.save(picture_path)

    return picture_fn



@main.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file  = picture_file

        current_user.username =form.username.data
        current_user.email =form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'primary')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

            
    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@main.route('/post/new',  methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title= form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'primary')
        return redirect(url_for('main.index'))
    return render_template('create_post.html',title='New Post', form=form, legend ='NewPost')

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@main.route("/post/<int:post_id>/update",methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'primary')
        return redirect(url_for('main.post',post_id =post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post .content
    return render_template('create_post.html', title='Update Post', legend ='Update Post', form=form)


@main.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'primary')
    return redirect(url_for('main.index'))


@main.route('/comment',  methods=['GET', 'POST'])
def comment():
    # post = Post.query.get_or_404()
    # content  = Comment.query.get_or_404()
    form = CommentsForm()
    if form.validate_on_submit():
        content = form.content.data
        form.content.data = ""
        new_comment = Comment(content=content ,user_id=current_user.id,post_id=post.post_id)
        db.session.add(new_comment)
        db.session.commit()
        # return redirect(url_for('auth.index'))
        return redirect(url_for(".comment", id=post.id))

    return render_template('comments.html', form=form )

      


