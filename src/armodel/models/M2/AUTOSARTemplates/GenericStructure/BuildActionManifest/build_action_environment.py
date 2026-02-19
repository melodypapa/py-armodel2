"""BuildActionEnvironment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 370)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionEnvironment(Identifiable):
    """AUTOSAR BuildActionEnvironment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sdgs: list[Sdg]
    def __init__(self) -> None:
        """Initialize BuildActionEnvironment."""
        super().__init__()
        self.sdgs: list[Sdg] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionEnvironment":
        """Deserialize XML element to BuildActionEnvironment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionEnvironment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sdgs (list)
        obj.sdgs = []
        for child in ARObject._find_all_child_elements(element, "SDGS"):
            sdgs_value = ARObject._deserialize_by_tag(child, "Sdg")
            obj.sdgs.append(sdgs_value)

        return obj



class BuildActionEnvironmentBuilder:
    """Builder for BuildActionEnvironment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEnvironment = BuildActionEnvironment()

    def build(self) -> BuildActionEnvironment:
        """Build and return BuildActionEnvironment object.

        Returns:
            BuildActionEnvironment instance
        """
        # TODO: Add validation
        return self._obj
