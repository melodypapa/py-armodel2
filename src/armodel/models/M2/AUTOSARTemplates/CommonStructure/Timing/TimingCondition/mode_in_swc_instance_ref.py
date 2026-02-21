"""ModeInSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 38)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)


class ModeInSwcInstanceRef(ARObject):
    """AUTOSAR ModeInSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    context_refs: list[Any]
    context_mode_ref: Optional[ARRef]
    context_port_ref: Optional[ARRef]
    target_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeInSwcInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_refs: list[Any] = []
        self.context_mode_ref: Optional[ARRef] = None
        self.context_port_ref: Optional[ARRef] = None
        self.target_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeInSwcInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "SwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_refs (list to container "CONTEXT-REFS")
        if self.context_refs:
            wrapper = ET.Element("CONTEXT-REFS")
            for item in self.context_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize context_mode_ref
        if self.context_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_port_ref
        if self.context_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_mode_ref
        if self.target_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeInSwcInstanceRef":
        """Deserialize XML element to ModeInSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeInSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_refs (list from container "CONTEXT-REFS")
        obj.context_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-REFS")
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
                    obj.context_refs.append(child_value)

        # Parse context_mode_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-MODE-REF")
        if child is not None:
            context_mode_ref_value = ARRef.deserialize(child)
            obj.context_mode_ref = context_mode_ref_value

        # Parse context_port_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-PORT-REF")
        if child is not None:
            context_port_ref_value = ARRef.deserialize(child)
            obj.context_port_ref = context_port_ref_value

        # Parse target_mode_ref
        child = SerializationHelper.find_child_element(element, "TARGET-MODE-REF")
        if child is not None:
            target_mode_ref_value = ARRef.deserialize(child)
            obj.target_mode_ref = target_mode_ref_value

        return obj



class ModeInSwcInstanceRefBuilder:
    """Builder for ModeInSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInSwcInstanceRef = ModeInSwcInstanceRef()

    def build(self) -> ModeInSwcInstanceRef:
        """Build and return ModeInSwcInstanceRef object.

        Returns:
            ModeInSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
