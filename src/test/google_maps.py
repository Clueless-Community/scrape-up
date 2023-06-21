from scrape_up.google_maps import GoogleMaps


def test_google_maps():
    #write a test for google maps

    #create a google maps object
    google_maps = GoogleMaps()

    #search for a business
    google_maps.search_for_business('dentist new york')

    #get the business list
    business_list = google_maps.get_business_list()

    #save the business list to excel
    business_list.save_to_excel('google_maps_data')


if __name__ == "__main__":
    test_google_maps()
    