from flask import (
    render_template,
    redirect,
    Blueprint,
    url_for,
    flash,
    request,
)
from .forms import SendForm
from .utils import (
    get_distance,
    get_location,
)
import logging.config

logging.config.fileConfig('myapp/logging.conf')
logger = logging.getLogger('loggerDistance')

main = Blueprint('main', __name__, template_folder='templates', url_prefix='/')


@main.route("/", methods=['GET', 'POST'])
def home():
    tittle = 'Home | Distance from MKAD'
    form = SendForm()
    counter = []
    if request.method == 'POST':
        if form.validate_on_submit():

            address = form.address.data
            city = form.city.data
            geo_location = get_location(address, city)
            try:
                distance = get_distance(geo_location)
                if distance <= 0:
                    flash(f'Your address {address}, {city}, is inside of MOSCOW RING ROAD.')
                else:
                    flash(f'Your address {address}, {city}, is {distance:.0f} KM away from MOSCOW RING ROAD.')

                logger.info(f'{address}, {city}, {geo_location.get("latitude")}, '
                            f'{geo_location.get("longitude")}, {distance:.2f}')

            except Exception as err:
                print(err)
                distance = '0'
                logger.error(f'error: {err}')

            return redirect(url_for('main.home'))

    return render_template('main/home.html', form=form, tittle=tittle)
