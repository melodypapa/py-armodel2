"""DiagnosticComControlSpecificChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class DiagnosticComControlSpecificChannel(ARObject):
    """AUTOSAR DiagnosticComControlSpecificChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    specific_channel: Optional[CommunicationCluster]
    specific_physical: Optional[Any]
    subnet_number: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticComControlSpecificChannel."""
        super().__init__()
        self.specific_channel: Optional[CommunicationCluster] = None
        self.specific_physical: Optional[Any] = None
        self.subnet_number: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControlSpecificChannel":
        """Deserialize XML element to DiagnosticComControlSpecificChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControlSpecificChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse specific_channel
        child = ARObject._find_child_element(element, "SPECIFIC-CHANNEL")
        if child is not None:
            specific_channel_value = ARObject._deserialize_by_tag(child, "CommunicationCluster")
            obj.specific_channel = specific_channel_value

        # Parse specific_physical
        child = ARObject._find_child_element(element, "SPECIFIC-PHYSICAL")
        if child is not None:
            specific_physical_value = child.text
            obj.specific_physical = specific_physical_value

        # Parse subnet_number
        child = ARObject._find_child_element(element, "SUBNET-NUMBER")
        if child is not None:
            subnet_number_value = child.text
            obj.subnet_number = subnet_number_value

        return obj



class DiagnosticComControlSpecificChannelBuilder:
    """Builder for DiagnosticComControlSpecificChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControlSpecificChannel = DiagnosticComControlSpecificChannel()

    def build(self) -> DiagnosticComControlSpecificChannel:
        """Build and return DiagnosticComControlSpecificChannel object.

        Returns:
            DiagnosticComControlSpecificChannel instance
        """
        # TODO: Add validation
        return self._obj
