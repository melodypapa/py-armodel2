"""EcucValueConfigurationClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_configuration_class import (
    EcucAbstractConfigurationClass,
)


class EcucValueConfigurationClass(EcucAbstractConfigurationClass):
    """AUTOSAR EcucValueConfigurationClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize EcucValueConfigurationClass."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucValueConfigurationClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValueConfigurationClass":
        """Create EcucValueConfigurationClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucValueConfigurationClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucValueConfigurationClass since parent returns ARObject
        return cast("EcucValueConfigurationClass", obj)


class EcucValueConfigurationClassBuilder:
    """Builder for EcucValueConfigurationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValueConfigurationClass = EcucValueConfigurationClass()

    def build(self) -> EcucValueConfigurationClass:
        """Build and return EcucValueConfigurationClass object.

        Returns:
            EcucValueConfigurationClass instance
        """
        # TODO: Add validation
        return self._obj
