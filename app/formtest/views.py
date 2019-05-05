from flask import abort, render_template, request
from .. import db
from ..models import Book
from . import formtest

@formtest.route('/formtest', methods=['POST', 'GET'])
def formTest():
    if request.form:
        book = Book(title=request.form.get("title"))
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template('formtest.html', books=books)