from flask import (
    Blueprint, flash, render_template, request
)

from app.db import get_db

bp = Blueprint('add_things', __name__, url_prefix='')

@bp.route('/add', methods=('GET', 'POST'))
def add_thing():
    if request.method == 'POST':
        thing = request.form['thing']
        nickname = request.form['thing']
        db = get_db()
        error = None

        if not thing:
            error = 'A thing is required.'
        elif not nickname:
            error = 'A nickname for this thing is required.'
        elif db.execute(
            'SELECT id FROM things WHERE thing = ?', (thing,)
        ).fetchone() is not None:
            error = 'This thing 👉 {} is already registered.'.format(thing)
        
        if error is None:
            db.execute(
                'INSERT INTO things (thing, nickname) VALUES (?, ?)',
                (thing, nickname)
            )
            db.commit()
        
        all_things_obj = db.execute(
            'SELECT * FROM things'
        ).fetchall()
        
        all_things = []
        for thing in all_things_obj:
            all_things.append(thing[1])

        flash(error)

    return render_template('things/register.html', all_things=all_things)