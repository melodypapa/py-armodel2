"""
Serialization framework for AUTOSAR models.

This module provides a reflection-based framework for serializing and
deserializing AUTOSAR model objects to/from XML.

The framework eliminates boilerplate code by using Python's built-in
reflection capabilities (vars() and get_type_hints()).

Example:
    ```python
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
    from armodel.serialization import NameConverter

    class MyAUTOSARClass(ARObject):
        def __init__(self) -> None:
            self.short_name: str = ""
            self.description: str | None = None

    # Use reflection-based serialization
    obj = MyAUTOSARClass()
    obj.short_name = "MyClass"

    # Serialize (automatically discovers attributes via vars())
    element = obj.serialize("http://autosar.org/schema/r4.0")

    # Deserialize (automatically determines types via get_type_hints())
    obj2 = MyAUTOSARClass.deserialize(element)
    ```

The serialization is automatically handled by the ARObject base class
using Python's standard reflection capabilities:
- vars() for automatic attribute discovery
- get_type_hints() for type-based deserialization
- NameConverter for snake_case ↔ UPPER-CASE-WITH-HYPHENS conversion

For edge cases, decorators are available:
- @xml_attribute: Mark a property to serialize as XML attribute
- @atp_variant(): Mark class using AUTOSAR atpVariation pattern
- @l_prefix(tag): Mark attribute using language-specific L-N pattern
"""

from armodel.serialization.decorators import xml_attribute
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.serialization_helper import SerializationHelper

__all__ = [
    "NameConverter",
    "xml_attribute",
    "SerializationHelper",
]
