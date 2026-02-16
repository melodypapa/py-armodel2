"""EcucAddInfoParamValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class EcucAddInfoParamValue(EcucParameterValue):
    """AUTOSAR EcucAddInfoParamValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, False, False, DocumentationBlock),  # value
    ]

    def __init__(self) -> None:
        """Initialize EcucAddInfoParamValue."""
        super().__init__()
        self.value: Optional[DocumentationBlock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAddInfoParamValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAddInfoParamValue":
        """Create EcucAddInfoParamValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAddInfoParamValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAddInfoParamValue since parent returns ARObject
        return cast("EcucAddInfoParamValue", obj)


class EcucAddInfoParamValueBuilder:
    """Builder for EcucAddInfoParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAddInfoParamValue = EcucAddInfoParamValue()

    def build(self) -> EcucAddInfoParamValue:
        """Build and return EcucAddInfoParamValue object.

        Returns:
            EcucAddInfoParamValue instance
        """
        # TODO: Add validation
        return self._obj
