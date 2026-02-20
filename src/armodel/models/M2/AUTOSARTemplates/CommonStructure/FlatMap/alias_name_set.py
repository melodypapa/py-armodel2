"""AliasNameSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 174)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 968)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_assignment import (
    AliasNameAssignment,
)


class AliasNameSet(ARElement):
    """AUTOSAR AliasNameSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alias_names: list[AliasNameAssignment]
    def __init__(self) -> None:
        """Initialize AliasNameSet."""
        super().__init__()
        self.alias_names: list[AliasNameAssignment] = []

    def serialize(self) -> ET.Element:
        """Serialize AliasNameSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AliasNameSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alias_names (list to container "ALIAS-NAMES")
        if self.alias_names:
            wrapper = ET.Element("ALIAS-NAMES")
            for item in self.alias_names:
                serialized = ARObject._serialize_item(item, "AliasNameAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AliasNameSet":
        """Deserialize XML element to AliasNameSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AliasNameSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AliasNameSet, cls).deserialize(element)

        # Parse alias_names (list from container "ALIAS-NAMES")
        obj.alias_names = []
        container = ARObject._find_child_element(element, "ALIAS-NAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.alias_names.append(child_value)

        return obj



class AliasNameSetBuilder:
    """Builder for AliasNameSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AliasNameSet = AliasNameSet()

    def build(self) -> AliasNameSet:
        """Build and return AliasNameSet object.

        Returns:
            AliasNameSet instance
        """
        # TODO: Add validation
        return self._obj
