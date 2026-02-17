"""SwComponentPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 77)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 896)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 245)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 21)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 79)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 466)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwComponentType,
        ),  # type
    }

    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type: Optional[SwComponentType] = None


class SwComponentPrototypeBuilder:
    """Builder for SwComponentPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwComponentPrototype = SwComponentPrototype()

    def build(self) -> SwComponentPrototype:
        """Build and return SwComponentPrototype object.

        Returns:
            SwComponentPrototype instance
        """
        # TODO: Add validation
        return self._obj
