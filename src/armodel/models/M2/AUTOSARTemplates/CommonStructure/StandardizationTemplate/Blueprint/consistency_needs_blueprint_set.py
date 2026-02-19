"""ConsistencyNeedsBlueprintSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Blueprint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
    ConsistencyNeeds,
)


class ConsistencyNeedsBlueprintSet(ARElement):
    """AUTOSAR ConsistencyNeedsBlueprintSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consistency_needses: list[ConsistencyNeeds]
    def __init__(self) -> None:
        """Initialize ConsistencyNeedsBlueprintSet."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeedsBlueprintSet":
        """Deserialize XML element to ConsistencyNeedsBlueprintSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeedsBlueprintSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse consistency_needses (list)
        obj.consistency_needses = []
        for child in ARObject._find_all_child_elements(element, "CONSISTENCY-NEEDSES"):
            consistency_needses_value = ARObject._deserialize_by_tag(child, "ConsistencyNeeds")
            obj.consistency_needses.append(consistency_needses_value)

        return obj



class ConsistencyNeedsBlueprintSetBuilder:
    """Builder for ConsistencyNeedsBlueprintSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsistencyNeedsBlueprintSet = ConsistencyNeedsBlueprintSet()

    def build(self) -> ConsistencyNeedsBlueprintSet:
        """Build and return ConsistencyNeedsBlueprintSet object.

        Returns:
            ConsistencyNeedsBlueprintSet instance
        """
        # TODO: Add validation
        return self._obj
