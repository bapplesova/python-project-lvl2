right_answer = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

right_nested_answer = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
    group4: {
      - default: null
      + default:
      - foo: 0
      + foo: null
      - isNested: false
      + isNested: none
      + key: false
        nest: {
          - bar:
          + bar: 0
          - isNested: true
        }
      + someKey: true
      - type: bas
      + type: bar
    }
}'''

right_t_json_answer = '''{"group1": {"   setting1": "Value 1"," - setting2": 200," + setting2": 2," + setting3": true," + setting4": false,"   setting6": {"   key": "value"}," - setting7": {"   key7": false}}}'''

right_plain = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''

right_plain_nested = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From 'too much' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
Property 'group4.default' was updated. From null to ''
Property 'group4.foo' was updated. From 0 to null
Property 'group4.isNested' was updated. From false to 'none'
Property 'group4.key' was added with value: false
Property 'group4.nest.bar' was updated. From '' to 0
Property 'group4.nest.isNested' was removed
Property 'group4.someKey' was added with value: true
Property 'group4.type' was updated. From 'bas' to 'bar\''''

right_json = '''{" - follow": false,"   host": "hexlet.io"," - proxy": "123.234.53.22"," - timeout": 50," + timeout": 20," + verbose": true}'''

right_json_nested = '''{"common": {" + follow": false,"   setting1": "Value 1"," - setting2": 200," - setting3": true," + setting3": {"   key": "value"}," + setting4": "blah blah"," + setting5": {"   key5": "value5"},"setting6": {"doge": {" - wow": "too much"," + wow": "so much"},"   key": "value"," + ops": "vops"}},"group1": {" - baz": "bas"," + baz": "bars","   foo": "bar"," - nest": {"   key": "value"}," + nest": "str"}," - group2": {"   abc": 12345,"deep": {"   id": 45}}," + group3": {"deep": {"id": {"   number": 45}},"   fee": 100500},"group4": {" - default": null," + default": ""," - foo": 0," + foo": null," - isNested": false," + isNested": "none"," + key": false,"nest": {" - bar": ""," + bar": 0," - isNested": true}," + someKey": true," - type": "bas"," + type": "bar"}}'''
