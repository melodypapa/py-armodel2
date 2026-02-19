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
    usage_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DependencyOnArtifact."""
        super().__init__()
        self.artifact: Optional[AutosarEngineeringObject] = None
        self.usage_refs: list[ARRef] = []
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

        # Parse usage_refs (list from container "USAGES")
        obj.usage_refs = []
        container = ARObject._find_child_element(element, "USAGES")
        if container is not None:
            for child in container:
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
