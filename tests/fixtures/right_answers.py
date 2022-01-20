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
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
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
}'''

right_t_answer = '''{
    group1: {
        setting1: Value 1
      - setting2: 200
      + setting2: 2
      - setting3: true
      + setting4: false
        setting6: {
            key: value
        }
      - setting7: {
            key7: false
        }
    }
}'''

right_t_json_answer = '''{"group1": {"   setting1": "Value 1"," - setting2": 200," + setting2": 2," + setting3": true," + setting4": false,"   setting6": {"   key": "value"}," - setting7": {"   key7": false}}}'''

right_plain = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''

right_plain_nested = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

right_json = '''{" - follow": false,"   host": "hexlet.io"," - proxy": "123.234.53.22"," - timeout": 50," + timeout": 20," + verbose": true}'''

right_json_nested = '''{"common": {" + follow": false,"   setting1": "Value 1"," - setting2": 200," - setting3": true," + setting3": null," + setting4": "blah blah"," + setting5": {"   key5": "value5"},"setting6": {"doge": {" - wow": ""," + wow": "so much"},"   key": "value"," + ops": "vops"}},"group1": {" - baz": "bas"," + baz": "bars","   foo": "bar"," - nest": {"   key": "value"}," + nest": "str"}," - group2": {"   abc": 12345,"deep": {"   id": 45}}," + group3": {"deep": {"id": {"   number": 45}},"   fee": 100500}}'''