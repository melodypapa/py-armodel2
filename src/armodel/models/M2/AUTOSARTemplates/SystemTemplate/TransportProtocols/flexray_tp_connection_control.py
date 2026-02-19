"""FlexrayTpConnectionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 593)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    FrArTpAckType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)


class FlexrayTpConnectionControl(Identifiable):
    """AUTOSAR FlexrayTpConnectionControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ack_type: Optional[FrArTpAckType]
    max_fc_wait: Optional[Integer]
    max_number_of: Optional[Integer]
    max_retries: Optional[Integer]
    separation_cycle: Optional[Integer]
    time_br: Optional[TimeValue]
    time_buffer: Optional[TimeValue]
    time_cs: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize FlexrayTpConnectionControl."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.max_fc_wait: Optional[Integer] = None
        self.max_number_of: Optional[Integer] = None
        self.max_retries: Optional[Integer] = None
        self.separation_cycle: Optional[Integer] = None
        self.time_br: Optional[TimeValue] = None
        self.time_buffer: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnectionControl":
        """Deserialize XML element to FlexrayTpConnectionControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConnectionControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConnectionControl, cls).deserialize(element)

        # Parse ack_type
        child = ARObject._find_child_element(element, "ACK-TYPE")
        if child is not None:
            ack_type_value = FrArTpAckType.deserialize(child)
            obj.ack_type = ack_type_value

        # Parse max_fc_wait
        child = ARObject._find_child_element(element, "MAX-FC-WAIT")
        if child is not None:
            max_fc_wait_value = child.text
            obj.max_fc_wait = max_fc_wait_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse max_retries
        child = ARObject._find_child_element(element, "MAX-RETRIES")
        if child is not None:
            max_retries_value = child.text
            obj.max_retries = max_retries_value

        # Parse separation_cycle
        child = ARObject._find_child_element(element, "SEPARATION-CYCLE")
        if child is not None:
            separation_cycle_value = child.text
            obj.separation_cycle = separation_cycle_value

        # Parse time_br
        child = ARObject._find_child_element(element, "TIME-BR")
        if child is not None:
            time_br_value = child.text
            obj.time_br = time_br_value

        # Parse time_buffer
        child = ARObject._find_child_element(element, "TIME-BUFFER")
        if child is not None:
            time_buffer_value = child.text
            obj.time_buffer = time_buffer_value

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

        return obj



class FlexrayTpConnectionControlBuilder:
    """Builder for FlexrayTpConnectionControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConnectionControl = FlexrayTpConnectionControl()

    def build(self) -> FlexrayTpConnectionControl:
        """Build and return FlexrayTpConnectionControl object.

        Returns:
            FlexrayTpConnectionControl instance
        """
        # TODO: Add validation
        return self._obj
