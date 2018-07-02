# naughty fakers

[Data fakers](https://github.com/joke2k/faker) that pull from [the big list of
naughty strings](https://github.com/minimaxir/big-list-of-naughty-strings).

Designed for edge-case testing. Do not expect data that will look sensible or
presentable.

# Installation and usage

```
pip install naughties
```

And then,

```python
from faker import Faker
from naughties.provider import NaughtyProvider

fake = Faker()
fake.add_provider(NaughtyProvider)

print fake.naughty_string()
```

# License

MIT
