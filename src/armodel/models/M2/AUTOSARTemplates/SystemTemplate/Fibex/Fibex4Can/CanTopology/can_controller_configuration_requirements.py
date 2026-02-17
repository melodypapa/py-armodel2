"""CanControllerConfigurationRequirements AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import (
    AbstractCanCommunicationControllerAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class CanControllerConfigurationRequirements(AbstractCanCommunicationControllerAttributes):
    """AUTOSAR CanControllerConfigurationRequirements."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_number_of_time_quanta_per": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IntegerBit),
        ),  # maxNumberOfTimeQuantaPer
        "max_sample": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSample
        "max_sync_jump": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSyncJump
        "min_number_of_time_quanta_per": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IntegerBit),
        ),  # minNumberOfTimeQuantaPer
        "min_sample_point": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minSamplePoint
        "min_sync_jump": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minSyncJump
    }

    def __init__(self) -> None:
        """Initialize CanControllerConfigurationRequirements."""
        super().__init__()
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None


class CanControllerConfigurationRequirementsBuilder:
    """Builder for CanControllerConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerConfigurationRequirements = CanControllerConfigurationRequirements()

    def build(self) -> CanControllerConfigurationRequirements:
        """Build and return CanControllerConfigurationRequirements object.

        Returns:
            CanControllerConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
