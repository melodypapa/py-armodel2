"""NetworkSegmentIdentification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NetworkSegmentIdentification(ARObject):
    """AUTOSAR NetworkSegmentIdentification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NetworkSegmentIdentification."""
        super().__init__()
        self.network: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkSegmentIdentification":
        """Deserialize XML element to NetworkSegmentIdentification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NetworkSegmentIdentification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = child.text
            obj.network = network_value

        return obj



class NetworkSegmentIdentificationBuilder:
    """Builder for NetworkSegmentIdentification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NetworkSegmentIdentification = NetworkSegmentIdentification()

    def build(self) -> NetworkSegmentIdentification:
        """Build and return NetworkSegmentIdentification object.

        Returns:
            NetworkSegmentIdentification instance
        """
        # TODO: Add validation
        return self._obj
