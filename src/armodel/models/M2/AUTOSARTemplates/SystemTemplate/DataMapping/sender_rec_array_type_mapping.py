"""SenderRecArrayTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecArrayTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_elements: list[Any]
    sender_to_signal_ref: Optional[ARRef]
    signal_to_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SenderRecArrayTypeMapping."""
        super().__init__()
        self.array_elements: list[Any] = []
        self.sender_to_signal_ref: Optional[ARRef] = None
        self.signal_to_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayTypeMapping":
        """Deserialize XML element to SenderRecArrayTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecArrayTypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecArrayTypeMapping, cls).deserialize(element)

        # Parse array_elements (list from container "ARRAY-ELEMENTS")
        obj.array_elements = []
        container = ARObject._find_child_element(element, "ARRAY-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.array_elements.append(child_value)

        # Parse sender_to_signal_ref
        child = ARObject._find_child_element(element, "SENDER-TO-SIGNAL")
        if child is not None:
            sender_to_signal_ref_value = ARObject._deserialize_by_tag(child, "TextTableMapping")
            obj.sender_to_signal_ref = sender_to_signal_ref_value

        # Parse signal_to_ref
        child = ARObject._find_child_element(element, "SIGNAL-TO")
        if child is not None:
            signal_to_ref_value = ARObject._deserialize_by_tag(child, "TextTableMapping")
            obj.signal_to_ref = signal_to_ref_value

        return obj



class SenderRecArrayTypeMappingBuilder:
    """Builder for SenderRecArrayTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayTypeMapping = SenderRecArrayTypeMapping()

    def build(self) -> SenderRecArrayTypeMapping:
        """Build and return SenderRecArrayTypeMapping object.

        Returns:
            SenderRecArrayTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
