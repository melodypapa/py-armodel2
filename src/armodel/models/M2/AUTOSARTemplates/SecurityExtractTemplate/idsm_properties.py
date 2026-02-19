"""IdsmProperties AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmProperties(IdsCommonElement):
    """AUTOSAR IdsmProperties."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rate_limitations: list[IdsmRateLimitation]
    traffic_limitations: list[IdsmTrafficLimitation]
    def __init__(self) -> None:
        """Initialize IdsmProperties."""
        super().__init__()
        self.rate_limitations: list[IdsmRateLimitation] = []
        self.traffic_limitations: list[IdsmTrafficLimitation] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmProperties":
        """Deserialize XML element to IdsmProperties object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmProperties object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rate_limitations (list)
        obj.rate_limitations = []
        for child in ARObject._find_all_child_elements(element, "RATE-LIMITATIONS"):
            rate_limitations_value = ARObject._deserialize_by_tag(child, "IdsmRateLimitation")
            obj.rate_limitations.append(rate_limitations_value)

        # Parse traffic_limitations (list)
        obj.traffic_limitations = []
        for child in ARObject._find_all_child_elements(element, "TRAFFIC-LIMITATIONS"):
            traffic_limitations_value = ARObject._deserialize_by_tag(child, "IdsmTrafficLimitation")
            obj.traffic_limitations.append(traffic_limitations_value)

        return obj



class IdsmPropertiesBuilder:
    """Builder for IdsmProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmProperties = IdsmProperties()

    def build(self) -> IdsmProperties:
        """Build and return IdsmProperties object.

        Returns:
            IdsmProperties instance
        """
        # TODO: Add validation
        return self._obj
