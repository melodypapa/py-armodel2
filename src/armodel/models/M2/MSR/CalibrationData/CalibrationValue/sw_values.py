"""SwValues AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.value_group import (
    ValueGroup,
)


class SwValues(ARObject):
    """AUTOSAR SwValues."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("v", None, True, False, None),  # v
        ("vf", None, True, False, None),  # vf
        ("vg", None, False, False, ValueGroup),  # vg
        ("vt", None, True, False, None),  # vt
        ("vtf", None, False, False, NumericalOrText),  # vtf
    ]

    def __init__(self) -> None:
        """Initialize SwValues."""
        super().__init__()
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vg: Optional[ValueGroup] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwValues to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwValues":
        """Create SwValues from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwValues instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwValues since parent returns ARObject
        return cast("SwValues", obj)


class SwValuesBuilder:
    """Builder for SwValues."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwValues = SwValues()

    def build(self) -> SwValues:
        """Build and return SwValues object.

        Returns:
            SwValues instance
        """
        # TODO: Add validation
        return self._obj
