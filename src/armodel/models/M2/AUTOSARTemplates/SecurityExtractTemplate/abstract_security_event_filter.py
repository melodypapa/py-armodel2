"""AbstractSecurityEventFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 21)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractSecurityEventFilter(Identifiable, ABC):
    """AUTOSAR AbstractSecurityEventFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractSecurityEventFilter."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AbstractSecurityEventFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractSecurityEventFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractSecurityEventFilter":
        """Deserialize XML element to AbstractSecurityEventFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractSecurityEventFilter object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AbstractSecurityEventFilter, cls).deserialize(element)



class AbstractSecurityEventFilterBuilder:
    """Builder for AbstractSecurityEventFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractSecurityEventFilter = AbstractSecurityEventFilter()

    def build(self) -> AbstractSecurityEventFilter:
        """Build and return AbstractSecurityEventFilter object.

        Returns:
            AbstractSecurityEventFilter instance
        """
        # TODO: Add validation
        return self._obj
