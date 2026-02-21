"""AutosarEngineeringObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_EngineeringObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AutosarEngineeringObject(EngineeringObject):
    """AUTOSAR AutosarEngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize AutosarEngineeringObject."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AutosarEngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AutosarEngineeringObject, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "AutosarEngineeringObject":
        """Deserialize XML element to AutosarEngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AutosarEngineeringObject object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AutosarEngineeringObject, cls).deserialize(element)



class AutosarEngineeringObjectBuilder:
    """Builder for AutosarEngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarEngineeringObject = AutosarEngineeringObject()

    def build(self) -> AutosarEngineeringObject:
        """Build and return AutosarEngineeringObject object.

        Returns:
            AutosarEngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
