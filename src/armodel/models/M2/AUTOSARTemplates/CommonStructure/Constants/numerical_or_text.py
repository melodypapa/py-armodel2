"""NumericalOrText AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    String,
)


class NumericalOrText(ARObject):
    """AUTOSAR NumericalOrText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("vf", None, True, False, None),  # vf
        ("vt", None, True, False, None),  # vt
    ]

    def __init__(self) -> None:
        """Initialize NumericalOrText."""
        super().__init__()
        self.vf: Optional[Numerical] = None
        self.vt: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NumericalOrText to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalOrText":
        """Create NumericalOrText from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NumericalOrText instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NumericalOrText since parent returns ARObject
        return cast("NumericalOrText", obj)


class NumericalOrTextBuilder:
    """Builder for NumericalOrText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalOrText = NumericalOrText()

    def build(self) -> NumericalOrText:
        """Build and return NumericalOrText object.

        Returns:
            NumericalOrText instance
        """
        # TODO: Add validation
        return self._obj
