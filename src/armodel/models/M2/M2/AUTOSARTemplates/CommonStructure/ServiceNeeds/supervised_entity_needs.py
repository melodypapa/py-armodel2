"""SupervisedEntityNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 234)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 707)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class SupervisedEntityNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "activate_at_start": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # activateAtStart
        "checkpointses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # checkpointses
        "enable": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enable
        "expected_alive": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # expectedAlive
        "max_alive_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxAliveCycle
        "min_alive_cycle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minAliveCycle
        "tolerated_failed": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # toleratedFailed
    }

    def __init__(self) -> None:
        """Initialize SupervisedEntityNeeds."""
        super().__init__()
        self.activate_at_start: Optional[Boolean] = None
        self.checkpointses: list[Any] = []
        self.enable: Optional[Boolean] = None
        self.expected_alive: Optional[TimeValue] = None
        self.max_alive_cycle: Optional[TimeValue] = None
        self.min_alive_cycle: Optional[TimeValue] = None
        self.tolerated_failed: Optional[PositiveInteger] = None


class SupervisedEntityNeedsBuilder:
    """Builder for SupervisedEntityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SupervisedEntityNeeds = SupervisedEntityNeeds()

    def build(self) -> SupervisedEntityNeeds:
        """Build and return SupervisedEntityNeeds object.

        Returns:
            SupervisedEntityNeeds instance
        """
        # TODO: Add validation
        return self._obj
