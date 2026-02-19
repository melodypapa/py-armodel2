"""DiagnosticComControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommunicationControl.diagnostic_com_control import (
    DiagnosticComControl,
)


class DiagnosticComControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticComControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    all_channelses: list[CommunicationCluster]
    all_physicals: list[Any]
    specific_channels: list[DiagnosticComControl]
    sub_nodes: list[DiagnosticComControl]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlClass."""
        super().__init__()
        self.all_channelses: list[CommunicationCluster] = []
        self.all_physicals: list[Any] = []
        self.specific_channels: list[DiagnosticComControl] = []
        self.sub_nodes: list[DiagnosticComControl] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlClass":
        """Deserialize XML element to DiagnosticComControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlClass object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse all_channelses (list)
        obj.all_channelses = []
        for child in ARObject._find_all_child_elements(element, "ALL-CHANNELSES"):
            all_channelses_value = ARObject._deserialize_by_tag(child, "CommunicationCluster")
            obj.all_channelses.append(all_channelses_value)

        # Parse all_physicals (list)
        obj.all_physicals = []
        for child in ARObject._find_all_child_elements(element, "ALL-PHYSICALS"):
            all_physicals_value = child.text
            obj.all_physicals.append(all_physicals_value)

        # Parse specific_channels (list)
        obj.specific_channels = []
        for child in ARObject._find_all_child_elements(element, "SPECIFIC-CHANNELS"):
            specific_channels_value = ARObject._deserialize_by_tag(child, "DiagnosticComControl")
            obj.specific_channels.append(specific_channels_value)

        # Parse sub_nodes (list)
        obj.sub_nodes = []
        for child in ARObject._find_all_child_elements(element, "SUB-NODES"):
            sub_nodes_value = ARObject._deserialize_by_tag(child, "DiagnosticComControl")
            obj.sub_nodes.append(sub_nodes_value)

        return obj



class DiagnosticComControlClassBuilder:
    """Builder for DiagnosticComControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlClass = DiagnosticComControlClass()

    def build(self) -> DiagnosticComControlClass:
        """Build and return DiagnosticComControlClass object.

        Returns:
            DiagnosticComControlClass instance
        """
        # TODO: Add validation
        return self._obj
