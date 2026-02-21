"""BuildAction AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 366)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 172)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_entity import (
    BuildActionEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_io_element import (
    BuildActionIoElement,
)


class BuildAction(BuildActionEntity):
    """AUTOSAR BuildAction."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    created_datas: list[BuildActionIoElement]
    follow_up_action_refs: list[ARRef]
    input_datas: list[BuildActionIoElement]
    modified_datas: list[BuildActionIoElement]
    predecessor_refs: list[ARRef]
    required_ref: ARRef
    def __init__(self) -> None:
        """Initialize BuildAction."""
        super().__init__()
        self.created_datas: list[BuildActionIoElement] = []
        self.follow_up_action_refs: list[ARRef] = []
        self.input_datas: list[BuildActionIoElement] = []
        self.modified_datas: list[BuildActionIoElement] = []
        self.predecessor_refs: list[ARRef] = []
        self.required_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize BuildAction to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildAction, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize created_datas (list to container "CREATED-DATAS")
        if self.created_datas:
            wrapper = ET.Element("CREATED-DATAS")
            for item in self.created_datas:
                serialized = SerializationHelper.serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize follow_up_action_refs (list to container "FOLLOW-UP-ACTION-REFS")
        if self.follow_up_action_refs:
            wrapper = ET.Element("FOLLOW-UP-ACTION-REFS")
            for item in self.follow_up_action_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("FOLLOW-UP-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize input_datas (list to container "INPUT-DATAS")
        if self.input_datas:
            wrapper = ET.Element("INPUT-DATAS")
            for item in self.input_datas:
                serialized = SerializationHelper.serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize modified_datas (list to container "MODIFIED-DATAS")
        if self.modified_datas:
            wrapper = ET.Element("MODIFIED-DATAS")
            for item in self.modified_datas:
                serialized = SerializationHelper.serialize_item(item, "BuildActionIoElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize predecessor_refs (list to container "PREDECESSOR-REFS")
        if self.predecessor_refs:
            wrapper = ET.Element("PREDECESSOR-REFS")
            for item in self.predecessor_refs:
                serialized = SerializationHelper.serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("PREDECESSOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_ref
        if self.required_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_ref, "BuildActionEnvironment")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildAction":
        """Deserialize XML element to BuildAction object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildAction object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildAction, cls).deserialize(element)

        # Parse created_datas (list from container "CREATED-DATAS")
        obj.created_datas = []
        container = SerializationHelper.find_child_element(element, "CREATED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.created_datas.append(child_value)

        # Parse follow_up_action_refs (list from container "FOLLOW-UP-ACTION-REFS")
        obj.follow_up_action_refs = []
        container = SerializationHelper.find_child_element(element, "FOLLOW-UP-ACTION-REFS")
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
                    obj.follow_up_action_refs.append(child_value)

        # Parse input_datas (list from container "INPUT-DATAS")
        obj.input_datas = []
        container = SerializationHelper.find_child_element(element, "INPUT-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.input_datas.append(child_value)

        # Parse modified_datas (list from container "MODIFIED-DATAS")
        obj.modified_datas = []
        container = SerializationHelper.find_child_element(element, "MODIFIED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.modified_datas.append(child_value)

        # Parse predecessor_refs (list from container "PREDECESSOR-REFS")
        obj.predecessor_refs = []
        container = SerializationHelper.find_child_element(element, "PREDECESSOR-REFS")
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
                    obj.predecessor_refs.append(child_value)

        # Parse required_ref
        child = SerializationHelper.find_child_element(element, "REQUIRED-REF")
        if child is not None:
            required_ref_value = ARRef.deserialize(child)
            obj.required_ref = required_ref_value

        return obj



class BuildActionBuilder:
    """Builder for BuildAction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildAction = BuildAction()

    def build(self) -> BuildAction:
        """Build and return BuildAction object.

        Returns:
            BuildAction instance
        """
        # TODO: Add validation
        return self._obj
