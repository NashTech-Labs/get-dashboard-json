from grafana_api.grafana_face import GrafanaFace
import os
from grafanalib._gen import DashboardEncoder
import json
import requests

def _get_grafana_client(auth=os.getenv('GRAFANA_API_TOKEN','None'),host=os.getenv('GRAFANA_HOST','localhost:3000')):
    grafana_client = GrafanaFace(
                    auth=auth, 
                    host=host
                )
    return grafana_client
def get_dashboard_json(dashboard, overwrite=False, message="Updated by grafanlib"):
    return json.dumps(

        {
            "dashboard": dashboard,
            "overwrite": overwrite,
            "message": message
        }, sort_keys=True, indent=2, cls=DashboardEncoder)

