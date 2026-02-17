"""RestrictionWithSeverity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 86)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Common.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint import (
    SeverityEnum,
)


class RestrictionWithSeverity(ARObject):
    """AUTOSAR RestrictionWithSeverity."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "severity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=SeverityEnum,
        ),  # severity
    }

    def __init__(self) -> None:
        """Initialize RestrictionWithSeverity."""
        super().__init__()
        self.severity: SeverityEnum = None


class RestrictionWithSeverityBuilder:
    """Builder for RestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RestrictionWithSeverity = RestrictionWithSeverity()

    def build(self) -> RestrictionWithSeverity:
        """Build and return RestrictionWithSeverity object.

        Returns:
            RestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
