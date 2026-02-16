"""ReferenceTailoring AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.unresolved_reference_restriction_with_severity import (
    UnresolvedReferenceRestrictionWithSeverity,
)


class ReferenceTailoring(AttributeTailoring):
    """AUTOSAR ReferenceTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type_tailorings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ClassTailoring,
        ),  # typeTailorings
        "unresolved_restriction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=UnresolvedReferenceRestrictionWithSeverity,
        ),  # unresolvedRestriction
    }

    def __init__(self) -> None:
        """Initialize ReferenceTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
        self.unresolved_restriction: Optional[UnresolvedReferenceRestrictionWithSeverity] = None


class ReferenceTailoringBuilder:
    """Builder for ReferenceTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceTailoring = ReferenceTailoring()

    def build(self) -> ReferenceTailoring:
        """Build and return ReferenceTailoring object.

        Returns:
            ReferenceTailoring instance
        """
        # TODO: Add validation
        return self._obj
