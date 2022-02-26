var json_data='{"a": 1, "b": 2, "c": 3}'
console.log(json_data) // '{"a": 1, "b": 2, "c": 3}'
console.log(typeof(json_data)) // 'string'

var js_obj=JSON.parse(json_data)
console.log(js_data) // {a: 1, b: 2, c: 3}
console.log(typeof(js_obj)) // 'object'

var back_to_json=JSON.stringify(js_obj)
console.log(back_to_json) // '{"a":1,"b":2,"c":3}'
console.log(typeof(back_to_json)) // 'string'
