"""SwRecordLayout AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)


class SwRecordLayout(ARElement):
    """AUTOSAR SwRecordLayout."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_record", None, False, False, SwRecordLayoutGroup),  # swRecord
    ]

    def __init__(self) -> None:
        """Initialize SwRecordLayout."""
        super().__init__()
        self.sw_record: Optional[SwRecordLayoutGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwRecordLayout to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayout":
        """Create SwRecordLayout from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwRecordLayout instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwRecordLayout since parent returns ARObject
        return cast("SwRecordLayout", obj)


class SwRecordLayoutBuilder:
    """Builder for SwRecordLayout."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayout = SwRecordLayout()

    def build(self) -> SwRecordLayout:
        """Build and return SwRecordLayout object.

        Returns:
            SwRecordLayout instance
        """
        # TODO: Add validation
        return self._obj
