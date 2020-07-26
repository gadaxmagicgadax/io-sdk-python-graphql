# Importer for graphql queries

This importer has been developed and tested in combination with a graphql server esposing queries on mysql database. Please have a look to : [https://github.com/gadaxmagicgadax/graphql4iosdk](https://github.com/gadaxmagicgadax/graphql4iosdk)

Just clone this repository and run build.sh to deploy the importer action in iosdk.

## Formatting data

Query result from graphql is not ready to be returned to iosdk. This format :

```
{
"data": {
"messages": [
{
"amount": 0,
"due_date": "2024-05-21",
"fiscal_code": "SUZPET23T58F284T",
"invalid_after_due_date": "false",
"markdown": "please check the expiration date of your payments is : 2024-05-21",
"notice_number": 1,
"subject": "Payment expiration date - Comune di Apirilia"
},
......
```

must be converted in :

```
{
"data":  [
{
"amount": 0,
"due_date": "2024-05-21",
"fiscal_code": "SUZPET23T58F284T",
"invalid_after_due_date": "false",
"markdown": "please check the expiration date of your payments is : 2024-05-21",
"notice_number": 1,
"subject": "Payment expiration date - Comune di Apirilia"
},
......
```

So , the result of the API query has been rolled in a new array and then returned in the proper format with :

```
new_json_data = []

        for item in json_data['data']['messages']:
                new_json_data.append(item)

        return {"body": { "data": new_json_data} }
```

Maybe there is a more "elegant" way to reformat a json. If you have an idea just let me know.
