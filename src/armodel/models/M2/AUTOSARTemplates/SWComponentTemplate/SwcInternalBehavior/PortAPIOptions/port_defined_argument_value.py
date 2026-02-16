"""PortDefinedArgumentValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class PortDefinedArgumentValue(ARObject):
    """AUTOSAR PortDefinedArgumentValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, False, False, ValueSpecification),  # value
        ("value_type", None, False, False, any (ImplementationData)),  # valueType
    ]

    def __init__(self) -> None:
        """Initialize PortDefinedArgumentValue."""
        super().__init__()
        self.value: Optional[ValueSpecification] = None
        self.value_type: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortDefinedArgumentValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortDefinedArgumentValue":
        """Create PortDefinedArgumentValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortDefinedArgumentValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortDefinedArgumentValue since parent returns ARObject
        return cast("PortDefinedArgumentValue", obj)


class PortDefinedArgumentValueBuilder:
    """Builder for PortDefinedArgumentValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortDefinedArgumentValue = PortDefinedArgumentValue()

    def build(self) -> PortDefinedArgumentValue:
        """Build and return PortDefinedArgumentValue object.

        Returns:
            PortDefinedArgumentValue instance
        """
        # TODO: Add validation
        return self._obj
