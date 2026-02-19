"""BusMirrorChannelMappingFlexray AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 704)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_BusMirror.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingFlexray(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingFlexray."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transmission: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingFlexray."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingFlexray":
        """Deserialize XML element to BusMirrorChannelMappingFlexray object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusMirrorChannelMappingFlexray object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BusMirrorChannelMappingFlexray, cls).deserialize(element)

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class BusMirrorChannelMappingFlexrayBuilder:
    """Builder for BusMirrorChannelMappingFlexray."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingFlexray = BusMirrorChannelMappingFlexray()

    def build(self) -> BusMirrorChannelMappingFlexray:
        """Build and return BusMirrorChannelMappingFlexray object.

        Returns:
            BusMirrorChannelMappingFlexray instance
        """
        # TODO: Add validation
        return self._obj
