from itertools import chain

cars = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
    (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return list(first_model[0] for first_model in cars.values())


def get_all_matching_models(cars=cars, grep="trail"):
    """return a list of all models containing the case insensitive
    'grep' string which defaults to 'trail' for this exercise,
    sort the resulting sequence alphabetically"""
    all_models = list(chain.from_iterable(cars.values()))
    matching_models = [model for model in all_models if grep.lower() in model.lower()]
    return sorted(matching_models)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
    sorted alphabetically"""
    return {make: sorted(model) for make, model in cars.items()}
