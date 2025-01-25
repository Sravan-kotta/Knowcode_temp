from pyinaturalist import get_observations
from pyinaturalist import get_places_autocomplete
import requests
from ete3 import NCBITaxa


def species(latitude, longitude, radius):


    response = get_observations(
        lat=latitude,
        lng=longitude,
        radius=radius,
        order='desc',
        order_by='created_at'
    )


    species_list = set()
    for obs in response['results']:
        if 'taxon' in obs and obs['taxon']:
            species_list.add(obs['taxon']['name'])

    return species_list

def endangered_species(genus, species):
    url1 = f"https://api.iucnredlist.org/api/v4/taxa/scientific_name?genus_name={genus}&species_name=%20{species}"
    headers = {
        "accept": "application/json",
        "Authorization": "XZEAWUn3f5fty6W5YgJLmQsrkB7XFUEchBBL"  # Replace with your actual API key
    }

    # Make the GET request
    response = requests.get(url1, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data['assessments'] == []:
            return "insufficient data"
        else:
            ass_id = data['assessments'][0]['assessment_id']
        
    else:
        return f"Error: {response.status_code}, {response.text}"

    url2 = f"https://api.iucnredlist.org/api/v4/assessment/{ass_id}"
    response = requests.get(url2, headers=headers)

    if response.status_code == 200:
        data = response.json()
        status = data['red_list_category']['description']['en']
        return status
    else:
        return f"Error: {response.status_code}, {response.text}"