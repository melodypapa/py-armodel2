"""ContainerIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 353)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainerIPduHeaderTypeEnum,
    ContainerIPduTriggerEnum,
    RxAcceptContainedIPduEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainerIPdu(IPdu):
    """AUTOSAR ContainerIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    contained_i_pdu_propses: list[ContainedIPduProps]
    contained_pdu_refs: list[ARRef]
    container: Optional[TimeValue]
    container_trigger_ref: Optional[ARRef]
    header_type: Optional[ContainerIPduHeaderTypeEnum]
    minimum_rx: Optional[PositiveInteger]
    minimum_tx: Optional[PositiveInteger]
    rx_accept: Optional[RxAcceptContainedIPduEnum]
    threshold_size: Optional[PositiveInteger]
    unused_bit: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ContainerIPdu."""
        super().__init__()
        self.contained_i_pdu_propses: list[ContainedIPduProps] = []
        self.contained_pdu_refs: list[ARRef] = []
        self.container: Optional[TimeValue] = None
        self.container_trigger_ref: Optional[ARRef] = None
        self.header_type: Optional[ContainerIPduHeaderTypeEnum] = None
        self.minimum_rx: Optional[PositiveInteger] = None
        self.minimum_tx: Optional[PositiveInteger] = None
        self.rx_accept: Optional[RxAcceptContainedIPduEnum] = None
        self.threshold_size: Optional[PositiveInteger] = None
        self.unused_bit: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainerIPdu":
        """Deserialize XML element to ContainerIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ContainerIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ContainerIPdu, cls).deserialize(element)

        # Parse contained_i_pdu_propses (list from container "CONTAINED-I-PDU-PROPSES")
        obj.contained_i_pdu_propses = []
        container = ARObject._find_child_element(element, "CONTAINED-I-PDU-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contained_i_pdu_propses.append(child_value)

        # Parse contained_pdu_refs (list from container "CONTAINED-PDUS")
        obj.contained_pdu_refs = []
        container = ARObject._find_child_element(element, "CONTAINED-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contained_pdu_refs.append(child_value)

        # Parse container
        child = ARObject._find_child_element(element, "CONTAINER")
        if child is not None:
            container_value = child.text
            obj.container = container_value

        # Parse container_trigger_ref
        child = ARObject._find_child_element(element, "CONTAINER-TRIGGER")
        if child is not None:
            container_trigger_ref_value = ContainerIPduTriggerEnum.deserialize(child)
            obj.container_trigger_ref = container_trigger_ref_value

        # Parse header_type
        child = ARObject._find_child_element(element, "HEADER-TYPE")
        if child is not None:
            header_type_value = ContainerIPduHeaderTypeEnum.deserialize(child)
            obj.header_type = header_type_value

        # Parse minimum_rx
        child = ARObject._find_child_element(element, "MINIMUM-RX")
        if child is not None:
            minimum_rx_value = child.text
            obj.minimum_rx = minimum_rx_value

        # Parse minimum_tx
        child = ARObject._find_child_element(element, "MINIMUM-TX")
        if child is not None:
            minimum_tx_value = child.text
            obj.minimum_tx = minimum_tx_value

        # Parse rx_accept
        child = ARObject._find_child_element(element, "RX-ACCEPT")
        if child is not None:
            rx_accept_value = RxAcceptContainedIPduEnum.deserialize(child)
            obj.rx_accept = rx_accept_value

        # Parse threshold_size
        child = ARObject._find_child_element(element, "THRESHOLD-SIZE")
        if child is not None:
            threshold_size_value = child.text
            obj.threshold_size = threshold_size_value

        # Parse unused_bit
        child = ARObject._find_child_element(element, "UNUSED-BIT")
        if child is not None:
            unused_bit_value = child.text
            obj.unused_bit = unused_bit_value

        return obj



class ContainerIPduBuilder:
    """Builder for ContainerIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainerIPdu = ContainerIPdu()

    def build(self) -> ContainerIPdu:
        """Build and return ContainerIPdu object.

        Returns:
            ContainerIPdu instance
        """
        # TODO: Add validation
        return self._obj
