from flask import Blueprint, render_template, request
from forms import ComposeForm

compose = Blueprint('compose', __name__, static_folder='./public', template_folder='./public/html')

@compose.route('/Compose.html', methods=['GET'])
def compose_page():
    form = ComposeForm()
    receiver_id = request.args.get('receiver_id')  # Get receiver ID from query parameter
    form.receiver_id.data = receiver_id  # Prepopulate the receiver_id field in the form

    return render_template('Compose.html', form=form, receiver_id=receiver_id)
