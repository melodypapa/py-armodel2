"""SwcBswMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 656)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcBswMapping(ARElement):
    """AUTOSAR SwcBswMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_behavior_ref: Optional[ARRef]
    runnable_mapping_refs: list[ARRef]
    swc_behavior_ref: Optional[ARRef]
    synchronizeds: list[Any]
    def __init__(self) -> None:
        """Initialize SwcBswMapping."""
        super().__init__()
        self.bsw_behavior_ref: Optional[ARRef] = None
        self.runnable_mapping_refs: list[ARRef] = []
        self.swc_behavior_ref: Optional[ARRef] = None
        self.synchronizeds: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SwcBswMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcBswMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_behavior_ref
        if self.bsw_behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_behavior_ref, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runnable_mapping_refs (list to container "RUNNABLE-MAPPING-REFS")
        if self.runnable_mapping_refs:
            wrapper = ET.Element("RUNNABLE-MAPPING-REFS")
            for item in self.runnable_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "SwcBswRunnableMapping")
                if serialized is not None:
                    child_elem = ET.Element("RUNNABLE-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_behavior_ref
        if self.swc_behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_behavior_ref, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize synchronizeds (list to container "SYNCHRONIZEDS")
        if self.synchronizeds:
            wrapper = ET.Element("SYNCHRONIZEDS")
            for item in self.synchronizeds:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswMapping":
        """Deserialize XML element to SwcBswMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcBswMapping, cls).deserialize(element)

        # Parse bsw_behavior_ref
        child = SerializationHelper.find_child_element(element, "BSW-BEHAVIOR-REF")
        if child is not None:
            bsw_behavior_ref_value = ARRef.deserialize(child)
            obj.bsw_behavior_ref = bsw_behavior_ref_value

        # Parse runnable_mapping_refs (list from container "RUNNABLE-MAPPING-REFS")
        obj.runnable_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "RUNNABLE-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnable_mapping_refs.append(child_value)

        # Parse swc_behavior_ref
        child = SerializationHelper.find_child_element(element, "SWC-BEHAVIOR-REF")
        if child is not None:
            swc_behavior_ref_value = ARRef.deserialize(child)
            obj.swc_behavior_ref = swc_behavior_ref_value

        # Parse synchronizeds (list from container "SYNCHRONIZEDS")
        obj.synchronizeds = []
        container = SerializationHelper.find_child_element(element, "SYNCHRONIZEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.synchronizeds.append(child_value)

        return obj



class SwcBswMappingBuilder:
    """Builder for SwcBswMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswMapping = SwcBswMapping()

    def build(self) -> SwcBswMapping:
        """Build and return SwcBswMapping object.

        Returns:
            SwcBswMapping instance
        """
        # TODO: Add validation
        return self._obj
