"""DltConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_ecu import (
    DltEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_log_channel import (
    DltLogChannel,
)


class DltConfig(ARObject):
    """AUTOSAR DltConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dlt_ecu: Optional[DltEcu]
    dlt_log_channels: list[DltLogChannel]
    session_id: Optional[Boolean]
    timestamp: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DltConfig."""
        super().__init__()
        self.dlt_ecu: Optional[DltEcu] = None
        self.dlt_log_channels: list[DltLogChannel] = []
        self.session_id: Optional[Boolean] = None
        self.timestamp: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltConfig":
        """Deserialize XML element to DltConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dlt_ecu
        child = ARObject._find_child_element(element, "DLT-ECU")
        if child is not None:
            dlt_ecu_value = ARObject._deserialize_by_tag(child, "DltEcu")
            obj.dlt_ecu = dlt_ecu_value

        # Parse dlt_log_channels (list)
        obj.dlt_log_channels = []
        for child in ARObject._find_all_child_elements(element, "DLT-LOG-CHANNELS"):
            dlt_log_channels_value = ARObject._deserialize_by_tag(child, "DltLogChannel")
            obj.dlt_log_channels.append(dlt_log_channels_value)

        # Parse session_id
        child = ARObject._find_child_element(element, "SESSION-ID")
        if child is not None:
            session_id_value = child.text
            obj.session_id = session_id_value

        # Parse timestamp
        child = ARObject._find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

        return obj



class DltConfigBuilder:
    """Builder for DltConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltConfig = DltConfig()

    def build(self) -> DltConfig:
        """Build and return DltConfig object.

        Returns:
            DltConfig instance
        """
        # TODO: Add validation
        return self._obj
