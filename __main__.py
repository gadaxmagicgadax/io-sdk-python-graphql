import requests
import json

def main(args):

	import config
	
	query = """
	query {
	messages {
	amount
	due_date: dueDate
	fiscal_code: fiscalCode
	invalid_after_due_date: invalidAfterDueDate
	markdown
	notice_number:noticeNumber
	subject
	}
	}
	"""

	url = args.get("url") if args.get("url") else 'http://192.168.1.124:8000/graphql/'
	if args.get("url") == None:
		print(config.emptyForm)
		json_data = json.loads(config.emptyForm)
		print(json_data)
		return {"body": json_data}

	try:
		r = requests.post(args.get("url"), json={'query': query})
	except requests.exceptions.RequestException as e:
		res = {}
		res.update(data = str(e))
		json_result = json.dumps(res)
		print(json_result)
		return {"body": json_result}

	json_data = json.loads(r.text)

	# recreate the json collection to create an array to return to iosdk

	new_json_data = []

	for item in json_data['data']['messages']:
		new_json_data.append(item)

	return {"body": { "data": new_json_data} }

if __name__ == "__main__":
   r = main({"url": "http://192.168.1.124:8000/graphql/"})
   print(json.dumps(r, indent=4))
