"""GlobalTimeDomain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 858)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 225)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_gateway import (
    GlobalTimeGateway,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.network_segment_identification import (
    NetworkSegmentIdentification,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GlobalTimeDomain(FibexElement):
    """AUTOSAR GlobalTimeDomain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    debounce_time: Optional[TimeValue]
    domain_id: Optional[PositiveInteger]
    gateways: list[GlobalTimeGateway]
    global_time: Optional[AbstractGlobalTimeDomainProps]
    global_time_master: Optional[GlobalTimeMaster]
    global_time_subs: list[GlobalTimeDomain]
    network: Optional[NetworkSegmentIdentification]
    offset_time: Optional[GlobalTimeDomain]
    pdu_triggering_ref: Optional[ARRef]
    slaves: list[GlobalTimeSlave]
    sync_loss: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeDomain."""
        super().__init__()
        self.debounce_time: Optional[TimeValue] = None
        self.domain_id: Optional[PositiveInteger] = None
        self.gateways: list[GlobalTimeGateway] = []
        self.global_time: Optional[AbstractGlobalTimeDomainProps] = None
        self.global_time_master: Optional[GlobalTimeMaster] = None
        self.global_time_subs: list[GlobalTimeDomain] = []
        self.network: Optional[NetworkSegmentIdentification] = None
        self.offset_time: Optional[GlobalTimeDomain] = None
        self.pdu_triggering_ref: Optional[ARRef] = None
        self.slaves: list[GlobalTimeSlave] = []
        self.sync_loss: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeDomain":
        """Deserialize XML element to GlobalTimeDomain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeDomain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeDomain, cls).deserialize(element)

        # Parse debounce_time
        child = ARObject._find_child_element(element, "DEBOUNCE-TIME")
        if child is not None:
            debounce_time_value = child.text
            obj.debounce_time = debounce_time_value

        # Parse domain_id
        child = ARObject._find_child_element(element, "DOMAIN-ID")
        if child is not None:
            domain_id_value = child.text
            obj.domain_id = domain_id_value

        # Parse gateways (list from container "GATEWAYS")
        obj.gateways = []
        container = ARObject._find_child_element(element, "GATEWAYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.gateways.append(child_value)

        # Parse global_time
        child = ARObject._find_child_element(element, "GLOBAL-TIME")
        if child is not None:
            global_time_value = ARObject._deserialize_by_tag(child, "AbstractGlobalTimeDomainProps")
            obj.global_time = global_time_value

        # Parse global_time_master
        child = ARObject._find_child_element(element, "GLOBAL-TIME-MASTER")
        if child is not None:
            global_time_master_value = ARObject._deserialize_by_tag(child, "GlobalTimeMaster")
            obj.global_time_master = global_time_master_value

        # Parse global_time_subs (list from container "GLOBAL-TIME-SUBS")
        obj.global_time_subs = []
        container = ARObject._find_child_element(element, "GLOBAL-TIME-SUBS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_time_subs.append(child_value)

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = ARObject._deserialize_by_tag(child, "NetworkSegmentIdentification")
            obj.network = network_value

        # Parse offset_time
        child = ARObject._find_child_element(element, "OFFSET-TIME")
        if child is not None:
            offset_time_value = ARObject._deserialize_by_tag(child, "GlobalTimeDomain")
            obj.offset_time = offset_time_value

        # Parse pdu_triggering_ref
        child = ARObject._find_child_element(element, "PDU-TRIGGERING")
        if child is not None:
            pdu_triggering_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.pdu_triggering_ref = pdu_triggering_ref_value

        # Parse slaves (list from container "SLAVES")
        obj.slaves = []
        container = ARObject._find_child_element(element, "SLAVES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.slaves.append(child_value)

        # Parse sync_loss
        child = ARObject._find_child_element(element, "SYNC-LOSS")
        if child is not None:
            sync_loss_value = child.text
            obj.sync_loss = sync_loss_value

        return obj



class GlobalTimeDomainBuilder:
    """Builder for GlobalTimeDomain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeDomain = GlobalTimeDomain()

    def build(self) -> GlobalTimeDomain:
        """Build and return GlobalTimeDomain object.

        Returns:
            GlobalTimeDomain instance
        """
        # TODO: Add validation
        return self._obj
