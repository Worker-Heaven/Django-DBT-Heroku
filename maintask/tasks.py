from background_task import background
from logging import getLogger

from .models import Name
import random

logger = getLogger(__name__)

@background(schedule=1)
def demo_task(message):
    print('message------>', message)
    # logger.debug('demo_task. message={0}'.format(message))

    new_person = Name()
    new_person.name = 'Random Name' + str(random.randint(1, 10000))

    new_person.save()