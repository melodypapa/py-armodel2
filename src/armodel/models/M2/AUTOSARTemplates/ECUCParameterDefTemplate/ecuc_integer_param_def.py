"""EcucIntegerParamDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)


class EcucIntegerParamDef(EcucParameterDef):
    """AUTOSAR EcucIntegerParamDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_value", None, True, False, None),  # defaultValue
        ("max", None, True, False, None),  # max
        ("min", None, True, False, None),  # min
    ]

    def __init__(self) -> None:
        """Initialize EcucIntegerParamDef."""
        super().__init__()
        self.default_value: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucIntegerParamDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucIntegerParamDef":
        """Create EcucIntegerParamDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucIntegerParamDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucIntegerParamDef since parent returns ARObject
        return cast("EcucIntegerParamDef", obj)


class EcucIntegerParamDefBuilder:
    """Builder for EcucIntegerParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIntegerParamDef = EcucIntegerParamDef()

    def build(self) -> EcucIntegerParamDef:
        """Build and return EcucIntegerParamDef object.

        Returns:
            EcucIntegerParamDef instance
        """
        # TODO: Add validation
        return self._obj
