"""DdsCpServiceInstanceEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 475)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DdsCpServiceInstanceEvent(ARObject):
    """AUTOSAR DdsCpServiceInstanceEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_event_ref: Optional[ARRef]
    dds_event_qos: Optional[DdsCpQosProfile]
    dds_event_topic: Optional[DdsCpTopic]
    def __init__(self) -> None:
        """Initialize DdsCpServiceInstanceEvent."""
        super().__init__()
        self.dds_event_ref: Optional[ARRef] = None
        self.dds_event_qos: Optional[DdsCpQosProfile] = None
        self.dds_event_topic: Optional[DdsCpTopic] = None


class DdsCpServiceInstanceEventBuilder:
    """Builder for DdsCpServiceInstanceEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstanceEvent = DdsCpServiceInstanceEvent()

    def build(self) -> DdsCpServiceInstanceEvent:
        """Build and return DdsCpServiceInstanceEvent object.

        Returns:
            DdsCpServiceInstanceEvent instance
        """
        # TODO: Add validation
        return self._obj
