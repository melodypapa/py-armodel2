"""IdsDesign AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 16)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)


class IdsDesign(ARElement):
    """AUTOSAR IdsDesign."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    elements: list[IdsCommonElement]
    def __init__(self) -> None:
        """Initialize IdsDesign."""
        super().__init__()
        self.elements: list[IdsCommonElement] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsDesign":
        """Deserialize XML element to IdsDesign object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsDesign object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse elements (list)
        obj.elements = []
        for child in ARObject._find_all_child_elements(element, "ELEMENTS"):
            elements_value = ARObject._deserialize_by_tag(child, "IdsCommonElement")
            obj.elements.append(elements_value)

        return obj



class IdsDesignBuilder:
    """Builder for IdsDesign."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsDesign = IdsDesign()

    def build(self) -> IdsDesign:
        """Build and return IdsDesign object.

        Returns:
            IdsDesign instance
        """
        # TODO: Add validation
        return self._obj
