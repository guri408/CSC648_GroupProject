from flask import Blueprint, render_template, request
from forms import ComposeForm
from flask_login import current_user, login_required
import logging

compose = Blueprint('compose', __name__, static_folder='./public', template_folder='./public/html')

@compose.route('/Compose.html', methods=['GET'])
@login_required
def compose_page():
    form = ComposeForm()
    receiver_id = request.args.get('receiver_id')  # Get receiver ID from query parameter
    listing_id = request.args.get('listing_id')  # Get listing ID from query parameter
    form.receiver_id.data = receiver_id  # Prepopulate the receiver_id field in the form
    form.listing_id.data = listing_id  # Prepopulate the listing_id field in the form

    return render_template('Compose.html', form=form, receiver_id=receiver_id, listing_id=listing_id)
