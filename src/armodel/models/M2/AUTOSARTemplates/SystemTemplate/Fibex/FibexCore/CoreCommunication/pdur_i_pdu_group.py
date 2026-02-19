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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PdurIPduGroup, cls).deserialize(element)

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = child.text
            obj.communication = communication_value

        # Parse i_pdu_refs (list from container "I-PDUS")
        obj.i_pdu_refs = []
        container = ARObject._find_child_element(element, "I-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_refs.append(child_value)

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
