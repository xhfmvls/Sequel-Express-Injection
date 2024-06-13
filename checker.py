import json
import quanchecker

urls = ["http://localhost:(port)/items"]

headers = [{
  'Content-Type': 'application/json'
}]

test_cases = [
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "item_name": "Item 1"
        }),
        'expected': {'items': [{'id': 1, 'name': 'Item 1', 'description': 'Description for Item 1'}]},
    },
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "item_name": "Item 6%"
        }),
        'expected': {'items': [{'id': 6, 'name': 'Item 6%', 'description': 'A versatile and innovative product with a touch of mystery, perfect for the modern adventurer'}]},
    },
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "item_name": "' OR 1=1;#"
        }),
        'expected': {'error': 'Item not found!'},
    },
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "item_name": "' OR 1 LIKE 1;#"
        }),
        'expected': {'error': 'Item not found!'},
    }
]

quanchecker.run_tests_dev(test_cases)
