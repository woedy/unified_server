import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_random_otp_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


def unique_user_id_generator(instance):
    """
    This is for a django project with a user_id field
    :param instance:
    :return:
    """

    size = random.randint(30,45)
    user_id = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(user_id=user_id).exists()
    if qs_exists:
        return
    return user_id


def unique_event_id_generator(instance):
    """
    This is for an event_id field
    :param instance:
    :return:
    """
    size = random.randint(5, 7)
    event_id = "UPA-" + random_string_generator(size=size, chars=string.ascii_uppercase + string.digits) + "-(ev)"

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(event_id=event_id).exists()
    if qs_exists:
        return None
    return event_id
def unique_game_id_generator(instance):
    """
    This is for a game_id field
    :param instance:
    :return:
    """
    size = random.randint(5, 7)
    game_id = "UPA-" + random_string_generator(size=size, chars=string.ascii_uppercase + string.digits) + "-(gm)"

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(game_id=game_id).exists()
    if qs_exists:
        return None
    return game_id

def unique_round_id_generator(instance):
    """
    This is for a round_id field
    :param instance:
    :return:
    """
    size = random.randint(5, 7)
    round_id = "UPA-" + random_string_generator(size=size, chars=string.ascii_uppercase + string.digits) + "-(rd)"

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(round_id=round_id).exists()
    if qs_exists:
        return None
    return round_id


def unique_league_id_generator(instance):
    """
    This is for an league_id field
    :param instance:
    :return:
    """
    size = random.randint(5, 7)
    league_id = "UPA-" + random_string_generator(size=size, chars=string.ascii_uppercase + string.digits) + "-(LG)"

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(league_id=league_id).exists()
    if qs_exists:
        return None
    return league_id

def unique_team_id_generator(instance):
    """
    This is for a team_id field
    :param instance:
    :return:
    """
    size = random.randint(5, 7)
    team_id = "UPA-" + random_string_generator(size=size, chars=string.ascii_uppercase + string.digits) + "-(TM)"

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(team_id=team_id).exists()
    if qs_exists:
        return None
    return team_id


def generate_email_token():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code
