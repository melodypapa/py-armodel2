"""EcucNumericalParamValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class EcucNumericalParamValue(EcucParameterValue):
    """AUTOSAR EcucNumericalParamValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize EcucNumericalParamValue."""
        super().__init__()
        self.value: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucNumericalParamValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucNumericalParamValue":
        """Create EcucNumericalParamValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucNumericalParamValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucNumericalParamValue since parent returns ARObject
        return cast("EcucNumericalParamValue", obj)


class EcucNumericalParamValueBuilder:
    """Builder for EcucNumericalParamValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucNumericalParamValue = EcucNumericalParamValue()

    def build(self) -> EcucNumericalParamValue:
        """Build and return EcucNumericalParamValue object.

        Returns:
            EcucNumericalParamValue instance
        """
        # TODO: Add validation
        return self._obj
