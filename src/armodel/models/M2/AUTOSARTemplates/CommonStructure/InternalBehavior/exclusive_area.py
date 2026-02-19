"""ExclusiveArea AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 82)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 552)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ExclusiveArea(Identifiable):
    """AUTOSAR ExclusiveArea."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ExclusiveArea."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize ExclusiveArea to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExclusiveArea, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExclusiveArea":
        """Deserialize XML element to ExclusiveArea object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExclusiveArea object
        """
        # Delegate to parent class to handle inherited attributes
        return super(ExclusiveArea, cls).deserialize(element)



class ExclusiveAreaBuilder:
    """Builder for ExclusiveArea."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveArea = ExclusiveArea()

    def build(self) -> ExclusiveArea:
        """Build and return ExclusiveArea object.

        Returns:
            ExclusiveArea instance
        """
        # TODO: Add validation
        return self._obj
