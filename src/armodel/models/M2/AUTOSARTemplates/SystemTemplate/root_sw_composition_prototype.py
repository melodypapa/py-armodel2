"""RootSwCompositionPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1003)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 186)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 240)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 18)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_map import (
    FlatMap,
)


class RootSwCompositionPrototype(Identifiable):
    """AUTOSAR RootSwCompositionPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    calibrations: list[Any]
    flat_map: Optional[FlatMap]
    software: Optional[CompositionSwComponentType]
    def __init__(self) -> None:
        """Initialize RootSwCompositionPrototype."""
        super().__init__()
        self.calibrations: list[Any] = []
        self.flat_map: Optional[FlatMap] = None
        self.software: Optional[CompositionSwComponentType] = None
    def serialize(self) -> ET.Element:
        """Serialize RootSwCompositionPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RootSwCompositionPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize calibrations (list to container "CALIBRATIONS")
        if self.calibrations:
            wrapper = ET.Element("CALIBRATIONS")
            for item in self.calibrations:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize flat_map
        if self.flat_map is not None:
            serialized = ARObject._serialize_item(self.flat_map, "FlatMap")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-MAP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize software
        if self.software is not None:
            serialized = ARObject._serialize_item(self.software, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RootSwCompositionPrototype":
        """Deserialize XML element to RootSwCompositionPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RootSwCompositionPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RootSwCompositionPrototype, cls).deserialize(element)

        # Parse calibrations (list from container "CALIBRATIONS")
        obj.calibrations = []
        container = ARObject._find_child_element(element, "CALIBRATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.calibrations.append(child_value)

        # Parse flat_map
        child = ARObject._find_child_element(element, "FLAT-MAP")
        if child is not None:
            flat_map_value = ARObject._deserialize_by_tag(child, "FlatMap")
            obj.flat_map = flat_map_value

        # Parse software
        child = ARObject._find_child_element(element, "SOFTWARE")
        if child is not None:
            software_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.software = software_value

        return obj



class RootSwCompositionPrototypeBuilder:
    """Builder for RootSwCompositionPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RootSwCompositionPrototype = RootSwCompositionPrototype()

    def build(self) -> RootSwCompositionPrototype:
        """Build and return RootSwCompositionPrototype object.

        Returns:
            RootSwCompositionPrototype instance
        """
        # TODO: Add validation
        return self._obj
