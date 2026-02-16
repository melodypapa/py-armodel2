"""DltEcu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_application import (
    DltApplication,
)


class DltEcu(ARElement):
    """AUTOSAR DltEcu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("applications", None, False, True, DltApplication),  # applications
        ("ecu_id", None, True, False, None),  # ecuId
    ]

    def __init__(self) -> None:
        """Initialize DltEcu."""
        super().__init__()
        self.applications: list[DltApplication] = []
        self.ecu_id: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DltEcu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltEcu":
        """Create DltEcu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DltEcu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DltEcu since parent returns ARObject
        return cast("DltEcu", obj)


class DltEcuBuilder:
    """Builder for DltEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltEcu = DltEcu()

    def build(self) -> DltEcu:
        """Build and return DltEcu object.

        Returns:
            DltEcu instance
        """
        # TODO: Add validation
        return self._obj
