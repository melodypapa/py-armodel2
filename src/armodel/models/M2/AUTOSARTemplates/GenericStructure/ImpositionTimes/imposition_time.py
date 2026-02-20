"""ImpositionTime AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ImpositionTimes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ImpositionTime(Identifiable):
    """AUTOSAR ImpositionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ImpositionTime."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize ImpositionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImpositionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImpositionTime":
        """Deserialize XML element to ImpositionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImpositionTime object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ImpositionTime, cls).deserialize(element)



class ImpositionTimeBuilder:
    """Builder for ImpositionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImpositionTime = ImpositionTime()

    def build(self) -> ImpositionTime:
        """Build and return ImpositionTime object.

        Returns:
            ImpositionTime instance
        """
        # TODO: Add validation
        return self._obj
