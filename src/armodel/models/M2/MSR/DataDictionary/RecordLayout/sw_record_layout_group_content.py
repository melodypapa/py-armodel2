"""SwRecordLayoutGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_v import (
    SwRecordLayoutV,
)


class SwRecordLayoutGroupContent(ARObject):
    """AUTOSAR SwRecordLayoutGroupContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_record_ref: Optional[ARRef]
    sw_record_layout_v: Optional[SwRecordLayoutV]
    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroupContent."""
        super().__init__()
        self.sw_record_ref: Optional[ARRef] = None
        self.sw_record_layout_v: Optional[SwRecordLayoutV] = None

    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutGroupContent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sw_record_ref
        if self.sw_record_ref is not None:
            serialized = ARObject._serialize_item(self.sw_record_ref, "SwRecordLayoutGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v
        if self.sw_record_layout_v is not None:
            serialized = ARObject._serialize_item(self.sw_record_layout_v, "SwRecordLayoutV")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroupContent":
        """Deserialize XML element to SwRecordLayoutGroupContent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutGroupContent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_record_ref
        child = ARObject._find_child_element(element, "SW-RECORD-REF")
        if child is not None:
            sw_record_ref_value = ARRef.deserialize(child)
            obj.sw_record_ref = sw_record_ref_value

        # Parse sw_record_layout_v
        child = ARObject._find_child_element(element, "SW-RECORD-LAYOUT-V")
        if child is not None:
            sw_record_layout_v_value = ARObject._deserialize_by_tag(child, "SwRecordLayoutV")
            obj.sw_record_layout_v = sw_record_layout_v_value

        return obj



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
