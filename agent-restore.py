from google.cloud import dialogflowcx_v3
import sys, getopt

def main(argv):
    id = ''
    region = 'europe-west1'
    
    try:
       opts, args = getopt.getopt(argv,"hi:r:",["id=", "region="])
    except getopt.GetoptError:
       print('restore-agent.py -i <agent-id> -r <region>')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print('restore-agent.py -i <agent-id> -r <region>')
          sys.exit()
       elif opt in ("-i", "--id"):
          id = arg
       elif opt in ("-r", "--region"):
          region = arg
    
    if id:
        print(f'restoring agent {id}')
    else:
        print("please provide agent-id as: -i <agent-id> (id not agent name!)")
    
    # Create a client
    client_options = {"api_endpoint": f"{region}-dialogflow.googleapis.com:443"}
    client = dialogflowcx_v3.AgentsClient(client_options=client_options)

    # Initialize request argument(s)
    request = dialogflowcx_v3.RestoreAgentRequest(
        agent_uri="gs://agent-export/dialogflow-agent.blob",
        name=f"projects/dialogflow-test-db/locations/{region}/agents/{id}",
    )

    # Make the request
    operation = client.restore_agent(request=request)    

    print("Waiting for operation to complete...")

    response = operation.result()    

    print("agent restored")
    
if __name__ == "__main__":
   main( sys.argv[1:])