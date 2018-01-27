from facebookads.adobjects.campaign import Campaign
from facebookads import FacebookSession
from facebookads import FacebookAdsApi
import json

class FacebookOps:

    def obtain_fb_api(self):
        """
        Returns FB api in order to use the services from the FB sdk.
        :return:
        FB api
        """
        try:

            print("     >>> Abriendo archivo de credenciales...")

            cred_file = 'credentials.json'
            with open('/home/sebasgona/Documents/proyecto_fintech/fintech' + cred_file) as credentials_json:
                credentials = json.load(credentials_json)

            session = FacebookSession(credentials['app_id'], credentials['app_secret'], credentials['access_token'])
            api = FacebookAdsApi(session)
            print("     >>> Obteniendo FB API...")
            return api
        except Exception as e:
            print("     >>> ERROR al obtener FB API: \n\n" + str(e))
            return None

