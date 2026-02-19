"""SwcToImplMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation.swc_implementation import (
    SwcImplementation,
)


class SwcToImplMapping(Identifiable):
    """AUTOSAR SwcToImplMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    component: Optional[SwcImplementation]
    def __init__(self) -> None:
        """Initialize SwcToImplMapping."""
        super().__init__()
        self.component: Optional[SwcImplementation] = None
    def serialize(self) -> ET.Element:
        """Serialize SwcToImplMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToImplMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component
        if self.component is not None:
            serialized = ARObject._serialize_item(self.component, "SwcImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToImplMapping":
        """Deserialize XML element to SwcToImplMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToImplMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToImplMapping, cls).deserialize(element)

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = ARObject._deserialize_by_tag(child, "SwcImplementation")
            obj.component = component_value

        return obj



class SwcToImplMappingBuilder:
    """Builder for SwcToImplMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToImplMapping = SwcToImplMapping()

    def build(self) -> SwcToImplMapping:
        """Build and return SwcToImplMapping object.

        Returns:
            SwcToImplMapping instance
        """
        # TODO: Add validation
        return self._obj
