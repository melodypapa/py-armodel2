"""CanTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanTpChannel(Identifiable):
    """AUTOSAR CanTpChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    channel_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanTpChannel."""
        super().__init__()
        self.channel_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpChannel":
        """Deserialize XML element to CanTpChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse channel_id
        child = ARObject._find_child_element(element, "CHANNEL-ID")
        if child is not None:
            channel_id_value = child.text
            obj.channel_id = channel_id_value

        return obj



class CanTpChannelBuilder:
    """Builder for CanTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpChannel = CanTpChannel()

    def build(self) -> CanTpChannel:
        """Build and return CanTpChannel object.

        Returns:
            CanTpChannel instance
        """
        # TODO: Add validation
        return self._obj
