"""FlexrayArTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 600)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    FrArTpAckType,
    MaximumMessageLengthType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_connection import (
    FlexrayArTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayArTpChannel(ARObject):
    """AUTOSAR FlexrayArTpChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ack_type: Optional[FrArTpAckType]
    cancellation: Optional[Boolean]
    extended: Optional[Boolean]
    max_ar: Optional[Integer]
    max_as: Optional[Integer]
    max_bs: Optional[Integer]
    max_fc_wait: Optional[PositiveInteger]
    maximum_message: Optional[MaximumMessageLengthType]
    max_retries: Optional[Integer]
    minimum: Optional[TimeValue]
    multicast: Optional[Boolean]
    n_pdus: list[NPdu]
    time_br: Optional[TimeValue]
    time_cs: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    tp_connections: list[FlexrayArTpConnection]
    def __init__(self) -> None:
        """Initialize FlexrayArTpChannel."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.cancellation: Optional[Boolean] = None
        self.extended: Optional[Boolean] = None
        self.max_ar: Optional[Integer] = None
        self.max_as: Optional[Integer] = None
        self.max_bs: Optional[Integer] = None
        self.max_fc_wait: Optional[PositiveInteger] = None
        self.maximum_message: Optional[MaximumMessageLengthType] = None
        self.max_retries: Optional[Integer] = None
        self.minimum: Optional[TimeValue] = None
        self.multicast: Optional[Boolean] = None
        self.n_pdus: list[NPdu] = []
        self.time_br: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.tp_connections: list[FlexrayArTpConnection] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpChannel":
        """Deserialize XML element to FlexrayArTpChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ack_type
        child = ARObject._find_child_element(element, "ACK-TYPE")
        if child is not None:
            ack_type_value = FrArTpAckType.deserialize(child)
            obj.ack_type = ack_type_value

        # Parse cancellation
        child = ARObject._find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse extended
        child = ARObject._find_child_element(element, "EXTENDED")
        if child is not None:
            extended_value = child.text
            obj.extended = extended_value

        # Parse max_ar
        child = ARObject._find_child_element(element, "MAX-AR")
        if child is not None:
            max_ar_value = child.text
            obj.max_ar = max_ar_value

        # Parse max_as
        child = ARObject._find_child_element(element, "MAX-AS")
        if child is not None:
            max_as_value = child.text
            obj.max_as = max_as_value

        # Parse max_bs
        child = ARObject._find_child_element(element, "MAX-BS")
        if child is not None:
            max_bs_value = child.text
            obj.max_bs = max_bs_value

        # Parse max_fc_wait
        child = ARObject._find_child_element(element, "MAX-FC-WAIT")
        if child is not None:
            max_fc_wait_value = child.text
            obj.max_fc_wait = max_fc_wait_value

        # Parse maximum_message
        child = ARObject._find_child_element(element, "MAXIMUM-MESSAGE")
        if child is not None:
            maximum_message_value = MaximumMessageLengthType.deserialize(child)
            obj.maximum_message = maximum_message_value

        # Parse max_retries
        child = ARObject._find_child_element(element, "MAX-RETRIES")
        if child is not None:
            max_retries_value = child.text
            obj.max_retries = max_retries_value

        # Parse minimum
        child = ARObject._find_child_element(element, "MINIMUM")
        if child is not None:
            minimum_value = child.text
            obj.minimum = minimum_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = child.text
            obj.multicast = multicast_value

        # Parse n_pdus (list from container "N-PDUS")
        obj.n_pdus = []
        container = ARObject._find_child_element(element, "N-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.n_pdus.append(child_value)

        # Parse time_br
        child = ARObject._find_child_element(element, "TIME-BR")
        if child is not None:
            time_br_value = child.text
            obj.time_br = time_br_value

        # Parse time_cs
        child = ARObject._find_child_element(element, "TIME-CS")
        if child is not None:
            time_cs_value = child.text
            obj.time_cs = time_cs_value

        # Parse timeout_ar
        child = ARObject._find_child_element(element, "TIMEOUT-AR")
        if child is not None:
            timeout_ar_value = child.text
            obj.timeout_ar = timeout_ar_value

        # Parse timeout_as
        child = ARObject._find_child_element(element, "TIMEOUT-AS")
        if child is not None:
            timeout_as_value = child.text
            obj.timeout_as = timeout_as_value

        # Parse timeout_bs
        child = ARObject._find_child_element(element, "TIMEOUT-BS")
        if child is not None:
            timeout_bs_value = child.text
            obj.timeout_bs = timeout_bs_value

        # Parse timeout_cr
        child = ARObject._find_child_element(element, "TIMEOUT-CR")
        if child is not None:
            timeout_cr_value = child.text
            obj.timeout_cr = timeout_cr_value

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = ARObject._find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        return obj



class FlexrayArTpChannelBuilder:
    """Builder for FlexrayArTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpChannel = FlexrayArTpChannel()

    def build(self) -> FlexrayArTpChannel:
        """Build and return FlexrayArTpChannel object.

        Returns:
            FlexrayArTpChannel instance
        """
        # TODO: Add validation
        return self._obj
