from google.cloud import dialogflowcx_v3
import sys, getopt

def main(argv):
    id = ''
    region = 'europe-west1'
    intent = '4fd93788-fda8-4f3e-abc0-848185af74b0'
    
    try:
       opts, args = getopt.getopt(argv,"hi:r:t:",["id=", "region=", "intent="])
    except getopt.GetoptError:
       print('export-agent.py -i <agent-id> -r <region> -t <intent-id>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print('export-agent.py -i <agent-id> -r <region> -t <intent-id>')
          sys.exit()
       elif opt in ("-i", "--id"):
          id = arg
       elif opt in ("-r", "--region"):
          region = arg
       elif opt in ("-t", "--intent"):
          intent = arg
    
    if id:
        print(f'exporting agent {id}')
    else:
        print("please provide agent-id as: -i <agent-id> (id not agent name!)")
    
    # Create a client
    client_options = {"api_endpoint": f"{region}-dialogflow.googleapis.com:443"}
    client = dialogflowcx_v3.IntentsClient(client_options=client_options)

    # Initialize request argument(s)
    request = dialogflowcx_v3.GetIntentRequest(
        name=f"projects/dialogflow-test-db/locations/{region}/agents/{id}/intents/{intent}",
    )

    # Make the request
    response = client.get_intent(request=request)

    # Handle the response
    print(response.training_phrases)
    
    
if __name__ == "__main__":
   main( sys.argv[1:])