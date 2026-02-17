"""ValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 333)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 433)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2076)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)


class ValueSpecification(ARObject):
    """AUTOSAR ValueSpecification."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortLabel
    }

    def __init__(self) -> None:
        """Initialize ValueSpecification."""
        super().__init__()
        self.short_label: Optional[Identifier] = None


class ValueSpecificationBuilder:
    """Builder for ValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueSpecification = ValueSpecification()

    def build(self) -> ValueSpecification:
        """Build and return ValueSpecification object.

        Returns:
            ValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
