"""SenderRecArrayElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 237)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
    IndexedArrayElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SenderRecArrayElementMapping(ARObject):
    """AUTOSAR SenderRecArrayElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    complex_type: Optional[SenderRecCompositeTypeMapping]
    indexed_array: Optional[IndexedArrayElement]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SenderRecArrayElementMapping."""
        super().__init__()
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.indexed_array: Optional[IndexedArrayElement] = None
        self.system_signal: Optional[SystemSignal] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayElementMapping":
        """Deserialize XML element to SenderRecArrayElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecArrayElementMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse complex_type
        child = ARObject._find_child_element(element, "COMPLEX-TYPE")
        if child is not None:
            complex_type_value = ARObject._deserialize_by_tag(child, "SenderRecCompositeTypeMapping")
            obj.complex_type = complex_type_value

        # Parse indexed_array
        child = ARObject._find_child_element(element, "INDEXED-ARRAY")
        if child is not None:
            indexed_array_value = ARObject._deserialize_by_tag(child, "IndexedArrayElement")
            obj.indexed_array = indexed_array_value

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        return obj



class SenderRecArrayElementMappingBuilder:
    """Builder for SenderRecArrayElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayElementMapping = SenderRecArrayElementMapping()

    def build(self) -> SenderRecArrayElementMapping:
        """Build and return SenderRecArrayElementMapping object.

        Returns:
            SenderRecArrayElementMapping instance
        """
        # TODO: Add validation
        return self._obj
