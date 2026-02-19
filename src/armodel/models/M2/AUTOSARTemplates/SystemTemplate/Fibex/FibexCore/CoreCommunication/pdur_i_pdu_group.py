"""PdurIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 352)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class PdurIPduGroup(FibexElement):
    """AUTOSAR PdurIPduGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication: Optional[String]
    i_pdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PdurIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.i_pdu_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PdurIPduGroup":
        """Deserialize XML element to PdurIPduGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PdurIPduGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = child.text
            obj.communication = communication_value

        # Parse i_pdu_refs (list)
        obj.i_pdu_refs = []
        for child in ARObject._find_all_child_elements(element, "I-PDUS"):
            i_pdu_refs_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.i_pdu_refs.append(i_pdu_refs_value)

        return obj



class PdurIPduGroupBuilder:
    """Builder for PdurIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PdurIPduGroup = PdurIPduGroup()

    def build(self) -> PdurIPduGroup:
        """Build and return PdurIPduGroup object.

        Returns:
            PdurIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
