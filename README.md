# ninja-bear-language-java
This [ninja-bear](https://pypi.org/project/ninja-bear) plugin adds support for the Java programming language.

```yaml
languages:
  # -------------------------------------------------------------------------
  # Property description for ninja-bear-language-java.
  #
  # language        (required): ninja-bear-language-java or java
  # package         (required): Specifies the config's package name.
  # file_naming     (optional): Specifies the file naming convention (snake |
  #                             screaming_snake | camel | pascal | kebap).
  #                             Defaults to the file-name without the extension.
  # property_naming (optional): Specifies the property naming convention (snake |
  #                             screaming_snake | camel | pascal | kebap).
  # type_naming     (optional): Specifies the naming convention for the generated
  #                             type (snake | screaming_snake | camel | pascal |
  #                             kebap). The default value is language specific.
  # indent          (optional): Specifies the amount of spaces before each
  #                             property. Defaults to 4.
  # transformers    (optional): Specifies a list of transformers (alias) to use.
  # distributors    (optional): Specifies a list of distributors (alias) to use.
  # ignore          (optional): If true, the section gets ignored.
  # -------------------------------------------------------------------------
  - language: ninja-bear-language-java
    package: com.example.testpackage
    property_naming: camel

properties:
  - type: bool
    name: myBoolean
    value: true

  - type: int
    name: myInteger
    value: 142

  - type: float
    name: myFloat
    value: 322f  # Float with float specifier. However, an additional specifier (f) is not required and will be trimmed.

  - type: float
    name: myCombinedFloat
    value: ${myInteger} * ${myFloat}  # Number and boolean combinations get evaluated during the dump process.

  - type: double
    name: myDouble
    value: 233.9

  - type: string
    name: myString
    value: Hello World
    hidden: true  # If a property should act as a helper but should not be written to the generated file, it must be marked as 'hidden'.

  - type: regex
    name: myRegex
    value: Test Reg(E|e)x
    comment: Just another RegEx.  # Variables can be described using the comment property.

  - type: string
    name: mySubstitutedString
    value: Sometimes I just want to scream ${myString}!  # To use the value of another property, simply use its name with ${}. E.g., ${myString}.
```
