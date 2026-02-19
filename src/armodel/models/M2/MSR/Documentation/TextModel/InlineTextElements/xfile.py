"""Xfile AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 319)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Xfile(SingleLanguageReferrable):
    """AUTOSAR Xfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tool: Optional[String]
    tool_version: Optional[String]
    url: Optional[Any]
    def __init__(self) -> None:
        """Initialize Xfile."""
        super().__init__()
        self.tool: Optional[String] = None
        self.tool_version: Optional[String] = None
        self.url: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xfile":
        """Deserialize XML element to Xfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xfile object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tool
        child = ARObject._find_child_element(element, "TOOL")
        if child is not None:
            tool_value = child.text
            obj.tool = tool_value

        # Parse tool_version
        child = ARObject._find_child_element(element, "TOOL-VERSION")
        if child is not None:
            tool_version_value = child.text
            obj.tool_version = tool_version_value

        # Parse url
        child = ARObject._find_child_element(element, "URL")
        if child is not None:
            url_value = child.text
            obj.url = url_value

        return obj



class XfileBuilder:
    """Builder for Xfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xfile = Xfile()

    def build(self) -> Xfile:
        """Build and return Xfile object.

        Returns:
            Xfile instance
        """
        # TODO: Add validation
        return self._obj
