"""Gateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 837)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.frame_mapping import (
    FrameMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_pdu_mapping import (
    IPduMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_signal_mapping import (
    ISignalMapping,
)


class Gateway(FibexElement):
    """AUTOSAR Gateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu: Optional[EcuInstance]
    frame_mapping_refs: list[ARRef]
    i_pdu_mapping_refs: list[ARRef]
    signal_mapping_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize Gateway."""
        super().__init__()
        self.ecu: Optional[EcuInstance] = None
        self.frame_mapping_refs: list[ARRef] = []
        self.i_pdu_mapping_refs: list[ARRef] = []
        self.signal_mapping_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Gateway":
        """Deserialize XML element to Gateway object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Gateway object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecu
        child = ARObject._find_child_element(element, "ECU")
        if child is not None:
            ecu_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu = ecu_value

        # Parse frame_mapping_refs (list)
        obj.frame_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "FRAME-MAPPINGS"):
            frame_mapping_refs_value = ARObject._deserialize_by_tag(child, "FrameMapping")
            obj.frame_mapping_refs.append(frame_mapping_refs_value)

        # Parse i_pdu_mapping_refs (list)
        obj.i_pdu_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "I-PDU-MAPPINGS"):
            i_pdu_mapping_refs_value = ARObject._deserialize_by_tag(child, "IPduMapping")
            obj.i_pdu_mapping_refs.append(i_pdu_mapping_refs_value)

        # Parse signal_mapping_refs (list)
        obj.signal_mapping_refs = []
        for child in ARObject._find_all_child_elements(element, "SIGNAL-MAPPINGS"):
            signal_mapping_refs_value = ARObject._deserialize_by_tag(child, "ISignalMapping")
            obj.signal_mapping_refs.append(signal_mapping_refs_value)

        return obj



class GatewayBuilder:
    """Builder for Gateway."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Gateway = Gateway()

    def build(self) -> Gateway:
        """Build and return Gateway object.

        Returns:
            Gateway instance
        """
        # TODO: Add validation
        return self._obj
