"""EcucTextualParamValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class EcucTextualParamValue(EcucParameterValue):
    """AUTOSAR EcucTextualParamValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize EcucTextualParamValue."""
        super().__init__()
        self.value: Optional[VerbatimString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucTextualParamValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucTextualParamValue":
        """Create EcucTextualParamValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucTextualParamValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucTextualParamValue since parent returns ARObject
        return cast("EcucTextualParamValue", obj)


class EcucTextualParamValueBuilder:
    """Builder for EcucTextualParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucTextualParamValue = EcucTextualParamValue()

    def build(self) -> EcucTextualParamValue:
        """Build and return EcucTextualParamValue object.

        Returns:
            EcucTextualParamValue instance
        """
        # TODO: Add validation
        return self._obj
