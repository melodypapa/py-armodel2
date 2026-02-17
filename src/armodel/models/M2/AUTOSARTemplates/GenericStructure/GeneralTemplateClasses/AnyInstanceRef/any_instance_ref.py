"""AnyInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 970)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1995)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 328)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_AnyInstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class AnyInstanceRef(ARObject):
    """AUTOSAR AnyInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AtpClassifier,
        ),  # base
        "context_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AtpFeature,
        ),  # contextElements
        "target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AtpFeature,
        ),  # target
    }

    def __init__(self) -> None:
        """Initialize AnyInstanceRef."""
        super().__init__()
        self.base: AtpClassifier = None
        self.context_elements: list[AtpFeature] = []
        self.target: AtpFeature = None


class AnyInstanceRefBuilder:
    """Builder for AnyInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AnyInstanceRef = AnyInstanceRef()

    def build(self) -> AnyInstanceRef:
        """Build and return AnyInstanceRef object.

        Returns:
            AnyInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
