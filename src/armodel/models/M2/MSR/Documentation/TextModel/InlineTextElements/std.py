"""Std AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class Std(SingleLanguageReferrable):
    """AUTOSAR Std."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    date: Optional[DateTime]
    position: Optional[String]
    state: Optional[String]
    subtitle: Optional[String]
    url: Optional[Any]
    def __init__(self) -> None:
        """Initialize Std."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.position: Optional[String] = None
        self.state: Optional[String] = None
        self.subtitle: Optional[String] = None
        self.url: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Std":
        """Deserialize XML element to Std object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Std object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Std, cls).deserialize(element)

        # Parse date
        child = ARObject._find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse position
        child = ARObject._find_child_element(element, "POSITION")
        if child is not None:
            position_value = child.text
            obj.position = position_value

        # Parse state
        child = ARObject._find_child_element(element, "STATE")
        if child is not None:
            state_value = child.text
            obj.state = state_value

        # Parse subtitle
        child = ARObject._find_child_element(element, "SUBTITLE")
        if child is not None:
            subtitle_value = child.text
            obj.subtitle = subtitle_value

        # Parse url
        child = ARObject._find_child_element(element, "URL")
        if child is not None:
            url_value = child.text
            obj.url = url_value

        return obj



class StdBuilder:
    """Builder for Std."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Std = Std()

    def build(self) -> Std:
        """Build and return Std object.

        Returns:
            Std instance
        """
        # TODO: Add validation
        return self._obj
