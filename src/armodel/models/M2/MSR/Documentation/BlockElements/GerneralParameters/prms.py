"""Prms AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 338)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_GerneralParameters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class Prms(Paginateable):
    """AUTOSAR Prms."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label: Optional[MultilanguageLongName]
    prm: Any
    def __init__(self) -> None:
        """Initialize Prms."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.prm: Any = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Prms":
        """Deserialize XML element to Prms object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Prms object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse label
        child = ARObject._find_child_element(element, "LABEL")
        if child is not None:
            label_value = ARObject._deserialize_by_tag(child, "MultilanguageLongName")
            obj.label = label_value

        # Parse prm
        child = ARObject._find_child_element(element, "PRM")
        if child is not None:
            prm_value = child.text
            obj.prm = prm_value

        return obj



class PrmsBuilder:
    """Builder for Prms."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Prms = Prms()

    def build(self) -> Prms:
        """Build and return Prms object.

        Returns:
            Prms instance
        """
        # TODO: Add validation
        return self._obj
