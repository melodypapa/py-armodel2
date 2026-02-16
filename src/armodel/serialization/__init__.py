"""
Serialization framework for AUTOSAR models.

This module provides a declarative, registry-based framework for
serializing and deserializing AUTOSAR model objects to/from XML.

The framework eliminates boilerplate code by using metadata descriptors
and a strategy pattern for flexible serialization.

Example:
    ```python
    from armodel.serialization import XMLMember, get_global_registry

    # Define a class with XML metadata
    class MyAUTOSARClass(ARObject):
        _xml_members: dict[str, XMLMember] = {
            "short_name": XMLMember(
                xml_tag="SHORT-NAME",
                is_attribute=False,
                multiplicity="1",
            ),
            "description": XMLMember(
                xml_tag="DESC",
                is_attribute=False,
                multiplicity="0..1",
            ),
        }

        def __init__(self) -> None:
            self.short_name: str = ""
            self.description: str | None = None
    ```

The serialization is automatically handled by the ARObject base class:
    ```python
    obj = MyAUTOSARClass()
    obj.short_name = "MyClass"

    # Serialize
    element = obj.serialize("http://autosar.org/schema/r4.0")

    # Deserialize
    obj2 = MyAUTOSARClass.deserialize(element)
    ```
"""

# Import initialization to register default strategies
import armodel.serialization._init  # noqa: F401 (side-effect import)

from armodel.serialization.base import (
    DeserializationContext,
    SerializationContext,
    SerializationStrategy,
    StrategyRegistry,
)
from armodel.serialization.metadata import (
    XMLMember,
    create_xml_member_from_tuple,
    get_xml_metadata,
)
from armodel.serialization.registry import (
    SerializationRegistry,
    get_global_registry,
    reset_global_registry,
)

__all__ = [
    # Base classes
    "SerializationContext",
    "DeserializationContext",
    "SerializationStrategy",
    "StrategyRegistry",
    # Metadata
    "XMLMember",
    "get_xml_metadata",
    "create_xml_member_from_tuple",
    # Registry
    "SerializationRegistry",
    "get_global_registry",
    "reset_global_registry",
]
