"""Traceable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 312)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)


class Traceable(MultilanguageReferrable):
    """AUTOSAR Traceable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "traces": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Traceable,
        ),  # traces
    }

    def __init__(self) -> None:
        """Initialize Traceable."""
        super().__init__()
        self.traces: list[Traceable] = []


class TraceableBuilder:
    """Builder for Traceable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Traceable = Traceable()

    def build(self) -> Traceable:
        """Build and return Traceable object.

        Returns:
            Traceable instance
        """
        # TODO: Add validation
        return self._obj
