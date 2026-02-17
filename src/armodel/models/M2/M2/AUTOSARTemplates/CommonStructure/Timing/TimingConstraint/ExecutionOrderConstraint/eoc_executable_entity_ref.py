"""EOCExecutableEntityRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bsw_module": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswImplementation,
        ),  # bswModule
        "component": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # component
        "executable_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExecutableEntity,
        ),  # executableEntity
        "successors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # successors
    }

    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.successors: list[Any] = []


class EOCExecutableEntityRefBuilder:
    """Builder for EOCExecutableEntityRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRef = EOCExecutableEntityRef()

    def build(self) -> EOCExecutableEntityRef:
        """Build and return EOCExecutableEntityRef object.

        Returns:
            EOCExecutableEntityRef instance
        """
        # TODO: Add validation
        return self._obj
