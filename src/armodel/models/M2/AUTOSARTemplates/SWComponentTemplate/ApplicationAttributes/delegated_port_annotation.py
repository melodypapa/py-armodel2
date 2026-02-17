"""DelegatedPortAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)


class DelegatedPortAnnotation(GeneralAnnotation):
    """AUTOSAR DelegatedPortAnnotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "signal_fan": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SignalFanEnum,
        ),  # signalFan
    }

    def __init__(self) -> None:
        """Initialize DelegatedPortAnnotation."""
        super().__init__()
        self.signal_fan: Optional[SignalFanEnum] = None


class DelegatedPortAnnotationBuilder:
    """Builder for DelegatedPortAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegatedPortAnnotation = DelegatedPortAnnotation()

    def build(self) -> DelegatedPortAnnotation:
        """Build and return DelegatedPortAnnotation object.

        Returns:
            DelegatedPortAnnotation instance
        """
        # TODO: Add validation
        return self._obj
