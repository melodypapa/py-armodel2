"""DiagnosticComControlSpecificChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 109)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)


class DiagnosticComControlSpecificChannel(ARObject):
    """AUTOSAR DiagnosticComControlSpecificChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "specific_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CommunicationCluster,
        ),  # specificChannel
        "specific_physical": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EthernetPhysical),
        ),  # specificPhysical
        "subnet_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # subnetNumber
    }

    def __init__(self) -> None:
        """Initialize DiagnosticComControlSpecificChannel."""
        super().__init__()
        self.specific_channel: Optional[CommunicationCluster] = None
        self.specific_physical: Optional[Any] = None
        self.subnet_number: Optional[PositiveInteger] = None


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
