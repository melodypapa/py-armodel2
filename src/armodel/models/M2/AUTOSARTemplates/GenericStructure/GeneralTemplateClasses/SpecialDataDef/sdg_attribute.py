"""SdgAttribute AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class SdgAttribute(Identifiable, ABC):
    """AUTOSAR SdgAttribute."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SdgAttribute."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize SdgAttribute to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgAttribute, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAttribute":
        """Deserialize XML element to SdgAttribute object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgAttribute object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SdgAttribute, cls).deserialize(element)



class SdgAttributeBuilder:
    """Builder for SdgAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAttribute = SdgAttribute()

    def build(self) -> SdgAttribute:
        """Build and return SdgAttribute object.

        Returns:
            SdgAttribute instance
        """
        # TODO: Add validation
        return self._obj
