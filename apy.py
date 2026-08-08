import boto3

# Initialize the API Gateway client
client = boto3.client('apigateway')
secret_key_to_find = "PFqSIziHxbcPASoAPF64N6Fg0a1Q9exaXuChMFr/"

# 1. Find the API Key ID from the raw secret string
api_keys = client.get_api_keys(includeValues=True)
print(f"Retrieved {len(api_keys.get('items', []))} API keys from AWS account.")
# target_key_id = None

# for key in api_keys.get('items', []):
#     if key.get('value') == secret_key_to_find:
#         target_key_id = key['id']
#         print(f"Found matching API Key ID: {target_key_id}")
#         break

# if not target_key_id:
#     print("Secret key value not found in this AWS account region.")
#     exit()

# # 2. Find Usage Plans associated with this API Key
# usage_plans = client.get_usage_plans(keyId=target_key_id)

# # 3. Extract API IDs and delete the APIs completely
# for plan in usage_plans.get('items', []):
#     stages = plan.get('apiStages', [])
#     for stage in stages:
#         api_id = stage['apiId']
#         try:
#             print(f"Deleting API ID: {api_id} associated with Usage Plan: {plan['name']}")
#             client.delete_rest_api(restApiId=api_id)
#             print(f"Successfully deleted API: {api_id}")
#         except Exception as e:
#             print(f"Could not delete API {api_id}: {str(e)}")

# # 4. Cleanup the key itself
# client.delete_api_key(apiKey=target_key_id)
# print("Process complete.")
