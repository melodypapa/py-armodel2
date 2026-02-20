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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    calibration_refs: list[Any]
    flat_map_ref: Optional[ARRef]
    software: Optional[CompositionSwComponentType]
    def __init__(self) -> None:
        """Initialize RootSwCompositionPrototype."""
        super().__init__()
        self.calibration_refs: list[Any] = []
        self.flat_map_ref: Optional[ARRef] = None
        self.software: Optional[CompositionSwComponentType] = None

    def serialize(self) -> ET.Element:
        """Serialize RootSwCompositionPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RootSwCompositionPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize calibration_refs (list to container "CALIBRATION-REFS")
        if self.calibration_refs:
            wrapper = ET.Element("CALIBRATION-REFS")
            for item in self.calibration_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CALIBRATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize flat_map_ref
        if self.flat_map_ref is not None:
            serialized = ARObject._serialize_item(self.flat_map_ref, "FlatMap")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLAT-MAP-REF")
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

        # Parse calibration_refs (list from container "CALIBRATION-REFS")
        obj.calibration_refs = []
        container = ARObject._find_child_element(element, "CALIBRATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.calibration_refs.append(child_value)

        # Parse flat_map_ref
        child = ARObject._find_child_element(element, "FLAT-MAP-REF")
        if child is not None:
            flat_map_ref_value = ARRef.deserialize(child)
            obj.flat_map_ref = flat_map_ref_value

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
