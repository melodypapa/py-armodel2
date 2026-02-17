"""Annotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 334)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_MSR_Documentation_Annotation.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)


class Annotation(GeneralAnnotation):
    """AUTOSAR Annotation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize Annotation."""
        super().__init__()


class AnnotationBuilder:
    """Builder for Annotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Annotation = Annotation()

    def build(self) -> Annotation:
        """Build and return Annotation object.

        Returns:
            Annotation instance
        """
        # TODO: Add validation
        return self._obj
