"""SwcServiceDependencyInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """AUTOSAR SwcServiceDependencyInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_root_sw_ref: Optional[ARRef]
    context_sw_prototype_refs: list[Any]
    target_swc_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize SwcServiceDependencyInSystemInstanceRef."""
        super().__init__()
        self.context_root_sw_ref: Optional[ARRef] = None
        self.context_sw_prototype_refs: list[Any] = []
        self.target_swc_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcServiceDependencyInSystemInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize context_root_sw_ref
        if self.context_root_sw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_root_sw_ref, "RootSwCompositionPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ROOT-SW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_sw_prototype_refs (list to container "CONTEXT-SW-PROTOTYPE-REFS")
        if self.context_sw_prototype_refs:
            wrapper = ET.Element("CONTEXT-SW-PROTOTYPE-REFS")
            for item in self.context_sw_prototype_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-SW-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_swc_ref
        if self.target_swc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_swc_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-SWC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependencyInSystemInstanceRef":
        """Deserialize XML element to SwcServiceDependencyInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependencyInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_root_sw_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-ROOT-SW-REF")
        if child is not None:
            context_root_sw_ref_value = ARRef.deserialize(child)
            obj.context_root_sw_ref = context_root_sw_ref_value

        # Parse context_sw_prototype_refs (list from container "CONTEXT-SW-PROTOTYPE-REFS")
        obj.context_sw_prototype_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-SW-PROTOTYPE-REFS")
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
                    obj.context_sw_prototype_refs.append(child_value)

        # Parse target_swc_ref
        child = SerializationHelper.find_child_element(element, "TARGET-SWC-REF")
        if child is not None:
            target_swc_ref_value = ARRef.deserialize(child)
            obj.target_swc_ref = target_swc_ref_value

        return obj



class SwcServiceDependencyInSystemInstanceRefBuilder:
    """Builder for SwcServiceDependencyInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependencyInSystemInstanceRef = SwcServiceDependencyInSystemInstanceRef()

    def build(self) -> SwcServiceDependencyInSystemInstanceRef:
        """Build and return SwcServiceDependencyInSystemInstanceRef object.

        Returns:
            SwcServiceDependencyInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
