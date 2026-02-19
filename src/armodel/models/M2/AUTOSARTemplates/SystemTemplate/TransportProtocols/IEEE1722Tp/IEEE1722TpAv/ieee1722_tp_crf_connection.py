"""IEEE1722TpCrfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 640)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpCrfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_frequency: Optional[PositiveInteger]
    crf_pull_enum: Optional[IEEE1722TpCrfPullEnum]
    crf_type_enum: Optional[IEEE1722TpCrfTypeEnum]
    frame_sync: Optional[Boolean]
    timestamp: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpCrfConnection."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.crf_pull_enum: Optional[IEEE1722TpCrfPullEnum] = None
        self.crf_type_enum: Optional[IEEE1722TpCrfTypeEnum] = None
        self.frame_sync: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpCrfConnection":
        """Deserialize XML element to IEEE1722TpCrfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpCrfConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpCrfConnection, cls).deserialize(element)

        # Parse base_frequency
        child = ARObject._find_child_element(element, "BASE-FREQUENCY")
        if child is not None:
            base_frequency_value = child.text
            obj.base_frequency = base_frequency_value

        # Parse crf_pull_enum
        child = ARObject._find_child_element(element, "CRF-PULL-ENUM")
        if child is not None:
            crf_pull_enum_value = IEEE1722TpCrfPullEnum.deserialize(child)
            obj.crf_pull_enum = crf_pull_enum_value

        # Parse crf_type_enum
        child = ARObject._find_child_element(element, "CRF-TYPE-ENUM")
        if child is not None:
            crf_type_enum_value = IEEE1722TpCrfTypeEnum.deserialize(child)
            obj.crf_type_enum = crf_type_enum_value

        # Parse frame_sync
        child = ARObject._find_child_element(element, "FRAME-SYNC")
        if child is not None:
            frame_sync_value = child.text
            obj.frame_sync = frame_sync_value

        # Parse timestamp
        child = ARObject._find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

        return obj



class IEEE1722TpCrfConnectionBuilder:
    """Builder for IEEE1722TpCrfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpCrfConnection = IEEE1722TpCrfConnection()

    def build(self) -> IEEE1722TpCrfConnection:
        """Build and return IEEE1722TpCrfConnection object.

        Returns:
            IEEE1722TpCrfConnection instance
        """
        # TODO: Add validation
        return self._obj
