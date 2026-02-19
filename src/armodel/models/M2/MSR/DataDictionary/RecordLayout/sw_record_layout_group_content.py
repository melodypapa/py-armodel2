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
        child = ARObject._find_child_element(element, "SW-RECORD")
        if child is not None:
            sw_record_ref_value = ARObject._deserialize_by_tag(child, "SwRecordLayoutGroup")
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
