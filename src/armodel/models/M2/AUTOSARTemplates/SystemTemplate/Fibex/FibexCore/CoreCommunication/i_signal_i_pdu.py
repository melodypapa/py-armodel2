"""ISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 994)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_timing import (
    IPduTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class ISignalIPdu(IPdu):
    """AUTOSAR ISignalIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_timing: Optional[IPduTiming]
    i_signal_to_pdu_refs: list[ARRef]
    unused_bit: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ISignalIPdu."""
        super().__init__()
        self.i_pdu_timing: Optional[IPduTiming] = None
        self.i_signal_to_pdu_refs: list[ARRef] = []
        self.unused_bit: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalIPdu":
        """Deserialize XML element to ISignalIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse i_pdu_timing
        child = ARObject._find_child_element(element, "I-PDU-TIMING")
        if child is not None:
            i_pdu_timing_value = ARObject._deserialize_by_tag(child, "IPduTiming")
            obj.i_pdu_timing = i_pdu_timing_value

        # Parse i_signal_to_pdu_refs (list)
        obj.i_signal_to_pdu_refs = []
        for child in ARObject._find_all_child_elements(element, "I-SIGNAL-TO-PDUS"):
            i_signal_to_pdu_refs_value = ARObject._deserialize_by_tag(child, "ISignalToIPduMapping")
            obj.i_signal_to_pdu_refs.append(i_signal_to_pdu_refs_value)

        # Parse unused_bit
        child = ARObject._find_child_element(element, "UNUSED-BIT")
        if child is not None:
            unused_bit_value = child.text
            obj.unused_bit = unused_bit_value

        return obj



class ISignalIPduBuilder:
    """Builder for ISignalIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPdu = ISignalIPdu()

    def build(self) -> ISignalIPdu:
        """Build and return ISignalIPdu object.

        Returns:
            ISignalIPdu instance
        """
        # TODO: Add validation
        return self._obj
