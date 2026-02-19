"""SwRecordLayout AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 421)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2066)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)


class SwRecordLayout(ARElement):
    """AUTOSAR SwRecordLayout."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_record_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwRecordLayout."""
        super().__init__()
        self.sw_record_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayout":
        """Deserialize XML element to SwRecordLayout object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayout object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_record_ref
        child = ARObject._find_child_element(element, "SW-RECORD")
        if child is not None:
            sw_record_ref_value = ARObject._deserialize_by_tag(child, "SwRecordLayoutGroup")
            obj.sw_record_ref = sw_record_ref_value

        return obj



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
