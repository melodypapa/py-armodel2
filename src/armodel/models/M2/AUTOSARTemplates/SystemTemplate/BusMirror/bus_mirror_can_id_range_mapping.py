"""BusMirrorCanIdRangeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BusMirrorCanIdRangeMapping(ARObject):
    """AUTOSAR BusMirrorCanIdRangeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination_base: Optional[PositiveInteger]
    source_can_id_code: Optional[PositiveInteger]
    source_can_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BusMirrorCanIdRangeMapping."""
        super().__init__()
        self.destination_base: Optional[PositiveInteger] = None
        self.source_can_id_code: Optional[PositiveInteger] = None
        self.source_can_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdRangeMapping":
        """Deserialize XML element to BusMirrorCanIdRangeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdRangeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination_base
        child = ARObject._find_child_element(element, "DESTINATION-BASE")
        if child is not None:
            destination_base_value = child.text
            obj.destination_base = destination_base_value

        # Parse source_can_id_code
        child = ARObject._find_child_element(element, "SOURCE-CAN-ID-CODE")
        if child is not None:
            source_can_id_code_value = child.text
            obj.source_can_id_code = source_can_id_code_value

        # Parse source_can_id
        child = ARObject._find_child_element(element, "SOURCE-CAN-ID")
        if child is not None:
            source_can_id_value = child.text
            obj.source_can_id = source_can_id_value

        return obj



class BusMirrorCanIdRangeMappingBuilder:
    """Builder for BusMirrorCanIdRangeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdRangeMapping = BusMirrorCanIdRangeMapping()

    def build(self) -> BusMirrorCanIdRangeMapping:
        """Build and return BusMirrorCanIdRangeMapping object.

        Returns:
            BusMirrorCanIdRangeMapping instance
        """
        # TODO: Add validation
        return self._obj
