"""ComponentSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.mapping_constraint import (
    MappingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    MappingScopeEnum,
)


class ComponentSeparation(MappingConstraint):
    """AUTOSAR ComponentSeparation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mapping_scope_enum_ref: Optional[MappingScopeEnum]
    def __init__(self) -> None:
        """Initialize ComponentSeparation."""
        super().__init__()
        self.mapping_scope_enum_ref: Optional[MappingScopeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ComponentSeparation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ComponentSeparation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mapping_scope_enum_ref
        if self.mapping_scope_enum_ref is not None:
            serialized = ARObject._serialize_item(self.mapping_scope_enum_ref, "MappingScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPING-SCOPE-ENUM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComponentSeparation":
        """Deserialize XML element to ComponentSeparation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComponentSeparation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComponentSeparation, cls).deserialize(element)

        # Parse mapping_scope_enum_ref
        child = ARObject._find_child_element(element, "MAPPING-SCOPE-ENUM-REF")
        if child is not None:
            mapping_scope_enum_ref_value = ARRef.deserialize(child)
            obj.mapping_scope_enum_ref = mapping_scope_enum_ref_value

        return obj



class ComponentSeparationBuilder:
    """Builder for ComponentSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComponentSeparation = ComponentSeparation()

    def build(self) -> ComponentSeparation:
        """Build and return ComponentSeparation object.

        Returns:
            ComponentSeparation instance
        """
        # TODO: Add validation
        return self._obj
