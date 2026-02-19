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

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class SwComponentPrototype(Identifiable):
    """AUTOSAR SwComponentPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type: Optional[SwComponentType]
    def __init__(self) -> None:
        """Initialize SwComponentPrototype."""
        super().__init__()
        self.type: Optional[SwComponentType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentPrototype":
        """Deserialize XML element to SwComponentPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse type
        child = ARObject._find_child_element(element, "TYPE")
        if child is not None:
            type_value = ARObject._deserialize_by_tag(child, "SwComponentType")
            obj.type = type_value

        return obj



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
