### Everett declarative wrapper

#### Usage:

Declare a `Config` subclass with `Param` class fields. Their name together with namespace will be full name of an option just like in regular everett

```python
from decleverett import Config, Param

class MyConfig(Config):
    namespace = 'my'
    COOL_PARAM: str = Param()
    OTHER_PARAM: str = Param(default='my value')

import os

os.environ['MY_COOL_PARAM'] = 'cool value'

print(MyConfig.COOL_PARAM) # cool value
print(MyConfig.OTHER_PARAM) # my value
```

`Param` attributes are the same as [here](https://everett.readthedocs.io/en/latest/configuration.html#extracting-values) except key is classfield name
