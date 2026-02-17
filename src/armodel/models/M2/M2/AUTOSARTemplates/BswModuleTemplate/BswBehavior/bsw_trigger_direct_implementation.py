"""BswTriggerDirectImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswTriggerDirectImplementation(ARObject):
    """AUTOSAR BswTriggerDirectImplementation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cat2_isr": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cat2Isr
        "mastered_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # masteredTrigger
        "task": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # task
    }

    def __init__(self) -> None:
        """Initialize BswTriggerDirectImplementation."""
        super().__init__()
        self.cat2_isr: Optional[Identifier] = None
        self.mastered_trigger: Optional[Trigger] = None
        self.task: Optional[Identifier] = None


class BswTriggerDirectImplementationBuilder:
    """Builder for BswTriggerDirectImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTriggerDirectImplementation = BswTriggerDirectImplementation()

    def build(self) -> BswTriggerDirectImplementation:
        """Build and return BswTriggerDirectImplementation object.

        Returns:
            BswTriggerDirectImplementation instance
        """
        # TODO: Add validation
        return self._obj
