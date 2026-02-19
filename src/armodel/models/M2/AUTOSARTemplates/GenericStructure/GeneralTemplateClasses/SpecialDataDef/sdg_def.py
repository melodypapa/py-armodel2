"""SdgDef AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgDef(ARElement):
    """AUTOSAR SdgDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sdg_classes: list[SdgClass]
    def __init__(self) -> None:
        """Initialize SdgDef."""
        super().__init__()
        self.sdg_classes: list[SdgClass] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgDef":
        """Deserialize XML element to SdgDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgDef, cls).deserialize(element)

        # Parse sdg_classes (list from container "SDG-CLASSES")
        obj.sdg_classes = []
        container = ARObject._find_child_element(element, "SDG-CLASSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdg_classes.append(child_value)

        return obj



class SdgDefBuilder:
    """Builder for SdgDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgDef = SdgDef()

    def build(self) -> SdgDef:
        """Build and return SdgDef object.

        Returns:
            SdgDef instance
        """
        # TODO: Add validation
        return self._obj
