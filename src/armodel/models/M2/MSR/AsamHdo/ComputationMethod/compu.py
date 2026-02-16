"""Compu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_content import (
    CompuContent,
)


class Compu(ARObject):
    """AUTOSAR Compu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_content", None, False, False, CompuContent),  # compuContent
        ("compu_default", None, False, False, CompuConst),  # compuDefault
    ]

    def __init__(self) -> None:
        """Initialize Compu."""
        super().__init__()
        self.compu_content: Optional[CompuContent] = None
        self.compu_default: Optional[CompuConst] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Compu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Compu":
        """Create Compu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Compu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Compu since parent returns ARObject
        return cast("Compu", obj)


class CompuBuilder:
    """Builder for Compu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compu = Compu()

    def build(self) -> Compu:
        """Build and return Compu object.

        Returns:
            Compu instance
        """
        # TODO: Add validation
        return self._obj
