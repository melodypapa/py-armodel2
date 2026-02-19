"""IEEE1722TpAcfLin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 666)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfLin."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_frequency: Optional[PositiveInteger]
    frame_sync_enabled: Optional[Boolean]
    timestamp: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLin."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.frame_sync_enabled: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLin":
        """Deserialize XML element to IEEE1722TpAcfLin object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfLin object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfLin, cls).deserialize(element)

        # Parse base_frequency
        child = ARObject._find_child_element(element, "BASE-FREQUENCY")
        if child is not None:
            base_frequency_value = child.text
            obj.base_frequency = base_frequency_value

        # Parse frame_sync_enabled
        child = ARObject._find_child_element(element, "FRAME-SYNC-ENABLED")
        if child is not None:
            frame_sync_enabled_value = child.text
            obj.frame_sync_enabled = frame_sync_enabled_value

        # Parse timestamp
        child = ARObject._find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

        return obj



class IEEE1722TpAcfLinBuilder:
    """Builder for IEEE1722TpAcfLin."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfLin = IEEE1722TpAcfLin()

    def build(self) -> IEEE1722TpAcfLin:
        """Build and return IEEE1722TpAcfLin object.

        Returns:
            IEEE1722TpAcfLin instance
        """
        # TODO: Add validation
        return self._obj
