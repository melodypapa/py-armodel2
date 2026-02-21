"""BuildActionManifest AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 134)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 365)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action import (
    BuildAction,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_environment import (
    BuildActionEnvironment,
)


class BuildActionManifest(ARElement):
    """AUTOSAR BuildActionManifest."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    build_actions: list[BuildActionEnvironment]
    dynamic_action_refs: list[ARRef]
    start_action_refs: list[ARRef]
    tear_down_action_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BuildActionManifest."""
        super().__init__()
        self.build_actions: list[BuildActionEnvironment] = []
        self.dynamic_action_refs: list[ARRef] = []
        self.start_action_refs: list[ARRef] = []
        self.tear_down_action_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BuildActionManifest to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildActionManifest, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize build_actions (list to container "BUILD-ACTIONS")
        if self.build_actions:
            wrapper = ET.Element("BUILD-ACTIONS")
            for item in self.build_actions:
                serialized = ARObject._serialize_item(item, "BuildActionEnvironment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dynamic_action_refs (list to container "DYNAMIC-ACTION-REFS")
        if self.dynamic_action_refs:
            wrapper = ET.Element("DYNAMIC-ACTION-REFS")
            for item in self.dynamic_action_refs:
                serialized = ARObject._serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("DYNAMIC-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize start_action_refs (list to container "START-ACTION-REFS")
        if self.start_action_refs:
            wrapper = ET.Element("START-ACTION-REFS")
            for item in self.start_action_refs:
                serialized = ARObject._serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("START-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tear_down_action_refs (list to container "TEAR-DOWN-ACTION-REFS")
        if self.tear_down_action_refs:
            wrapper = ET.Element("TEAR-DOWN-ACTION-REFS")
            for item in self.tear_down_action_refs:
                serialized = ARObject._serialize_item(item, "BuildAction")
                if serialized is not None:
                    child_elem = ET.Element("TEAR-DOWN-ACTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionManifest":
        """Deserialize XML element to BuildActionManifest object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionManifest object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionManifest, cls).deserialize(element)

        # Parse build_actions (list from container "BUILD-ACTIONS")
        obj.build_actions = []
        container = ARObject._find_child_element(element, "BUILD-ACTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.build_actions.append(child_value)

        # Parse dynamic_action_refs (list from container "DYNAMIC-ACTION-REFS")
        obj.dynamic_action_refs = []
        container = ARObject._find_child_element(element, "DYNAMIC-ACTION-REFS")
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
                    obj.dynamic_action_refs.append(child_value)

        # Parse start_action_refs (list from container "START-ACTION-REFS")
        obj.start_action_refs = []
        container = ARObject._find_child_element(element, "START-ACTION-REFS")
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
                    obj.start_action_refs.append(child_value)

        # Parse tear_down_action_refs (list from container "TEAR-DOWN-ACTION-REFS")
        obj.tear_down_action_refs = []
        container = ARObject._find_child_element(element, "TEAR-DOWN-ACTION-REFS")
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
                    obj.tear_down_action_refs.append(child_value)

        return obj



class BuildActionManifestBuilder:
    """Builder for BuildActionManifest."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionManifest = BuildActionManifest()

    def build(self) -> BuildActionManifest:
        """Build and return BuildActionManifest object.

        Returns:
            BuildActionManifest instance
        """
        # TODO: Add validation
        return self._obj
