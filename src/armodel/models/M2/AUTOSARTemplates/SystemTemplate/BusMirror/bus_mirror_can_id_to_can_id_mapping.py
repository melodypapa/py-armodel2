"""BusMirrorCanIdToCanIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 702)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_triggering import (
    CanFrameTriggering,
)


class BusMirrorCanIdToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorCanIdToCanIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    remapped_can_id: Optional[PositiveInteger]
    souce_can_id_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BusMirrorCanIdToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.souce_can_id_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdToCanIdMapping":
        """Deserialize XML element to BusMirrorCanIdToCanIdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorCanIdToCanIdMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse remapped_can_id
        child = ARObject._find_child_element(element, "REMAPPED-CAN-ID")
        if child is not None:
            remapped_can_id_value = child.text
            obj.remapped_can_id = remapped_can_id_value

        # Parse souce_can_id_ref
        child = ARObject._find_child_element(element, "SOUCE-CAN-ID")
        if child is not None:
            souce_can_id_ref_value = ARObject._deserialize_by_tag(child, "CanFrameTriggering")
            obj.souce_can_id_ref = souce_can_id_ref_value

        return obj



class BusMirrorCanIdToCanIdMappingBuilder:
    """Builder for BusMirrorCanIdToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdToCanIdMapping = BusMirrorCanIdToCanIdMapping()

    def build(self) -> BusMirrorCanIdToCanIdMapping:
        """Build and return BusMirrorCanIdToCanIdMapping object.

        Returns:
            BusMirrorCanIdToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
