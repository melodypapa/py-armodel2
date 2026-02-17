"""TriggerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_TriggerDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerMapping(ARObject):
    """AUTOSAR TriggerMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # firstTrigger
        "second_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # secondTrigger
    }

    def __init__(self) -> None:
        """Initialize TriggerMapping."""
        super().__init__()
        self.first_trigger: Optional[Trigger] = None
        self.second_trigger: Optional[Trigger] = None


class TriggerMappingBuilder:
    """Builder for TriggerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerMapping = TriggerMapping()

    def build(self) -> TriggerMapping:
        """Build and return TriggerMapping object.

        Returns:
            TriggerMapping instance
        """
        # TODO: Add validation
        return self._obj
