"""DdsReliability AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsReliability(ARObject):
    """AUTOSAR DdsReliability."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "reliability_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsReliabilityKindEnum,
        ),  # reliabilityKind
        "reliability_max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # reliabilityMax
    }

    def __init__(self) -> None:
        """Initialize DdsReliability."""
        super().__init__()
        self.reliability_kind: Optional[DdsReliabilityKindEnum] = None
        self.reliability_max: Optional[Float] = None


class DdsReliabilityBuilder:
    """Builder for DdsReliability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsReliability = DdsReliability()

    def build(self) -> DdsReliability:
        """Build and return DdsReliability object.

        Returns:
            DdsReliability instance
        """
        # TODO: Add validation
        return self._obj
