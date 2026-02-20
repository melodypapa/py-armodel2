"""SwcToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)


class SwcToApplicationPartitionMapping(Identifiable):
    """AUTOSAR SwcToApplicationPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_ref: Optional[ARRef]
    sw_component_prototype_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcToApplicationPartitionMapping."""
        super().__init__()
        self.application_ref: Optional[ARRef] = None
        self.sw_component_prototype_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcToApplicationPartitionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToApplicationPartitionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_ref
        if self.application_ref is not None:
            serialized = ARObject._serialize_item(self.application_ref, "ApplicationPartition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_component_prototype_ref
        if self.sw_component_prototype_ref is not None:
            serialized = ARObject._serialize_item(self.sw_component_prototype_ref, "SwComponentPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToApplicationPartitionMapping":
        """Deserialize XML element to SwcToApplicationPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToApplicationPartitionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToApplicationPartitionMapping, cls).deserialize(element)

        # Parse application_ref
        child = ARObject._find_child_element(element, "APPLICATION-REF")
        if child is not None:
            application_ref_value = ARRef.deserialize(child)
            obj.application_ref = application_ref_value

        # Parse sw_component_prototype_ref
        child = ARObject._find_child_element(element, "SW-COMPONENT-PROTOTYPE-REF")
        if child is not None:
            sw_component_prototype_ref_value = ARRef.deserialize(child)
            obj.sw_component_prototype_ref = sw_component_prototype_ref_value

        return obj



class SwcToApplicationPartitionMappingBuilder:
    """Builder for SwcToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToApplicationPartitionMapping = SwcToApplicationPartitionMapping()

    def build(self) -> SwcToApplicationPartitionMapping:
        """Build and return SwcToApplicationPartitionMapping object.

        Returns:
            SwcToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
