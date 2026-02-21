"""FibexElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 445)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class FibexElement(PackageableElement, ABC):
    """AUTOSAR FibexElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize FibexElement."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize FibexElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FibexElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FibexElement":
        """Deserialize XML element to FibexElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FibexElement object
        """
        # Delegate to parent class to handle inherited attributes
        return super(FibexElement, cls).deserialize(element)



class FibexElementBuilder:
    """Builder for FibexElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FibexElement = FibexElement()

    def build(self) -> FibexElement:
        """Build and return FibexElement object.

        Returns:
            FibexElement instance
        """
        # TODO: Add validation
        return self._obj
