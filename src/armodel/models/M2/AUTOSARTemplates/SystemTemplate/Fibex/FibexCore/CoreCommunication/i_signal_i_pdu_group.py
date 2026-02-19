"""ISignalIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 316)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 350)

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)


class ISignalIPduGroup(FibexElement):
    """AUTOSAR ISignalIPduGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication: Optional[String]
    contained_refs: list[ARRef]
    i_signal_i_pdus: list[ISignalIPdu]
    nm_pdus: list[NmPdu]
    def __init__(self) -> None:
        """Initialize ISignalIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.contained_refs: list[ARRef] = []
        self.i_signal_i_pdus: list[ISignalIPdu] = []
        self.nm_pdus: list[NmPdu] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalIPduGroup":
        """Deserialize XML element to ISignalIPduGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalIPduGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalIPduGroup, cls).deserialize(element)

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = child.text
            obj.communication = communication_value

        # Parse contained_refs (list from container "CONTAINEDS")
        obj.contained_refs = []
        container = ARObject._find_child_element(element, "CONTAINEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.contained_refs.append(child_value)

        # Parse i_signal_i_pdus (list from container "I-SIGNAL-I-PDUS")
        obj.i_signal_i_pdus = []
        container = ARObject._find_child_element(element, "I-SIGNAL-I-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_i_pdus.append(child_value)

        # Parse nm_pdus (list from container "NM-PDUS")
        obj.nm_pdus = []
        container = ARObject._find_child_element(element, "NM-PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_pdus.append(child_value)

        return obj



class ISignalIPduGroupBuilder:
    """Builder for ISignalIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPduGroup = ISignalIPduGroup()

    def build(self) -> ISignalIPduGroup:
        """Build and return ISignalIPduGroup object.

        Returns:
            ISignalIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
