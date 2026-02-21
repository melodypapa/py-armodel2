"""DependencyOnArtifact AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 131)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    DependencyUsageEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)


class DependencyOnArtifact(Identifiable):
    """AUTOSAR DependencyOnArtifact."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    artifact: Optional[AutosarEngineeringObject]
    usage_refs: list[DependencyUsageEnum]
    def __init__(self) -> None:
        """Initialize DependencyOnArtifact."""
        super().__init__()
        self.artifact: Optional[AutosarEngineeringObject] = None
        self.usage_refs: list[DependencyUsageEnum] = []

    def serialize(self) -> ET.Element:
        """Serialize DependencyOnArtifact to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DependencyOnArtifact, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize artifact
        if self.artifact is not None:
            serialized = ARObject._serialize_item(self.artifact, "AutosarEngineeringObject")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARTIFACT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize usage_refs (list to container "USAGE-REFS")
        if self.usage_refs:
            wrapper = ET.Element("USAGE-REFS")
            for item in self.usage_refs:
                serialized = ARObject._serialize_item(item, "DependencyUsageEnum")
                if serialized is not None:
                    child_elem = ET.Element("USAGE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DependencyOnArtifact":
        """Deserialize XML element to DependencyOnArtifact object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DependencyOnArtifact object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DependencyOnArtifact, cls).deserialize(element)

        # Parse artifact
        child = ARObject._find_child_element(element, "ARTIFACT")
        if child is not None:
            artifact_value = ARObject._deserialize_by_tag(child, "AutosarEngineeringObject")
            obj.artifact = artifact_value

        # Parse usage_refs (list from container "USAGE-REFS")
        obj.usage_refs = []
        container = ARObject._find_child_element(element, "USAGE-REFS")
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
                    obj.usage_refs.append(child_value)

        return obj



class DependencyOnArtifactBuilder:
    """Builder for DependencyOnArtifact."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DependencyOnArtifact = DependencyOnArtifact()

    def build(self) -> DependencyOnArtifact:
        """Build and return DependencyOnArtifact object.

        Returns:
            DependencyOnArtifact instance
        """
        # TODO: Add validation
        return self._obj
