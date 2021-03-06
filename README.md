rutherford
==========

Automatically add and remove pool members from neutron LBaaS pools based on nova server names

## Background

Rutherford is named after (Ernest Rutherford)[http://en.wikipedia.org/wiki/Ernest_Rutherford], who conceived of the possible existence of (the neutron)[http://en.wikipedia.org/wiki/Neutron] in 1920.

## Pre-requisites

Must have python 2.7 with future print()
Must have pyrax installed, configured via ~/.raxpub

## How to use

Add a mapping in rutherford.py:
mapping.append(Mapping('servername-prefix', 'loadbalancer-name', port))


```python rutherford.py```

## To Do
- Add more node settings to the mapping class
- Move mappings to a file

## License

```
Copyright 2014 Martin Smith <martin@mbs3.org>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

