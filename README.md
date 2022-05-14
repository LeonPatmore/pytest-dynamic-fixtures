# pytest dynamic fixtures

A decorator for generating dynamic fixtures.

## Usage

The decorator takes the following arguments:

- `args_list`: A list of arguments, in the tuple format.
- `name_generator`: A callable which generates the name of the fixture given a tuple of args.
- `fixture_params`: A dict of params to pass directly to the pytest fixture decorator.
- `fixtures`: A list of fixtures this fixture should depend on. You should put the fixture name in the arguments
of the function, at the end.

### Examples

Generates two session fixtures named `jack` and `bill`. The value of each fixture is the surname of the person.

```python
@dynamic_fixture(args_list=[("jack", "castleton"), ("bill", "allen")],
                 name_generator=lambda x, _: x,
                 fixture_params={"scope": "session"})
def generate_surname_fixture(_: str, surname: str) -> str:
    return surname
```

The following generates two fixtures named `jack_surname_length` and `bill_surname_length`. The fixtures depend on the
`request` fixture, which is used in the function by declaring `request` as an argument.

```python
@dynamic_fixture(args_list=[("jack",), ("bill",)],
                 name_generator=lambda x: f"{x}_surname_length",
                 fixtures=["request"])
def generate_surname_length(name: str, request):
    surname = request.getfixturevalue(name)
    return len(surname)
```
