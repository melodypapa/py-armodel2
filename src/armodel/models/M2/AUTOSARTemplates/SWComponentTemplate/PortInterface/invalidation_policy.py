"""InvalidationPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class InvalidationPolicy(ARObject):
    """AUTOSAR InvalidationPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_element", None, False, False, VariableDataPrototype),  # dataElement
        ("handle_invalid_enum", None, False, False, HandleInvalidEnum),  # handleInvalidEnum
    ]

    def __init__(self) -> None:
        """Initialize InvalidationPolicy."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InvalidationPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InvalidationPolicy":
        """Create InvalidationPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InvalidationPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InvalidationPolicy since parent returns ARObject
        return cast("InvalidationPolicy", obj)


class InvalidationPolicyBuilder:
    """Builder for InvalidationPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InvalidationPolicy = InvalidationPolicy()

    def build(self) -> InvalidationPolicy:
        """Build and return InvalidationPolicy object.

        Returns:
            InvalidationPolicy instance
        """
        # TODO: Add validation
        return self._obj
