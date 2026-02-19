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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse communication
        child = ARObject._find_child_element(element, "COMMUNICATION")
        if child is not None:
            communication_value = child.text
            obj.communication = communication_value

        # Parse contained_refs (list)
        obj.contained_refs = []
        for child in ARObject._find_all_child_elements(element, "CONTAINEDS"):
            contained_refs_value = ARObject._deserialize_by_tag(child, "ISignalIPduGroup")
            obj.contained_refs.append(contained_refs_value)

        # Parse i_signal_i_pdus (list)
        obj.i_signal_i_pdus = []
        for child in ARObject._find_all_child_elements(element, "I-SIGNAL-I-PDUS"):
            i_signal_i_pdus_value = ARObject._deserialize_by_tag(child, "ISignalIPdu")
            obj.i_signal_i_pdus.append(i_signal_i_pdus_value)

        # Parse nm_pdus (list)
        obj.nm_pdus = []
        for child in ARObject._find_all_child_elements(element, "NM-PDUS"):
            nm_pdus_value = ARObject._deserialize_by_tag(child, "NmPdu")
            obj.nm_pdus.append(nm_pdus_value)

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
