"""LLongName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class LLongName(ARObject):
    """AUTOSAR LLongName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    blueprint_value: Optional[String]
    def __init__(self) -> None:
        """Initialize LLongName."""
        super().__init__()
        self.blueprint_value: Optional[String] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LLongName":
        """Deserialize XML element to LLongName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LLongName object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse blueprint_value
        child = ARObject._find_child_element(element, "BLUEPRINT-VALUE")
        if child is not None:
            blueprint_value_value = child.text
            obj.blueprint_value = blueprint_value_value

        return obj



class LLongNameBuilder:
    """Builder for LLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LLongName = LLongName()

    def build(self) -> LLongName:
        """Build and return LLongName object.

        Returns:
            LLongName instance
        """
        # TODO: Add validation
        return self._obj
