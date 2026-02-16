"""SwRecordLayoutGroupContent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_v import (
    SwRecordLayoutV,
)


class SwRecordLayoutGroupContent(ARObject):
    """AUTOSAR SwRecordLayoutGroupContent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_record", None, False, False, SwRecordLayoutGroup),  # swRecord
        ("sw_record_layout_v", None, False, False, SwRecordLayoutV),  # swRecordLayoutV
    ]

    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroupContent."""
        super().__init__()
        self.sw_record: Optional[SwRecordLayoutGroup] = None
        self.sw_record_layout_v: Optional[SwRecordLayoutV] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwRecordLayoutGroupContent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroupContent":
        """Create SwRecordLayoutGroupContent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwRecordLayoutGroupContent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwRecordLayoutGroupContent since parent returns ARObject
        return cast("SwRecordLayoutGroupContent", obj)


class SwRecordLayoutGroupContentBuilder:
    """Builder for SwRecordLayoutGroupContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwRecordLayoutGroupContent = SwRecordLayoutGroupContent()

    def build(self) -> SwRecordLayoutGroupContent:
        """Build and return SwRecordLayoutGroupContent object.

        Returns:
            SwRecordLayoutGroupContent instance
        """
        # TODO: Add validation
        return self._obj
